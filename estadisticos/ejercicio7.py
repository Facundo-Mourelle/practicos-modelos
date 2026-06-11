import math
import random
import numpy as np

# Ajustar semilla para reproducibilidad (opcional)
random.seed(42)


def cdf_exponencial(x, media=1.0):
    """Función de distribución acumulada (CDF) teórica."""
    if x < 0:
        return 0.0
    return 1.0 - math.exp(-x / media)


def calcular_estadistico_d(datos):
    """Calcula el estadístico D de Kolmogorov-Smirnov para los datos dados."""
    n = len(datos)
    datos_ordenados = sorted(datos)
    max_d = 0.0

    for i in range(1, n + 1):
        x = datos_ordenados[i - 1]
        f_teorica = cdf_exponencial(x, media=1.0)

        # Diferencia con el escalón superior e inferior
        d_mas = (i / n) - f_teorica
        d_menos = f_teorica - ((i - 1) / n)

        max_d = max(max_d, d_mas, d_menos)

    return max_d


def generar_datos_exponenciales(n, media=1.0):
    """Genera n variables aleatorias exponenciales independientes."""
    # En Python, random.expovariate toma el parámetro lambda (1/media)
    lambd = 1.0 / media
    return [random.expovariate(lambd) for _ in range(n)]


np.random.uniform()

# --- PASO 1: Generar los 30 datos originales y calcular D_obs ---
n_muestra = 30
datos_originales = generar_datos_exponenciales(n_muestra, media=1.0)
d_observado = calcular_estadistico_d(datos_originales)

print(f"Estadístico D observado en la muestra: {d_observado:.4f}")

# --- PASO 2 y 3: Simulación de Monte Carlo para aproximar el p-valor ---
n_simulaciones = 10000
contador_extremos = 0

for _ in range(n_simulaciones):
    # Generamos una muestra bajo la hipótesis nula
    muestra_simulada = generar_datos_exponenciales(n_muestra, media=1.0)
    d_simulado = calcular_estadistico_d(muestra_simulada)

    # Contamos cuántas veces el estadístico simulado es tan extremo como el observado
    if d_simulado >= d_observado:
        contador_extremos += 1

p_valor_simulado = contador_extremos / n_simulaciones
print(f"P-valor aproximado por simulación: {p_valor_simulado:.4f}")
