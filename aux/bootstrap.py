import numpy as np


# =====================================================================
# SECCIÓN A CAMBIAR: DATOS ORIGINALES Y CONFIGURACIÓN BOOTSTRAP
# =====================================================================
# Cambiar por los de tu examen
datos_originales = np.array([56, 101, 78, 67, 93, 85, 72, 67, 81, 70])
n = len(datos_originales)
B = 100000  # Número de réplicas bootstrap (usualmente 10.000 o 100.000)

# Calcular el parámetro de referencia con la muestra original
# Ejemplo: si el enunciado pide evaluar (X_barra - mu), mu se reemplaza por x_barra_original
media_original = np.mean(datos_originales)
# =====================================================================

# 1. Generar la matriz gigante Bootstrap (B filas, n columnas) con reemplazo
muestras_boot = np.random.choice(datos_originales, size=(B, n), replace=True)

# =====================================================================
# SECCIÓN A CAMBIAR: CALCULO DEL ESTIMADOR POR FILA
# =====================================================================
# Ejemplo A: Si te piden evaluar la Media Bootstrap en cada réplica
medias_boot = np.mean(muestras_boot, axis=1)

# Ejemplo B: Si te piden evaluar la Varianza Muestral Bootstrap (descomentar si se requiere)
# varianzas_boot = np.var(muestras_boot, axis=1, ddof=1)
# =====================================================================

# =====================================================================
# SECCIÓN A CAMBIAR: VARIABLE DE INTERÉS / INDICADORA
# =====================================================================
# Ejemplo: Estimar P( a < X_barra_boot - media_original < b )
a, b = -5, 5
exitos = (medias_boot - media_original >
          a) & (medias_boot - media_original < b)

# Calcular proporción final
probabilidad_estimada = np.sum(exitos) / B
print(f"Bootstrap - Probabilidad estimada: {probabilidad_estimada:.4f}")

# Si te pedían la varianza del estimador (Ej: Ejercicio 6):
# var_estimada = np.var(varianzas_boot, ddof=1)
# =====================================================================
