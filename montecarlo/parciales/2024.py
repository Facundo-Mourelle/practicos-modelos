# Ejercicio 3
# integral de 1 a inf de 1 / (x² * ln(x+1))

import numpy as np

def g(u):
    return 1/np.log(1+u)-np.log(u)

def monte_carlo(N):
    total = 0
    for _ in range(N):
        num = np.random.uniform()
        total += g(num)
    return total / N

print(f'1000:   {monte_carlo(1000):.6f}')
print(f'10000:  {monte_carlo(10000):.6f}')
print(f'100000: {monte_carlo(100000):.6f}')

