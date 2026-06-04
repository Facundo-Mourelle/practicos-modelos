import numpy as np


def gen_X_and_get_mean(n: int = 1000) -> float:
    if n <= 0:
        raise ValueError("n debe ser un entero positivo")

    # 1. Generar Y ~ Exp(1) (rate = 1, scale = 1)
    U1 = np.random.uniform(size=n)
    Y = -np.log(U1)

    # 2. Generar U ~ Uniform(0,1)
    U = np.random.uniform(size=n)

    # 3. Transformada inversa de la CDF condicional: X = U^(1/Y)
    X = U ** (1.0 / Y)

    return float(np.mean(X))


if __name__ == "__main__":
    N = 10_000
    media_est = gen_X_and_get_mean(N)
    # Esperanza teorica: E[X] = 1 - e * E_1(1)
    # donde E_1(1) = integral_1^infty e^{-t}/t dt (exponential integral)
    # Aproximacion numerica de E_1(1):
    t = np.linspace(1.0, 100.0, 100_000)
    dt = t[1] - t[0]
    e1_1 = np.sum(np.exp(-t) / t) * dt
    media_teo = 1.0 - np.e * e1_1

    print("=" * 55)
    print("Ejercicio 4 - Estimacion de media (N = {})".format(N))
    print("=" * 55)
    print(f"  Media estimada:  {media_est:.6f}")
    print(f"  Media teorica:   {media_teo:.6f}")
    print(f"  Diferencia:      {abs(media_est - media_teo):.6f}")
