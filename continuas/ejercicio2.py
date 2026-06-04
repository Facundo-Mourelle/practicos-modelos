"""
Practico 5 - Ejercicio 2
Generacion de variables aleatorias continuas: Pareto, Erlang, Weibull.

Metodos:
  - Pareto y Weibull: transformada inversa (CDF cerrada).
  - Erlang: suma de k exponenciales independientes.
"""

import numpy as np
from math import gamma as gamma_func


def pareto(a: float, size: int = 1) -> np.ndarray:
    """Pareto(a) por transformada inversa: X = U^{-1/a}, U ~ U(0,1)."""
    u = np.random.uniform(0, 1, size=size)
    return u ** (-1.0 / a)


def erlang(mu: float, k: int, size: int = 1) -> np.ndarray:
    """Erlang(k, mu) como suma de k exponenciales(µ) independientes."""
    u = np.random.uniform(0, 1, size=(size, k))
    return -mu * np.log(np.prod(u, axis=1))


def weibull(lam: float, beta: float, size: int = 1) -> np.ndarray:
    """Weibull(lam, beta) por transformada inversa."""
    u = np.random.uniform(0, 1, size=size)
    return lam * (-np.log(1.0 - u)) ** (1.0 / beta)


if __name__ == "__main__":
    N = 10_000
    a, mu, k, lam_, beta = 2, 2, 2, 1, 2

    x_p = pareto(a, size=N)
    est_p = np.mean(x_p)
    teo_p = a / (a - 1)

    x_e = erlang(mu, k, size=N)
    est_e = np.mean(x_e)
    teo_e = k * mu

    x_w = weibull(lam_, beta, size=N)
    est_w = np.mean(x_w)
    teo_w = lam_ * gamma_func(1.0 + 1.0 / beta)

    print("=" * 65)
    print("Ejercicio 2 - Estimacion de medias (N = {})".format(N))
    print("=" * 65)
    print()
    print("i)  Pareto(a=2)")
    print(f"    Estimada: {est_p:.6f}   Teorica: {teo_p:.6f}   "
          f"Diff: {abs(est_p - teo_p):.6f}")
    print()
    print("ii) Erlang(k=2, mu=2)")
    print(f"    Estimada: {est_e:.6f}   Teorica: {teo_e:.6f}   "
          f"Diff: {abs(est_e - teo_e):.6f}")
    print()
    print("iii) Weibull(lambda=1, beta=2)")
    print(f"    Estimada: {est_w:.6f}   Teorica: {teo_w:.6f}   "
          f"Diff: {abs(est_w - teo_w):.6f}")
