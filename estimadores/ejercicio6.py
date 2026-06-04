import numpy as np

print("--- PARTE A ---")
datos_a = np.array([1, 3])
B_a = 50000  # Número de réplicas bootstrap

# Generamos una matriz donde cada fila es una muestra bootstrap de tamaño n=2 con reemplazo
muestras_a = np.random.choice(datos_a, size=(B_a, len(datos_a)), replace=True)

# Calculamos la varianza muestral S^*^2 de cada réplica (ddof=1 asegura dividir por n-1)
varianzas_a = np.var(muestras_a, axis=1, ddof=1)

# La estimación bootstrap de Var(S^2) es la varianza de los resultados obtenidos
var_bootstrap_a = np.var(varianzas_a, ddof=1)
print(f"Estimación bootstrap de Var(S^2) para n=2: {var_bootstrap_a:.4f}")


# =============================================================================
# PARTE b) n = 15, datos del enunciado
# =============================================================================
print("\n--- PARTE B ---")
datos_b = np.array([5, 4, 9, 6, 21, 17, 11, 20, 7, 10, 21, 15, 13, 16, 8])
B_b = 100000  # Usamos más réplicas para mayor precisión en Monte Carlo

# Generamos una matriz de B_b filas y n=15 columnas muestreando con reemplazo
muestras_b = np.random.choice(datos_b, size=(B_b, len(datos_b)), replace=True)

# Calculamos S^*^2 para cada una de las muestras a lo largo del eje horizontal
varianzas_b = np.var(muestras_b, axis=1, ddof=1)

# La estimación de Monte Carlo es la varianza de las varianzas obtenidas
var_bootstrap_b = np.var(varianzas_b, ddof=1)
print(f"Estimación bootstrap de Var(S^2) para n=15: {var_bootstrap_b:.4f}")
