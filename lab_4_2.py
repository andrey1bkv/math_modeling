import numpy as np
def umnozalka(sklad):
    p = 1
    for i in range(len(sklad)):
        p = p * sklad[i]
    return p 

test_1 = np.arange(1, 33, 5)
umnozalka(test_1)

print(umnozalka(test_1))