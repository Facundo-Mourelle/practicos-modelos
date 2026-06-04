import numpy as np

def gamma(n, lamda):
    suma_logs = sum(np.log(1 - np.random.uniform()) for _ in range(n))
    return -(suma_logs) / lamda

res = gamma(1000, 6)
print(f'{res}')
