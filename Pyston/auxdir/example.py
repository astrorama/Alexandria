import numpy as np
import pyston

a = 42


def myfunc1(x):
    return -x / 2 + np.power(x, 5)


def myfunc2(x, y):
    z = 5 + (y > 0.)
    return x + pyston.world2pix(y * z**np.log(x))


setattr(pyston, 'evaluate', dict())
#pyston.evaluate[0] = lambda: 5
#pyston.evaluate[1] = lambda x: True + x
pyston.evaluate[2] = lambda x, y: myfunc2(x, y)
#pyston.evaluate[3] = lambda x, y, z: z + y + x  # myfunc2(x, y)
