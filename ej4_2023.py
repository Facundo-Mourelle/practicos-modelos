import numpy as np

# AREA FIGURA


def condicion_figura(x, y):
    # Evalúa la inecuación de la figura
    return (x**2 + y**2 - 1) ** 3 <= (x**2) * (y**3)


# ==========================================
# INCISO B: Proporción con 10.000 puntos
# ==========================================
N = 10000

# Generamos N variables aleatorias uniformes en el rango [-1.5, 1.5]
X = np.random.uniform(-1.5, 1.5, N)
Y = np.random.uniform(-1.5, 1.5, N)

# Contamos cuántos cumplen la condición
adentro_10k = condicion_figura(X, Y)
exitos_10k = np.sum(adentro_10k)
p_hat_10k = exitos_10k / N

print("--- INCISO B ---")
print(f"Puntos generados: {N}")
print(f"Proporción estimada (p_hat): {p_hat_10k:.4f}")

# ==========================================
# INCISO C: Intervalo de ancho < 0.1 y Área
# ==========================================
z = 1.96
n_sim = (
    100  # Empezamos con un lote inicial para evitar división por cero en la varianza
)
exitos = np.sum(
    condicion_figura(
        np.random.uniform(-1.5, 1.5, n_sim), np.random.uniform(-1.5, 1.5, n_sim)
    )
)

# Bucle while para detenerse cuando el ancho sea < 0.1
while True:
    p_hat = exitos / n_sim

    # Calculamos el ancho del intervalo (evitamos el caso p_hat = 0)
    if p_hat > 0 and p_hat < 1:
        ancho = 2 * z * np.sqrt((p_hat * (1 - p_hat)) / n_sim)
        if ancho < 0.1:
            break

    # Generamos un punto más
    x_new = np.random.uniform(-1.5, 1.5)
    y_new = np.random.uniform(-1.5, 1.5)
    if condicion_figura(x_new, y_new):
        exitos += 1

    n_sim += 1

# Cálculo final del área
area_cuadrado = 3 * 3
area_estimada = p_hat * area_cuadrado

print("\n--- INCISO C ---")
print(f"Simulaciones necesarias para ancho < 0.1: {n_sim}")
print(f"Ancho final del intervalo: {ancho:.5f}")
print(f"Proporción estimada final: {p_hat:.4f}")
print(f"Área estimada de la figura: {area_estimada:.4f} unidades cuadradas")
