import numpy as np

# Calcua el numero de eventos y sus tiempos de arribo en las primeras
# T unidades de tiempo de un proceso de Poisson homogeneo de parametro lamda
def eventosPoisson(lamda, T):
    t = 0
    NT = 0
    Eventos = []
    while t < T:
        U = 1 - np.random.uniform()
        t += -np.log(U)/lamda
        if t <= T:
            NT += 1
            Eventos.append(t)
    return NT, Eventos
