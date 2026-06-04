# Ejercicio 2
# U,V ~ U(0,1)
# Si U > 0.5 y V < 0.5 -> A
# Si U < 0.5 y V > 0.5 -> B
#           c.c        -> volver a tirar

# calcular P(A gane el juego en 1º o 2º jugada)

import numpy as np

def simular_juego(ensayos):
    u = np.random.uniform(0, 1, ensayos)
    v = np.random.uniform(0, 1, ensayos)

    gana_A = (u > 0.5) & (v < 0.5)
    gana_B = (u < 0.5) & (v > 0.5)
    empate_r1 = ~(gana_A | gana_B)

    total_empates = np.sum(empate_r1)

    u2 = np.random.uniform(0, 1, total_empates)
    v2 = np.random.uniform(0, 1, total_empates)
    gana_A_r2 = (u2 > 0.5) & (v2 < 0.5)

    total_exitos = np.sum(gana_A) + np.sum(gana_A_r2)

    return total_exitos / ensayos

n = int(input("numero de iteraciones: "))
res = simular_juego(n)
print(f'{res}')

