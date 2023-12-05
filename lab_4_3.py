import numpy as np
def energia(m, v):
    e = m / 2 * v / 2 * v / 2
    return e

test_1 = np.arange(1, 33,)
energia(test_1)

print(energia(test_1))

