import math
import pytest

# --- functions under test (import them in practice) ---
def inverse_kin(v, w, L=0.15):
    return v - w * L / 2, v + w * L / 2

def forward_kin(vl, vr, L=0.15):
    return (vl + vr) / 2, (vr - vl) / L

class PID:
    def __init__(self, kp, ki, kd, lo=-255, hi=255):
        self.kp, self.ki, self.kd = kp, ki, kd
        self.lo, self.hi = lo, hi
        self.i, self.prev = 0.0, None
    def update(self, sp, meas, dt):
        e = sp - meas
        d = 0 if self.prev is None else \
            -(meas - self.prev) / dt
        self.prev = meas
        ni = self.i + e * dt
        out = self.kp * e + self.ki * ni + self.kd * d
        if self.lo < out < self.hi:
            self.i = ni
        return max(self.lo, min(self.hi, out))

def wrap(a):
    return math.atan2(math.sin(a), math.cos(a))

# --- tests ---
def test_kinematics_round_trip():
    for v, w in [(0.2, 0.0), (0.1, 1.0), (0.0, -2.0)]:
        vl, vr = inverse_kin(v, w)
        v2, w2 = forward_kin(vl, vr)
        assert v2 == pytest.approx(v)
        assert w2 == pytest.approx(w)

def test_rotate_in_place_has_opposite_wheels():
    vl, vr = inverse_kin(0.0, 1.0)
    assert vl == pytest.approx(-vr)

def test_pid_output_is_limited():
    pid = PID(1000, 0, 0)
    assert pid.update(10, 0, 0.1) == 255
    assert pid.update(-10, 0, 0.1) == -255

def test_pid_no_windup_when_saturated():
    pid = PID(1000, 100, 0)
    for _ in range(100):
        pid.update(10, 0, 0.1)      # saturated
    assert pid.i == pytest.approx(0.0)

@pytest.mark.parametrize("angle, expected", [
    (0.0, 0.0), (math.pi * 3, math.pi),
    (-math.pi / 2, -math.pi / 2),
    (7.0, 7.0 - 2 * math.pi)])
def test_wrap(angle, expected):
    assert abs(wrap(angle)) <= math.pi
    assert math.cos(wrap(angle)) == \
        pytest.approx(math.cos(expected))
