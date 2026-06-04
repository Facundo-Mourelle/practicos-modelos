import time
import numpy as np

# --- 1. Método Común ---
def poisson_comun(lamda):
    U = np.random.uniform()
    i = 0
    p = np.exp(-lamda)
    F = p
    while U >= F:
        i += 1
        p *= lamda / i
        F += p
    return i

# --- 2. Método Mejorado ---
def poisson_mejorado(lamda):
    p = np.exp(-lamda)
    F = p
    # Acumulamos las probabilidades hasta I = int(lamda)
    I = int(lamda)
    for j in range(1, I + 1):
        p *= lamda / j
        F += p

    U = np.random.uniform()
    if U >= F:
        j = I + 1
        while U >= F:
            p *= lamda / j
            F += p
            j += 1
        return j - 1
    else:
        j = I
        while U < F:
            F -= p
            p *= j / lamda  # Relación inversa para retroceder
            j -= 1
        return j + 1


def ejecutar_simulacion(lamda=10, repeticiones=1000):
    inicio_comun = time.perf_counter()
    resultados_comun = [poisson_comun(lamda) for _ in range(repeticiones)]
    tiempo_comun = time.perf_counter() - inicio_comun
    prob_comun = sum(1 for y in resultados_comun if y > 2) / repeticiones

    inicio_mejor = time.perf_counter()
    resultados_mejorado = [poisson_mejorado(lamda) for _ in range(repeticiones)]
    tiempo_mejorado = time.perf_counter() - inicio_mejor
    prob_mejor = sum(1 for y in resultados_mejorado if y > 2) / repeticiones
    
    print(f"--- Resultados para {repeticiones} repeticiones (λ={lamda}) ---")
    print(f"P(Y > 2) Teórica: ~0.9972")
    print(f"P(Y > 2) Común:   {prob_comun:.4f} (Tiempo: {tiempo_comun:.5f}s)")
    print(f"P(Y > 2) Mejorado:{prob_mejor:.4f} (Tiempo: {tiempo_mejorado:.5f}s)")

ejecutar_simulacion()
