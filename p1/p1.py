import matplotlib.pyplot as plt
import numpy


def func(x):
    return 2 ** x + 3 ** x


xs = [x for x in numpy.arange(-2, 5, 0.1)]
ys = [func(x) for x in xs]

plt.plot(xs, ys, "y--")
plt.savefig("exponent.png")
