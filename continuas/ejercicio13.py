import numpy as np

def simular_aficionados():
    # 1. Simular la cantidad de autobuses (N) en t = 1 hora con lambda = 5
    lamda = 5
    N = 0
    producto = 1 - np.random.uniform()
    cota = np.exp(-lamda)
    
    while producto >= cota:
        producto *= (1 - np.random.uniform())
        N += 1
        
    # 2. Si no llegó ningún autobús, no hay aficionados
    if N == 0:
        return 0
    
    # 3. Simular la capacidad de cada uno de los N autobuses y acumular
    total_aficionados = 0
    m = 20  # Capacidad mínima
    k = 40  # Capacidad máxima
    
    for _ in range(N):
        U = np.random.uniform()
        # Método de la transformada inversa para uniforme discreta [m, k]
        capacidad = int(U * (k - m + 1)) + m
        total_aficionados += capacidad
        
    return total_aficionados

# Ejemplo de ejecución para una simulación individual
resultado = simular_aficionados()
print(f"En el instante t = 1 hora, llegaron en total {resultado} aficionados.")
