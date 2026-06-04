import numpy as np

def aproximar_pi(n):
    # Generar N puntos aleatorios en el intervalo [-1, 1] para x e y
    puntos = np.random.uniform(-1, 1, (n, 2))

    # Calcular la distancia al cuadrado desde el origen (x^2 + y^2)
    # Sumamos los cuadrados de las columnas (axis=1)
    distancia_cuadrada = np.sum(puntos**2, axis=1)
    
    # Contar cuántos puntos cumplen x^2 + y^2 <= 1
    dentro_del_circulo = np.sum(distancia_cuadrada <= 1)
    
    # Calcular la aproximacion
    pi_aprox = 4 * dentro_del_circulo / n
    
    return pi_aprox

# Parámetros
N = 1_000_000
resultado = aproximar_pi(N)

print(f"Aproximación de π con N={N}: {resultado}")
print(f"Error absoluto: {abs(np.pi - resultado)}")
