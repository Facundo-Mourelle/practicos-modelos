import numpy as np

# 1. Definición de los datos iniciales del enunciado
datos = np.array([56, 101, 78, 67, 93, 87, 64, 72, 80, 69])
n = len(datos)
a = -5
b = 5

# Calculamos la media muestral original (estimador de mu)
x_barra = np.mean(datos)

# 2. Configuración de la simulación de Monte Carlo
B = 100000          # Número de réplicas bootstrap

# 3. Generación de las muestras en forma matricial
# Se generan B muestras de tamaño n seleccionando elementos con reposición
muestras_boot = np.random.choice(datos, size=(B, n), replace=True)

# 4. Cálculo de las medias de cada una de las B muestras
# axis=1 calcula la media a lo largo de cada fila (cada réplica)
medias_boot = np.mean(muestras_boot, axis=1)

# 5. Evaluación de la condición: a < X*_barra - x_barra < b
diferencias = medias_boot - x_barra
exitos = (diferencias > a) & (diferencias < b)

# 6. Estimación de la probabilidad p
p_estimada = np.sum(exitos) / B

# Mostrar resultados
print(f"Media original (x_barra): {x_barra}")
print(f"Número de réplicas (B): {B}")
print(f"Probabilidad estimada p_hat: {p_estimada:.4f}")
