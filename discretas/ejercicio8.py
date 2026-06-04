import math
import numpy as np

# Parámetros
lamda = 0.7
k = 10
repeticiones = 1000

# 1. Cálculo del valor exacto
def q(i, lam):
    return (lam**i * np.exp(-lam)) / math.factorial(i)

# Constante de normalización C = P(Y <= 10)
C = sum(q(j, lamda) for j in range(k + 1))

# P(X > 2) = P(X <= 2)
# P(X <= 2) = (q0 + q1 + q2) / C
p_le_2 = sum(q(j, lamda) for j in range(3)) / C
prob_exacta_mayor_2 = 1 - p_le_2

# 2. Simulación (Método de Rechazo simplificado)
def generar_poisson(lam):
    L = np.exp(-lam)
    p = 1.0
    i = 0
    while True:
        i += 1
        p *= np.random.uniform()
        if p <= L:
            return i - 1

def simular_truncada_rechazo():
    while True:
        Y = generar_poisson(lamda)
        if Y <= k:  # Condición de aceptación simplificada
            return Y

# Ejecutar simulación
exitos = 0
for _ in range(repeticiones):
    if simular_truncada_rechazo() > 2:
        exitos += 1

prob_estimada = exitos / repeticiones

print(f"P(X > 2) Exacta:    {prob_exacta_mayor_2:.5f}")
print(f"P(X > 2) Estimada:  {prob_estimada:.5f}")
