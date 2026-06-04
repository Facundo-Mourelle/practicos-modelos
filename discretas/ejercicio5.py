import numpy as np
import time
from collections import Counter
import math

# --- I) Método Transformada Inversa ---
def binomial_inversa(n, p):
    c = p / (1 - p)
    prob = (1 - p)**n
    F = prob
    i = 0
    U = np.random.uniform()
    while U >= F: # Acumulación recursiva de probabilidades
        prob *= c * (n - i) / (i + 1)
        F += prob
        i += 1
    return i

# --- II) Método de Ensayos Bernoulli ---
def binomial_ensayos(n, p):
    exitos = 0
    for _ in range(n):
        if np.random.uniform() < p: # Simulación de éxito/fracaso
            exitos += 1
    return exitos

# --- Parámetros del Ejercicio ---
n = 10
p = 0.3
simulaciones = 10000

def ejecutar_analisis():
    # a) Comparación de Eficiencia
    # 1. Inversa
    inicio_inv = time.perf_counter()
    resultados_inv = [binomial_inversa(n, p) for _ in range(simulaciones)]
    tiempo_inv = time.perf_counter() - inicio_inv

    # 2. Ensayos
    inicio_ens = time.perf_counter()
    resultados_ens = [binomial_ensayos(n, p) for _ in range(simulaciones)]
    tiempo_ens = time.perf_counter() - inicio_ens

    # b) Estimación de valores (usando los resultados de la Transformada Inversa)
    conteo_inv = Counter(resultados_inv)
    valor_mas_frecuente_inv = conteo_inv.most_common(1)[0][0]
    prop_0_inv = conteo_inv.get(0, 0) / simulaciones
    prop_10_inv = conteo_inv.get(10, 0) / simulaciones

    conteo_ens = Counter(resultados_ens)
    valor_mas_frecuente_ens = conteo_ens.most_common(1)[0][0]
    prop_0_ens = conteo_ens.get(0, 0) / simulaciones
    prop_10_ens = conteo_ens.get(10, 0) / simulaciones

    # c) Probabilidades Teóricas
    prob_teorica_0 = (1 - p)**n
    prob_teorica_10 = p**n
    
    print(f"--- a) Eficiencia (10,000 simulaciones) ---")
    print(f"Tiempo Transformada Inversa: {tiempo_inv * 1000:.5f} ms")
    print(f"Tiempo Ensayos Bernoulli:    {tiempo_ens * 1000:.5f} ms")
    
    print(f"\n--- b) y c) Estimaciones vs Teórico ---")
    print(f"Valor con mayor ocurrencia (Inversa): {valor_mas_frecuente_inv}")
    print(f"Valor con mayor ocurrencia (Ensayos): {valor_mas_frecuente_ens}")
    print(f"Moda Teórica: {math.floor((n+1)*p)}")
    print(" Proporciones ")
    print(" --- Prop. inversa --- ")
    print(f"P(X=0):  {prop_0_inv:.6f} | P(X=10): {prop_10_inv:.6f}")
    print(" --- Prop. ensayos --- ")
    print(f"P(X=0):  {prop_0_ens:.6f} | P(X=10): {prop_10_ens:.6f}")
    print(f" --- Prop. Teórica --- ")
    print(f"Prop. Teórica P(X=0): {prob_teorica_0:.6f} | P(X=10): {prob_teorica_10:.6f}")

ejecutar_analisis()
