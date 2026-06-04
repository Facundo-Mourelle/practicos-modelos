import numpy as np
def montecarlo(g, Nsim):
    integral = 0
    for _ in range(Nsim):
        integral += g(np.random.uniform())
    return integral / Nsim

# Ejercicio a
print('=== EJERCICIO A ===')
def g1(u):
    return (1 - u ** 2) ** (1.5)

print(f'n=1000 -> {montecarlo(g1,1000)}')
print(f'n=10000 -> {montecarlo(g1,10000)}')
print(f'n=100000 -> {montecarlo(g1,100000)}')
print(f'n=1000000 -> {montecarlo(g1,1000000)}')

# Ejercicio b
print('=== EJERCICIO B ===')
def g2(u):
    return ((u+2)/((u+2)**2)-1)

print(f'n=1000 -> {montecarlo(g2,1000)}')
print(f'n=10000 -> {montecarlo(g2,10000)}')
print(f'n=100000 -> {montecarlo(g2,100000)}')
print(f'n=1000000 -> {montecarlo(g2,1000000)}')

# Ejercicio c
print('=== EJERCICIO C ===')
def g3(u):
    return ((1/u+1)/u**2 * (1 + (1/u+1)**2)**2)

print(f'n=1000 -> {montecarlo(g3,1000)}')
print(f'n=10000 -> {montecarlo(g3,10000)}')
print(f'n=100000 -> {montecarlo(g3,100000)}')
print(f'n=1000000 -> {montecarlo(g3,1000000)}')

# Ejercicio d
print('=== EJERCICIO D ===')
def g4(u):
    return 2*(np.exp(-((1/u)-1)**2)/u**2)

print(f'n=1000 -> {montecarlo(g4,1000)}')
print(f'n=10000 -> {montecarlo(g4,10000)}')
print(f'n=100000 -> {montecarlo(g4,100000)}')
print(f'n=1000000 -> {montecarlo(g4,1000000)}')
