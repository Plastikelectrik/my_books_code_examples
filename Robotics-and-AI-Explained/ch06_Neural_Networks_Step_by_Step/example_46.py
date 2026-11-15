# Find the minimum of loss(w) = (w - 3)^2 step by step
def loss(w):
    return (w - 3) ** 2

def gradient(w):
    return 2 * (w - 3)       # slope of the loss

w = -2.0
lr = 0.2
for step in range(12):
    w = w - lr * gradient(w)
    if step % 2 == 1:
        print(f"step {step + 1:2d}: w={w:6.3f} "
              f"loss={loss(w):.4f}")
