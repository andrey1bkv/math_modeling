import numpy as np
def summing(sklad):
    s = 0
    for i in range(len(sklad)):
        s = s + sklad[i]
    return s/len(sklad) 

test_1 = np.arange(0, 444, 1)
summing(test_1)   

print(summing(test_1))
