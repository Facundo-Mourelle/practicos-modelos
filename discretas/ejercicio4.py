import numpy as np
import time

# Probabilidades dadas
p = [0.11, 0.14, 0.09, 0.08, 0.12, 0.10, 0.09, 0.07, 0.11, 0.09]

# --- a) Rechazo c = 1.4 ---
def rechazo_minimo():
    c = 1.4
    while True:
        Y = int(np.random.uniform() * 10) + 1  # Uniforme en {1..10}
        U = np.random.uniform()
        if U < (p[Y-1] / (c * 0.1)):
            return Y

# --- b) Rechazo c = 3.0 ---
def rechazo_c3():
    c = 3.0
    while True:
        Y = int(np.random.uniform() * 10) + 1
        U = np.random.uniform()
        if U < (p[Y-1] / (c * 0.1)):
            return Y

# --- c) Transformada Inversa (Optimizada) ---
# Valores ordenados por probabilidad descendente
valores_ordenados = [2, 5, 1, 9, 6, 3, 7, 10, 4, 8]
prob_ordenadas = [0.14, 0.12, 0.11, 0.11, 0.10, 0.09, 0.09, 0.09, 0.08, 0.07]

def transformada_inversa():
    U = np.random.uniform()
    F = 0
    for i in range(10):
        F += prob_ordenadas[i]
        if U < F:
            return valores_ordenados[i]

# --- d) Método de la Urna ---
# Precomputar el arreglo
urna = []
for i, prob in enumerate(p):
    urna.extend([i + 1] * int(prob * 100))

def metodo_urna():
    index = int(np.random.uniform() * 100) # Uniforme en [0, 99]
    return urna[index]

# --- Simulaciones y Benchmarking ---
def comparar_eficiencia(N=10000):
    metodos = {
        "Rechazo (c=1.4)": rechazo_minimo,
        "Rechazo (c=3.0)": rechazo_c3,
        "Transformada Inversa": transformada_inversa,
        "Urna": metodo_urna
    }
    
    print(f"{'Método':<25} | {'Tiempo (s)':<12} | {'Velocidad Relativa'}")
    print("-" * 60)
    
    tiempos = {}
    for nombre, func in metodos.items():
        inicio = time.perf_counter()
        for _ in range(N):
            func()
        tiempos[nombre] = time.perf_counter() - inicio
        
    t_min = min(tiempos.values())
    
    for nombre, t in tiempos.items():
        print(f"{nombre:<25} | {t:<12.5f} | {t/t_min:.2f}x más lento")

comparar_eficiencia(10000)
