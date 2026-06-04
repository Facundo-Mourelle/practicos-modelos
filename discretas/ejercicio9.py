import time
import numpy as np

# --- a) Transformada Inversa Recursiva ---
def geom_inversa(p):
    U = np.random.uniform()
    q = 1 - p
    prob = p
    F = prob
    i = 1
    while U >= F:
        prob *= q       # Fórmula recursiva: p_{i+1} = p_i * q
        F += prob
        i += 1
    return i

# --- b) Simulación de Ensayos Bernoulli ---
def geom_ensayos(p):
    i = 1
    # Mientras el ensayo sea un fracaso (U >= p), seguimos intentando
    while np.random.uniform() >= p: 
        i += 1
    return i

# --- Simulación y Comparación ---
def comparar_geometrica(p, simulaciones=10000):
    esperanza_teorica = 1 / p

    # 1. Inversa
    inicio_inv = time.perf_counter()
    resultados_inv = [geom_inversa(p) for _ in range(simulaciones)]
    tiempo_inv = time.perf_counter() - inicio_inv
    promedio_inv = np.mean(resultados_inv)

    # 2. Ensayos
    inicio_ens = time.perf_counter()
    resultados_ens = [geom_ensayos(p) for _ in range(simulaciones)]
    tiempo_ens = time.perf_counter() - inicio_ens
    promedio_ens = np.mean(resultados_ens)

    print(f"--- Resultados para p = {p} ({simulaciones} simulaciones) ---")
    print(f"E(X) Teórico: {esperanza_teorica:.2f}")
    print(f"Promedio Inversa: {promedio_inv:.4f} (Error: {abs(promedio_inv - esperanza_teorica):.4f})")
    print(f"Promedio Ensayos: {promedio_ens:.4f} (Error: {abs(promedio_ens - esperanza_teorica):.4f})")
    print(f"Tiempo Inversa:   {tiempo_inv:.5f} s")
    print(f"Tiempo Ensayos:   {tiempo_ens:.5f} s")
    print("-" * 50)

comparar_geometrica(0.8)
comparar_geometrica(0.2)
