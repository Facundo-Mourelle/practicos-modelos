import random
import math
import time

N = 10000
M = 100

# Ejercicio b)

# Estimación Monte Carlo
inicio_mc = time.perf_counter()
suma_mc = 0
for _ in range(M):
    # Generación de uniforme discreta según el texto
    j = int(random.random() * N) + 1
    suma_mc += math.exp(j / N)

aproximacion_mc = (N / M) * suma_mc
fin_mc = time.perf_counter()

print(f"Aproximación Monte Carlo (M=100): {aproximacion_mc:.4f}")
print(f"Tiempo Monte Carlo: {fin_mc - inicio_mc:.8f} s")

# Ejercicio c)
# 1. Valor exacto (Suma de los 10000 términos)
inicio_exacto = time.perf_counter()
valor_exacto = sum(math.exp(k / N) for k in range(1, N + 1))
fin_exacto = time.perf_counter()

# 2. Suma de los primeros 100 términos (k=1 a 100)
suma_100_terminos = sum(math.exp(k / N) for k in range(1, 101))

print(f"Valor exacto (10000 términos): {valor_exacto:.4f}")
print(f"Suma primeros 100 términos: {suma_100_terminos:.4f}")
print(f"Tiempo Valor Exacto: {fin_exacto - inicio_exacto:.8f} s")
