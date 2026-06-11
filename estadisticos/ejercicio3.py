import numpy as np
import scipy.stats as stats


def calcular_estadistico_D(datos):
    datos_ordenados = sorted(datos)
    n = len(datos_ordenados)
    max_desvio = 0.0

    for i in range(1, n + 1):
        x = datos_ordenados[i-1]
        d_mas = (i / n) - x
        d_menos = x - ((i - 1) / n)

        if d_mas > max_desvio:
            max_desvio = d_mas
        if d_menos > max_desvio:
            max_desvio = d_menos

    return max_desvio


# Datos observados del enunciado
datos_reales = [0.12, 0.18, 0.06, 0.33, 0.72, 0.83, 0.36, 0.27, 0.77, 0.74]
D_observado = calcular_estadistico_D(datos_reales)


# Simulación de Monte Carlo
N_simulaciones = 100000
casos_extremos = 0

for _ in range(N_simulaciones):
    muestra_simulada = [np.random.uniform() for _ in range(len(datos_reales))]
    D_simulado = calcular_estadistico_D(muestra_simulada)

    if D_simulado >= D_observado:
        casos_extremos += 1

p_valor_aproximado = casos_extremos / N_simulaciones

print(f"Estadístico D observado: {D_observado}")
print(f"p-valor aproximado por simulación: {p_valor_aproximado:.4f}")


# USAR SOLO PARA CHEQUEAR
# Aplicamos el test de Kolmogorov-Smirnov contra la uniforme 'uniform' (0 a 1)
resultado = stats.kstest(datos_reales, 'uniform')
print(f"Estadístico D: {resultado.statistic:.4f}")
print(f"p-valor: {resultado.pvalue:.4f}")
