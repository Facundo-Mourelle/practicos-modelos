import numpy as np

# =====================================================================
# SECCIÓN A CAMBIAR: FUNCIÓN A INTEGRAR Y LÍMITES
# =====================================================================
# Enunciado Ejemplo: Integral de 0 a 1 de e^x * sqrt(2x)


def g(x):
    return np.exp(x) * np.sqrt(2 * x)


# Límites de integración. Si es de 0 a inf, hacer cambio de variable u = 1/(x+1)
A, B = 0, 1
# =====================================================================

# Inicializaciones obligatorias para controlar la condición de parada
suma_g = 0
suma_g_cuad = 0
n = 0

# Condición de parada mínima (ej: mínimo 100 muestras)
MIN_MUESTRAS = 100
error_estandar = float('inf')

# =====================================================================
# SECCIÓN A CAMBIAR: CRITERIO DE PARADA (Según enunciado)
# =====================================================================
# Cambiar el valor (0.01) o cambiar la condición si pide "semiancho del IC < valor"
while n < MIN_MUESTRAS or error_estandar >= 0.01:
    # 1. Generar variable uniforme en el intervalo (A, B)
    u = np.random.uniform(A, B)

    # 2. Evaluar la función
    val = g(u)

    # 3. Acumular estadísticos
    suma_g += val
    suma_g_cuad += val**2
    n += 1

    # 4. Calcular desviación estándar del estimador (Error estándar)
    if n >= 2:
        media_muestral = suma_g / n
        varianza_muestral = (suma_g_cuad - n * (media_muestral**2)) / (n - 1)
        # Ojo: la desviación estándar del estimador de la integral es S / sqrt(n) * longitud_intervalo
        error_estandar = (np.sqrt(varianza_muestral) / np.sqrt(n)) * (B - A)

# 5. Resultado final del estimador de Monte Carlo
integral_estimada = (suma_g / n) * (B - A)

print("Resultados Monte Carlo Integrales:")
print(f"Muestras simuladas (n): {n}")
print(f"Valor estimado: {integral_estimada:.5f}")
