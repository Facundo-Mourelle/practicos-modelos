import numpy as np
import scipy.stats as stats
from statsmodels.stats.diagnostic import lilliefors

# 1. Datos del enunciado
datos = np.array([91.9, 97.8, 111.4, 122.3, 105.4, 95.0,
                 103.8, 99.6, 96.6, 119.3, 104.8, 101.7])

# 2. Estimación de parámetros
media = np.mean(datos)
desviacion = np.std(datos, ddof=1)  # ddof=1 para desviación muestral

print(f"Media estimada (mu): {media:.3f}")
print(f"Desviación estándar estimada (sigma): {desviacion:.3f}")
print("-" * 40)

# --- MÉTODO A: Prueba de Shapiro-Wilk (Ideal para n pequeños) ---
estadistico_sw, p_valor_sw = stats.shapiro(datos)
print("--- Prueba de Shapiro-Wilk ---")
print(f"Estadístico W: {estadistico_sw:.4f}")
print(f"p-valor: {p_valor_sw:.4f}")

# --- MÉTODO B: Prueba de Kolmogorov-Smirnov (Lilliefors) ---
# Usamos lilliefors de statsmodels ya que estimamos parámetros de la muestra
estadistico_ks, p_valor_ks = lilliefors(datos, dist='norm')
print("\n--- Prueba de Lilliefors (KS modificado) ---")
print(f"Estadístico D: {estadistico_ks:.4f}")
print(f"p-valor aproximado: {p_valor_ks:.4f}")
