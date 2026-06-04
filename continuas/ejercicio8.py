import numpy as np

def simulacion_suma(n):
    muestras = []
    rngs_usados = 0
    for _ in range(n):
        muestras.append(np.random.uniform() + np.random.uniform())
        rngs_usados += 2
    return muestras, rngs_usados

def simulacion_transformada(n):
    muestras = []
    rngs_usados = 0
    for _ in range(n):
        u = np.random.uniform()
        rngs_usados += 1
        if u <= 0.5:
            muestras.append(np.sqrt(2 * u))
        else:
            muestras.append(2 - np.sqrt(2 * (1 - u)))
    return muestras, rngs_usados

def simulacion_rechazo(n):
    muestras = []
    rngs_usados = 0
    while len(muestras) < n:
        rngs_usados += 2
        y = 2 * np.random.uniform()  # U(0,2)
        u2 = np.random.uniform()
        
        # f(y) condicional
        fy = y if y <= 1 else (2 - y)
        
        if u2 <= fy:
            muestras.append(y)
    return muestras, rngs_usados

# --- Ejecución ---
N = 10000
x0 = 1.5

m_suma, rng_suma = simulacion_suma(N)
m_trans, rng_trans = simulacion_transformada(N)
m_rech, rng_rech = simulacion_rechazo(N)

# --- Estadísticos ---
print("--- Comparación de Eficiencia y Valor Esperado ---")
print(f"{'Método':<15} | {'E[X] (Empírico)':<15} | {'RNGs Totales':<12}")
print("-" * 50)
print(f"{'Suma de U':<15} | {sum(m_suma)/N:<15.4f} | {rng_suma:<12}")
print(f"{'Transformada':<15} | {sum(m_trans)/N:<15.4f} | {rng_trans:<12}")
print(f"{'Acept/Rechazo':<15} | {sum(m_rech)/N:<15.4f} | {rng_rech:<12}")
print("\nValor esperado teórico: 1.0000")
print("RNG Esperado Acept/Rechazo Teórico: 40000 (c=2 * 2 variables * 10000)")

# --- Comprobación de probabilidad empírica (Punto d) ---
prop_suma = sum(1 for x in m_suma if x > x0) / N
prop_trans = sum(1 for x in m_trans if x > x0) / N
prop_rech = sum(1 for x in m_rech if x > x0) / N

print("\n--- Comparación P(X > 1.5) empírica vs teórica ---")
print(f"P(X > 1.5) Teórica          : 0.1250")
print(f"P(X > 1.5) Suma Uniformes   : {prop_suma:.4f}")
print(f"P(X > 1.5) Transformada     : {prop_trans:.4f}")
print(f"P(X > 1.5) Acept/Rechazo    : {prop_rech:.4f}")
