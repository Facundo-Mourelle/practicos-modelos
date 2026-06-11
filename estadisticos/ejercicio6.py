import numpy as np
import scipy.stats as stats


# Datos del enunciado
observados = np.array([188, 138, 87, 65, 48, 32, 30, 34, 13, 2])
probabilidades = np.array(
    [0.31, 0.22, 0.12, 0.10, 0.08, 0.06, 0.04, 0.04, 0.02, 0.01])

N = np.sum(observados)  # 637
esperados = N * probabilidades

# --- d) Cálculo usando Chi-cuadrado ---
# Calculamos el estadístico T de forma manual para verificar
t_obs = np.sum((observados - esperados) ** 2 / esperados)

# Grados de libertad: k - 1 = 10 - 1 = 9
gl = len(observados) - 1
p_valor_chi2 = stats.chi2.sf(t_obs, df=gl)

print(f"Estadístico T observado: {t_obs:.4f}")
print(f"d) p-valor (Aproximación Chi-cuadrado): {p_valor_chi2:.4f}")


# --- e) Cálculo usando Simulación  ---
replicas = 100000
extremos = 0

# El espacio de eventos va del 0 al 9 (los 10 sectores)
sectores = np.arange(10)

for _ in range(replicas):
    # Simulamos 637 giros de la rueda bajo la hipótesis nula
    simulacion = np.random.choice(sectores, size=N, p=probabilidades)

    # Contamos las frecuencias de cada sector en la simulación
    obs_sim = np.bincount(simulacion, minlength=10)

    # Calculamos el estadístico T para esta muestra simulada
    t_sim = np.sum((obs_sim - esperados) ** 2 / esperados)

    # Si es igual o más extremo que el observado, sumamos uno
    if t_sim >= t_obs:
        extremos += 1

p_valor_sim = extremos / replicas
print(f"e) p-valor (Simulación Monte Carlo): {p_valor_sim:.4f}")
