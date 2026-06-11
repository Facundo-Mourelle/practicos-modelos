import numpy as np


# Datos del problema
datos = np.array(
    [1.6, 10.3, 3.5, 13.5, 18.4, 7.7, 24.3,
        10.7, 8.4, 4.9, 7.9, 12, 16.2, 6.8, 14.7]
)
n = len(datos)
datos_ordenados = np.sort(datos)
media_muestral = np.mean(datos)

# Función para calcular el estadístico D de K-S


def calcular_D(valores, media_est):
    n_en = len(valores)
    # CDF exponencial teórica con el parámetro estimado
    cdf_teorica = 1 - np.exp(-valores / media_est)
    i_n = np.arange(1, n_en + 1) / n_en
    i_minus_1_n = np.arange(0, n_en) / n_en

    d_mas = np.abs(cdf_teorica - i_n)
    d_menos = np.abs(cdf_teorica - i_minus_1_n)
    return max(np.max(d_mas), np.max(d_menos))


# 1. Calcular el D observado de nuestra muestra
D_observado = calcular_D(datos_ordenados, media_muestral)
print(f"Estadístico D observado: {D_observado:.4f}")

# 2. Simulación de Monte Carlo para obtener el p-valor correcto
np.random.seed(42)  # Semilla para reproducibilidad
replicas = 100000
contador_extremos = 0

for _ in range(replicas):
    # Generamos una muestra exponencial con cualquier media (ej. 1), ya que el test es invariante a la escala
    muestra_sim = np.random.exponential(scale=1.0, size=n)
    muestra_sim_ordenada = np.sort(muestra_sim)
    media_sim = np.mean(muestra_sim)

    # Calculamos el D simulado estimando la media de esa misma muestra
    D_sim = calcular_D(muestra_sim_ordenada, media_sim)

    if D_sim >= D_observado:
        contador_extremos += 1

p_valor = contador_extremos / replicas
print(f"p-valor aproximado por simulación: {p_valor:.4f}")
