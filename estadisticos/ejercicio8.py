import math
import random


# 1. Generador de t-student provisto por el enunciado
def rt(df):
    # df: grados de libertad
    x = random.gauss(0.0, 1.0)
    y = 2.0 * random.gammavariate(0.5 * df, 2.0)
    return x / (math.sqrt(y / df))


# 2. Función de distribución acumulada (CDF) de la N(0,1) provista
def cdf_normal(x):
    return math.erf(x / math.sqrt(2.0)) / 2.0 + 0.5


# 3. Cálculo del estadístico D de Kolmogorov-Smirnov
def calcular_D(muestra):
    muestra_ordenada = sorted(muestra)
    n = len(muestra_ordenada)
    max_d = 0.0
    for i in range(n):
        x = muestra_ordenada[i]
        fx = cdf_normal(x)
        d_superior = ((i + 1) / n) - fx
        d_inferior = fx - (i / n)
        if d_superior > max_d:
            max_d = d_superior
        if d_inferior > max_d:
            max_d = d_inferior
    return max_d


# 4. Simulación para aproximar el p-valor bajo H0 (Datos puramente Normales)
def aproximar_p_valor(d_observado, n, replicas=10000):
    cont_extremos = 0
    for _ in range(replicas):
        # Bajo H0, los datos provienen de una N(0,1)
        muestra_h0 = [random.gauss(0.0, 1.0) for _ in range(n)]
        d_h0 = calcular_D(muestra_h0)
        if d_h0 >= d_observado:
            cont_extremos += 1
    return cont_extremos / replicas


# --- Experimento Principal ---
random.seed(42)  # Fijamos semilla para repetibilidad
tamanos_muestra = [10, 20, 100, 1000]
grados_libertad = 11

print(f"{'N (Tamaño)':<12} | {'Estadístico D':<15} | {'p-valor':<10}")
print("-" * 45)

for n in tamanos_muestra:
    # Generamos la muestra real del experimento (proviene de t-student)
    muestra_t = [rt(grados_libertad) for _ in range(n)]

    # Calculamos el estadístico D asumiendo erróneamente que es Normal
    d_obs = calcular_D(muestra_t)

    # Calculamos el p-valor por Monte Carlo
    p_val = aproximar_p_valor(d_obs, n, replicas=5000)

    print(f"{n:<12} | {d_obs:<15.5f} | {p_val:<10.4f}")
