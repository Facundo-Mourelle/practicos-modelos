import numpy as np

# Ejercicio 2
def varY():
    U = np.random.uniform()
    V = np.random.uniform()
    if U < 0.2:
        valores_impares = [1, 3, 5, 7, 9]
        return valores_impares[int(V * 5)]
    else:
        valores_pares = [2, 4, 6, 8, 10]
        return valores_pares[int(V * 5) ]

# Ejercicio 3
def f(x):
    return 0.5 * x**2 * np.exp(-x)

def fv(x):
    return (1/3) * np.exp(-x/3)

def rechazoX():
    c = 1.8270
    while True:
        u1 = np.random.uniform(0, 1)
        y = -3 * np.log(u1)
        u2 = np.random.uniform(0, 1)
        condition = f(y) / (c * fv(y))
        if u2 <= condition:
            return y

# Ejercicio 4
def jugador(p: float, lam: float) -> tuple[int, float]:
    N = 0
    T = 0.0
    while True:
        N += 1
        U = np.random.uniform()
        if U < p:
            break
        Xi = -np.log(np.random.uniform()) / lam
        T += Xi
    return (N, T)

if __name__ == "__main__":
    p = 0.4
    lam = 0.5
    n_sim = 10_000

    resultados = [jugador(p, lam) for _ in range(n_sim)]
    intentos = [r[0] for r in resultados]
    tiempos = [r[1] for r in resultados]

    tiempo_promedio = np.mean(tiempos)
    prob_tres_o_mas = np.mean([n >= 3 for n in intentos])

    print("=" * 55)
    print("Ejercicio 4")
    print(f"b) Tiempo promedio: {tiempo_promedio:.4f} minutos")
    print(f"c) P(N >= 3): {prob_tres_o_mas:.4f}")
    print("=" * 55)
