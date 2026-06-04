import numpy as np

def exponenciales():
    U1 = np.random.uniform()

    if U1 < 0.5:
        m = 3
    elif U1 < 0.8:
        m = 5
    else:
        m = 7

    # evitar problemas con ln(0)
    U2 = 1 - np.random.uniform()
    return (-m * np.log(U2))

n = 10000
resultados = [exponenciales() for _ in range(n)]
esperanza = np.mean(resultados)
print(f'{esperanza:.3f}')



