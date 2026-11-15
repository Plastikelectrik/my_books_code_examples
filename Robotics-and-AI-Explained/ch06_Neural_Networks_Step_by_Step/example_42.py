# A single neuron with hand-chosen weights (OR logic)
def perceptron(x1, x2, w1, w2, b):
    z = w1 * x1 + w2 * x2 + b
    return 1 if z > 0 else 0

w1, w2, b = 1.0, 1.0, -0.5
print("obstacle person -> stop")
for x1 in [0, 1]:
    for x2 in [0, 1]:
        out = perceptron(x1, x2, w1, w2, b)
        print(f"   {x1}       {x2}    ->  {out}")
