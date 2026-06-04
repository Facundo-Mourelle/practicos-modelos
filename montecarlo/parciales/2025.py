import numpy as np

def g(u):
    return (1 + 6*u +((1 + 6*u)(1/2))(1/2))

def montecarlo(n=1000):
    total = 0
    for _ in range(n):
        num = np.random.uniform()
        total += g(num)
    return total / n

#print(f'1000:   {montecarlo(10000):.6f}')
#print(f'10000:  {montecarlo(100000):.6f}')
#print(f'100000: {montecarlo(1000000):.6f}')

def juego():
    sum = 0
    count = 0
    while sum <= 1:
        w = np.random.uniform()
        count += 1
        sum += w
    return count

def par(N):
    total = 0
    for _ in range(N):
        x = juego()
        if x % 2 == 1:
            total += 1
    return total

print(f'{par(100)}')
print(f'{par(1000)}')
print(f'{par(10000)}')
