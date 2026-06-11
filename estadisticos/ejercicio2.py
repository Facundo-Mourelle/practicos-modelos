import scipy.stats as stats
import numpy as np


def estadisticoT(frecuencias, probabilidades):
    t = 0
    K = len(frecuencias)
    n = sum(frecuencias)
    for k in range(K):
        t = t + (frecuencias[k] - n * probabilidades[k]
                 )**2 / (n * probabilidades[k])
    return t


probabilidades = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]
frecuencias = [158, 172, 164, 181, 160, 165]

print('Cantidad de datos: ', sum(frecuencias))

t0 = estadisticoT(frecuencias, probabilidades)
# df=5 porque tengo k-1 grados de libertad y k=6
print('p-valor: ', 1 - stats.chi2.cdf(t0, df=5))


def generar_numero_discreto(p, x):
    '''
    x: lista de valores posibles de la variable aleatoria
    p: lista de probabilidades asociadas a cada valor de x
    '''
    u = np.random.random()
    i = 0
    F = p
    while u >= F:
        i = i+1
        F = F + 1/6
    return x[i]


def frecuencias_generadas(n):
    freq = [0, 0, 0, 0, 0, 0]
    for k in range(n):
        x = generar_numero_discreto(1/6, [1, 2, 3, 4, 5, 6])
        freq[x-1] = freq[x-1] + 1
    return freq


def ejercicio_2b(frecuencias, probabilidades, NSim):
    pvalor = 0
    # cantidad de datos de mi muestra
    n = sum(frecuencias)
    t_obs = estadisticoT(frecuencias, probabilidades)
    for k in range(NSim):
        # frecuencias de las clases en mi muestra generada con distribución U{1,6}
        freq = frecuencias_generadas(n)
        # calculo el estadístico para la muestra generada
        t = estadisticoT(freq, probabilidades)
        if t_obs <= t:
            pvalor = pvalor + 1
    return pvalor/NSim


probabilidades = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]
frecuencias = [158, 172, 164, 181, 160, 165]
Nsim = 10000
t = ejercicio_2b(frecuencias, probabilidades, Nsim)

print('Ejercicio b:')
print('p-valor estimado: ', t)
