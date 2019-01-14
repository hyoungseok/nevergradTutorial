from nevergrad.optimization import optimizerlib


def square(x):
    return (x - 0.75)**2


optimizer = optimizerlib.OnePlusOne(dimension=1, budget=100, num_workers=5)
recommendation = optimizer.optimize(square, executor=None, batch_mode=True)

print(recommendation)
