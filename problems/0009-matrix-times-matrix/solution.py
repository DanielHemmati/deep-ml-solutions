import numpy as np

def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

    if len(a[0]) != len(b):
        return -1
    
    a_t = np.array(a)
    b_t = np.array(b)

    return a_t @ b_t