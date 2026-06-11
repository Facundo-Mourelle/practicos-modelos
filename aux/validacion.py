import numpy as np
import scipy.stats as stats


# =====================================================================
# SECCIÓN A CAMBIAR: DATOS OBSERVADOS Y PROBABILIDADES TEÓRICAS
# =====================================================================
# Frecuencias del enunciado
frec_observadas = np.array([141, 291, 132])
prob_teoricas = np.array([0.25, 0.50, 0.25])        # Proporciones bajo H0
N_TOTAL = np.sum(frec_observadas)

# Si el enunciado estima parámetros desde los datos (ej: una binomial), restarlos en ddof
PARAMETROS_ESTIMADOS = 0
# =====================================================================

frec_esperadas = N_TOTAL * prob_teoricas

# 1. Cálculo Analítico del Estadístico T y p-valor
T_obs = np.sum((frec_observadas - frec_esperadas)**2 / frec_esperadas)
grados_libertad = len(frec_observadas) - 1 - PARAMETROS_ESTIMADOS
p_valor_analitico = stats.chi2.sf(T_obs, df=grados_libertad)

# 2. Aproximación por Simulación de Monte Carlo (Obligatorio si frec_esperadas < 5)
REPLICAS = 50000
contador_extremos = 0

for _ in range(REPLICAS):
    # Generar muestra simulada bajo H0 usando la distribución multinomial
    muestra_sim = np.random.multinomial(N_TOTAL, prob_teoricas)

    # Si reestimaras parámetros en cada iteración, recalculas frec_esperadas_sim aquí!
    T_sim = np.sum((muestra_sim - frec_esperadas)**2 / frec_esperadas)

    if T_sim >= T_obs:
        contador_extremos += 1

p_valor_simulado = contador_extremos / REPLICAS

print("Test Chi-cuadrada:")
print(f"Estadístico T observado: {T_obs:.4f}")
print(f"p-valor Analítico: {p_valor_analitico:.4f}")
print(f"p-valor Simulado: {p_valor_simulado:.4f}")
