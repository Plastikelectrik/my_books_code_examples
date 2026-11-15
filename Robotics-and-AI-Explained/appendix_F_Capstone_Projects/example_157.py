import numpy as np

rng = np.random.default_rng(3)
dt, speed = 0.1, 0.5                   # s, m/s
true_x, odo_x = 0.0, 0.0
est_x, P = 0.0, 0.01        # estimate, variance
Q, R = 0.0004, 0.01         # process, sensor noise
LANDMARKS = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
err_odo, err_kf = [], []

for step in range(1, 201):
    true_x += speed * dt
    moved = speed * dt * (1 + rng.normal(0.03, 0.02))
    odo_x += moved
    est_x += moved                     # predict
    P += Q
    if step % 20 == 0:       # a landmark is seen
        lm = min(LANDMARKS, key=lambda m: abs(m - true_x))
        z = lm - true_x + rng.normal(0, 0.1)
        meas_x = lm - z      # position from landmark
        K = P / (P + R)                # update
        est_x += K * (meas_x - est_x)
        P = (1 - K) * P
    err_odo.append(abs(odo_x - true_x))
    err_kf.append(abs(est_x - true_x))
    if step % 40 == 0:
        print(f"t={step * dt:4.1f} s  true={true_x:5.2f} "
              f"odo={odo_x:5.2f} kf={est_x:5.2f}")
print(f"final odometry error: {err_odo[-1]*100:.1f} cm")
print(f"final Kalman error  : {err_kf[-1]*100:.1f} cm")
print(f"mean Kalman error : {np.mean(err_kf)*100:.1f} cm")
