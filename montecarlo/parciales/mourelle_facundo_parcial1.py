import numpy as np

# Ejercicio 1b
def g(u):
    return np.exp(1 - 4*u + np.exp(1 - 4*u))

def monte_carlo(N):
    total = 0
    for _ in range(N):
        num = np.random.uniform()
        total += g(num)
    return total * 4 / N

print(f'  1000: {monte_carlo(1000):.6f}')
print(f' 10000: {monte_carlo(10000):.6f}')
print(f'100000: {monte_carlo(100000):.6f}')

