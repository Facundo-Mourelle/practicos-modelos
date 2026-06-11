import numpy as np

# DENSIDAD

# Datos observados
datos = np.array(
    [0.590, 0.312, 0.665, 0.926, 0.577, 0.505, 0.615, 0.360, 0.899, 0.779, 0.293, 0.962]
)
datos_ordenados = np.sort(datos)
n = len(datos)

# 1. Calcular el D observado
i = np.arange(1, n + 1)
f_teorico = datos_ordenados**2
d_mas = i / n - f_teorico
d_menos = f_teorico - (i - 1) / n
d_obs = np.max(np.maximum(d_mas, d_menos))

# 2. Simulación de Monte Carlo (10,000 réplicas)
n_simulaciones = 10000
contador_extremos = 0

for _ in range(n_simulaciones):
    # Generar muestras de la hipótesis nula usando la transformada inversa: X = sqrt(U)
    u = np.random.uniform(0, 1, n)
    muestra_simulada = np.sort(np.sqrt(u))

    # Calcular el estadístico D para la muestra simulada
    f_sim_teorico = muestra_simulada**2
    d_mas_sim = i / n - f_sim_teorico
    d_menos_sim = f_sim_teorico - (i - 1) / n
    d_sim = np.max(np.maximum(d_mas_sim, d_menos_sim))

    if d_sim >= d_obs:
        contador_extremos += 1

# Calcular p-valor estimado
p_valor = contador_extremos / n_simulaciones
print(f"Estadístico D observado: {d_obs:.4f}")
print(f"P-valor estimado: {p_valor:.4f}")
