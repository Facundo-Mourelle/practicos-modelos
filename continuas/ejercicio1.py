import numpy as np

def f1():
    U = np.random.uniform()
    if U < 0.25:
        return 2 + 2*np.sqrt(U)
    else:
        return 6 - np.sqrt(12*(1-U))

def f2():
    U = np.random.uniform()
    if U < 0.6:
        return 3 - np.sqrt(9 + 35*U/3)
    else:
        return np.cbrt((35*U - 19)/2)

