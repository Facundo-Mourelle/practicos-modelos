import numpy as np

def estimacion_randu(n_puntos=10000, M=2**31, a=(2**16 +3), seed=12345):
    # 1. Configuración de RANDU
    total_valores = n_puntos * 3
    v = np.zeros(total_valores)
    v[0] = seed  # Semilla impar obligatoria
    
    # 2. Generación de la secuencia (el "corazón" de RANDU)
    for i in range(1, total_valores):
        v[i] = (a * v[i-1]) % M
    
    # 3. Transformación a puntos 3D en el cubo [0, M)
    puntos = v.reshape(n_puntos, 3).astype(float)
    
    # 4. Cálculo de puntos dentro de la esfera
    centro = M / 2
    radio = M / 10

    dist_sq = np.sum((puntos - centro)**2, axis=1)
    dentro = np.sum(dist_sq <= radio**2)
    
    return (dentro / n_puntos) * 100

seed = 12345
n = 100000

# Caso 1
M = 2**31
a = 2**16 + 3
print(f"Resultado con RANDU: {estimacion_randu(n, M, a, seed):.4f}%")

# Caso 2
M = 2**31 - 1
a = 7**5
print(f"Resultado con RANDU ajustado: {estimacion_randu(n, M, a, seed):.4f}%")
