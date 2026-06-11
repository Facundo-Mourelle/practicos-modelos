import numpy as np

# BOOTSTRAP

# 1. Definición de los datos originales del enunciado
datos = np.array([2, 4, 6, 7, 11, 21, 81, 90, 105, 121])
n = len(datos)
B = 1000  # Número de réplicas de simulación especificadas


# Función auxiliar para calcular la media truncada al 10%
def calcular_media_truncada(muestra):
    # Ordenar la muestra de menor a mayor
    muestra_ordenada = np.sort(muestra)
    # Excluir el primer elemento [0] y el último [-1], tomando el promedio del resto
    return np.mean(muestra_ordenada[1:-1])


# 2. Configuración de la simulación
theta_boot = np.zeros(B)

# 3. Bucle de Simulación de Monte Carlo (Bootstrap)
for b in range(B):
    # Generar una muestra bootstrap con reemplazo del mismo tamaño 'n'
    muestra_b = np.random.choice(datos, size=n, replace=True)
    # Calcular el estadístico correspondiente y guardarlo
    theta_boot[b] = calcular_media_truncada(muestra_b)

# 4. Estimación de la varianza (usando ddof=1 para obtener el estimador muestral insesgado)
var_estimada = np.var(theta_boot, ddof=1)

# Mostrar resultados en consola
print(f"Media truncada original (theta_hat): {calcular_media_truncada(datos)}")
print(
    f"Estimación Bootstrap de Var(theta_hat) con {B} simulaciones: {var_estimada:.4f}"
)
