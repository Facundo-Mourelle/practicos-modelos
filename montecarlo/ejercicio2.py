import numpy as np

def simular_juego(iteraciones):
    """
    Simulación del Juego 1:
    - Si U < 1/2: X = W1 + W2
    - Si U >= 1/2: X = W1 + W2 + W3
    - Gana si X >= 1
    """
    aciertos = 0
    for _ in range(iteraciones):
        u = np.random.uniform()
        
        if u < (1/2):
            x = np.sum(np.random.uniform(0, 1, 2))
        else:
            x = np.sum(np.random.uniform(0, 1, 3))
        if x >= 1:
            aciertos+=1
    return aciertos / iteraciones

n = int(input("numero de iteraciones: "))
res = simular_juego(n)
print(f'{res}')
