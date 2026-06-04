import numpy as np

# ===============================================
# Ejercicio 1
# ===============================================
def ejercicio1():
    """
    Genera un valor de la variable aleatoria X utilizando 
    el método de aceptación y rechazo.
    """
    while True:
        y = np.random.uniform()
        u = np.random.uniform()
        
        # Condición de aceptación simplificada: f(y) / (c * g(y))
        prob_aceptacion = 16 * (y**2 - 2*y**3 + y**4)
        
        if u <= prob_aceptacion:
            return y

def estimar_esperanza_1(n_simulaciones):
    suma_x = 0
    for _ in range(n_simulaciones):
        suma_x += ejercicio1()
    
    return suma_x / n_simulaciones

# ===============================================
# Ejercicio 2
# ===============================================
def codigoX(p):
    """
    Genera un valor de la variable aleatoria X utilizando 
    el método de la transformada inversa y recursión.
    """
    u = np.random.uniform()
    # Valores iniciales para i = 10
    i = 10
    prob_i = p
    F = prob_i
    # Bucle de búsqueda del inverso de la FDA
    while u > F:
        prob_i *= (1 - p)  # Fórmula recursiva del inciso a)
        F += prob_i        # Acumulación de la probabilidad
        i += 1
    return i


def estimar_esperanza_2(n, p):
    suma_x = 0
    for _ in range(n):
        suma_x += codigoX(p)

    return  suma_x / n

# ===============================================
# Ejercicio 3
# ===============================================

if __name__ == "__main__":
    n = 10000
    esperanza_estimada = estimar_esperanza_1(n)
    print(40*'=')
    print('Ejercicio 1')
    print(f"Esperanza estimada con {n} simulaciones: {esperanza_estimada:.4f}")
    print(40*'=')

    p = 0.5
    esperanza_estimada = estimar_esperanza_2(n, p)
    print(40*'=')
    print('Ejercicio 2')
    print(40*'=')
    print(f"Parámetro p: {p}")
    print(f"Esperanza estimada E[X]: {estimar_esperanza_2(10000, p):.4f}")
    print(f"Esperanza estimada con {n} simulaciones: {esperanza_estimada:.4f}")
    print(40*'=')

