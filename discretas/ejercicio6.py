import random
import time
import math

# Probabilidades P(X=i)
p = [0.15, 0.20, 0.10, 0.35, 0.20]

# --- I) Transformada Inversa Optimizada ---
def simular_inversa():
    U = random.random()
    if U < 0.35: return 3
    elif U < 0.55: return 1
    elif U < 0.75: return 4
    elif U < 0.90: return 0
    else: return 2

# --- II) Aceptación y Rechazo ---

# Precomputar probabilidades de B(4, 0.45) y la constante c
q = [math.comb(4, i) * (0.45**i) * (0.55**(4-i)) for i in range(5)]
c = max(p[i] / q[i] for i in range(5))

def simular_y_binomial():
    # Genera B(4, 0.45) por ensayos de Bernoulli
    return sum(1 for _ in range(4) if random.random() < 0.45)

def simular_rechazo():
    while True:
        Y = simular_y_binomial()
        U = random.random()
        # Condición: U < p(Y) / (c * q(Y))[cite: 1]
        if U < (p[Y] / (c * q[Y])):
            return Y

# --- Simulación y Análisis ---
def comparar_eficiencia(simulaciones=10000):
    inicio_inv = time.perf_counter()
    for _ in range(simulaciones):
        simular_inversa()
    t_inv = time.perf_counter() - inicio_inv

    inicio_rech = time.perf_counter()
    for _ in range(simulaciones):
        simular_rechazo()
    t_rech = time.perf_counter() - inicio_rech
    
    print(f"Constante 'c' del método de rechazo: {c:.4f}")
    print(f"--- Tiempos ({simulaciones} iteraciones) ---")
    print(f"Transformada Inversa: {t_inv:.5f} s")
    print(f"Aceptación y Rechazo: {t_rech:.5f} s")
    print(f"Relación: Rechazo es {t_rech/t_inv:.2f}x más lento.")

comparar_eficiencia()
