import numpy as np


# =====================================================================
# SECCIÓN A CAMBIAR: MUESTRA ORIGINAL Y CURVA ACUMULADA TEÓRICA (CDF)
# =====================================================================
datos = np.array([0.12, 0.18, 0.06, 0.33, 0.72, 0.83, 0.36, 0.27, 0.77, 0.74])
n = len(datos)


def cdf_teorica(x):
    # Ejemplo: Si H0 dice que son Uniformes(0,1), la CDF es F(x) = x
    return np.clip(x, 0, 1)
    # Si fuera Exponencial con media 1: return 1 - np.exp(-x)
# =====================================================================


def calcular_estadistico_d(muestra):
    X_ordenado = np.sort(muestra)
    d_mas = []
    d_menos = []
    for i in range(1, len(X_ordenado) + 1):
        fx = cdf_teorica(X_ordenado[i-1])
        d_mas.append((i / len(X_ordenado)) - fx)
        d_menos.append(fx - ((i - 1) / len(X_ordenado)))
    return max(max(d_mas), max(d_menos))


# 1. Calcular el D observado de tu examen
D_obs = calcular_estadistico_d(datos)

# 2. Simulación de Monte Carlo para obtener el p-valor exacto
REPLICAS_KS = 10000
casos_peores = 0

for _ in range(REPLICAS_KS):
    # Generar muestras directamente de la distribución de la Hipótesis Nula
    # Ejemplo: Si H0 es Uniforme(0,1) -> np.random.rand(n)
    # Ejemplo: Si H0 es Exponencial(media=1) -> np.random.exponential(scale=1.0, size=n)
    muestra_bajo_h0 = np.random.rand(n)

    D_sim = calcular_estadistico_d(muestra_bajo_h0)
    if D_sim >= D_obs:
        casos_peores += 1

p_valor_ks = casos_peores / REPLICAS_KS
print("Test Kolmogorov-Smirnov:")
print(f"Estadístico D observado: {D_obs:.4f}")
print(f"p-valor obtenido por simulación: {p_valor_ks:.4f}")
