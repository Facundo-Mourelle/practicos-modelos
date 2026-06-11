import numpy as np

# MONTECARLO


def f(x):
    return np.exp(-x) * (1 - x**4)


def simulacion_inciso_a():
    n = 100

    # Generar los primeros 100 valores
    U = np.random.uniform(2, 3, n)
    Y = f(U)

    # Inicialización estándar
    # Utilizamos formulas recursivas
    mean = np.mean(Y)
    S2 = np.var(Y, ddof=1)

    while True:
        S = np.sqrt(S2)
        semi_ancho = 1.96 * S / np.sqrt(n)

        if semi_ancho < 0.001:
            break

        # Generar un dato nuevo: X_{n+1}
        U = np.random.uniform(2, 3)
        X_n1 = f(U)

        # 1. Fórmula recursiva para la media: X(n+1)
        mean_next = mean + (X_n1 - mean) / (n + 1)

        # 2. Fórmula recursiva para la varianza: S^2(n+1)
        # Nota: La fórmula del apunte asume que estamos saltando al paso n+1
        S2_next = (1 - 1 / n) * S2 + (n + 1) * (mean_next - mean) ** 2

        # Actualizar valores para la próxima iteración
        mean = mean_next
        S2 = S2_next
        n += 1

    print("--- Inciso a ---")
    print(f"Simulaciones finales (N): {n}")
    print(f"Estimación (~I): {mean:.4f}")
    print(f"Desviación (S): {np.sqrt(S2):.4f}")
    print(f"Semi-ancho final: {1.96 * np.sqrt(S2) / np.sqrt(n):.5f}\n")


def simulacion_inciso_b(Ns_lista):
    print("--- Inciso b ---")
    print("Nºsim\t~I\t\tS\t\tIC(95%)")
    for Ns in Ns_lista:
        U = np.random.uniform(2, 3, Ns)
        Y = f(U)
        mean = np.mean(Y)
        S = np.std(Y, ddof=1)
        semi_ancho = 1.96 * S / np.sqrt(Ns)

        ic_inf = mean - semi_ancho
        ic_sup = mean + semi_ancho

        print(f"{Ns}\t{mean:.4f}\t\t{S:.4f}\t\t({ic_inf:.4f}, {ic_sup:.4f})")


# Ejecutar las funciones
simulacion_inciso_a()
simulacion_inciso_b([1000, 5000, 7000])
