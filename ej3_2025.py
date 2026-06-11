import numpy as np
from scipy import stats

# CHI CUADRADO, ESTIMAR PARAMETRO, P-VALOR

CARAS = np.array([0, 1, 2, 3, 4, 5])
FREC_OBS = np.array([38, 144, 342, 287, 164, 25])
N_EXPERIMENTOS = 1000
N_MONEDAS = 5


def estimar_p_binomial(caras, frecuencias, n_monedas):
    total_ensayos = np.sum(frecuencias) * n_monedas
    total_exitos = np.sum(caras * frecuencias)
    return total_exitos / total_ensayos


def calcular_probabilidades_binomial(n, p):
    k = np.arange(n + 1)
    return stats.binom.pmf(k, n, p)


def calcular_estadistico_chi2(frec_obs, frec_esp):
    return np.sum((frec_obs - frec_esp) ** 2 / frec_esp)


def inciso_a():
    print("INCISO A: Planteo de la prueba Chi-cuadrado")
    print("=" * 60)
    print()
    print("Procedimiento:")
    print("  1. Estimar p por máxima verosimilitud")
    print("  2. Calcular probabilidades esperadas bajo H0")
    print("  3. Calcular frecuencias esperadas: E_i = n * P(X=i)")
    print("  4. Estadístico: T = sum((O_i - E_i)^2 / E_i)")
    print("  5. Grados de libertad: k - 1 - m = 6 - 1 - 1 = 4")
    print("     donde k = número de categorías, m = parámetros estimados")
    print()


def inciso_b(caras, frec_obs, n_monedas, n_total):
    print("INCISO B: Cálculo del estadístico T")
    print("=" * 70)
    print()

    p_estimado = estimar_p_binomial(caras, frec_obs, n_monedas)
    print(f"p estimado por MV: {p_estimado:.6f}")

    prob_teoricas = calcular_probabilidades_binomial(n_monedas, p_estimado)
    frec_esp = n_total * prob_teoricas

    print("\nFrecuencias:")
    print(f"{'Caras':<10} {'Observadas':<15} {'Esperadas':<15} {'(O-E)^2/E':<15}")
    print("-" * 55)

    for i, k in enumerate(caras):
        contribucion = (frec_obs[i] - frec_esp[i]) ** 2 / frec_esp[i]
        print(
            f"{k:<10} {frec_obs[i]:<15.1f} {frec_esp[i]:<15.4f} {contribucion:<15.4f}"
        )

    T_obs = calcular_estadistico_chi2(frec_obs, frec_esp)
    print("-" * 55)
    print(f"{'TOTAL T':<40} {T_obs:<15.4f}")

    grados_libertad = len(caras) - 1 - 1
    p_valor_analitico = stats.chi2.sf(T_obs, df=grados_libertad)

    print(f"\nGrados de libertad: {grados_libertad}")
    print(f"p-valor analítico (scipy): {p_valor_analitico:.6f}")

    return T_obs, p_estimado


def inciso_c(caras, frec_obs, n_monedas, n_total, p_estimado, T_obs, N_sim=1000):
    print("\n" + "=" * 70)
    print("INCISO C: Simulación para p-valor (1000 réplicas)")
    print("=" * 70)
    print()
    print("Procedimiento de simulación:")
    print("  1. Generar muestra de tamaño 1000 de Binomial(5, p_estimado)")
    print("  2. Reestimar p desde la muestra simulada")
    print("  3. Calcular T_sim para esa muestra")
    print("  4. Repetir 1000 veces")
    print("  5. p-valor = proporción de T_sim >= T_obs")
    print()

    contador_extremos = 0

    for _ in range(N_sim):
        muestra_sim = np.random.binomial(n_monedas, p_estimado, n_total)

        frec_sim = np.array([np.sum(muestra_sim == k) for k in caras])

        p_sim = estimar_p_binomial(caras, frec_sim, n_monedas)

        prob_sim = calcular_probabilidades_binomial(n_monedas, p_sim)
        frec_esp_sim = n_total * prob_sim

        T_sim = calcular_estadistico_chi2(frec_sim, frec_esp_sim)

        if T_sim >= T_obs:
            contador_extremos += 1

    p_valor_sim = contador_extremos / N_sim

    print(f"Simulaciones realizadas: {N_sim}")
    print(f"Casos con T_sim >= T_obs: {contador_extremos}")
    print(f"p-valor simulado: {p_valor_sim:.6f}")

    return p_valor_sim


def inciso_d(T_obs, p_valor, alpha=0.05):
    print("\n" + "=" * 70)
    print("INCISO D: Decisión con alpha = 5%")
    print("=" * 70)
    print()

    grados_libertad = len(CARAS) - 1 - 1
    valor_critico = stats.chi2.ppf(1 - alpha, df=grados_libertad)

    print(f"Nivel de significancia: {alpha}")
    print(f"Estadístico T observado: {T_obs:.4f}")
    print(f"Valor crítico chi2(4, 0.95): {valor_critico:.4f}")
    print(f"p-valor: {p_valor:.6f}")
    print()

    if T_obs > valor_critico:
        print("DECISIÓN: Se RECHAZA H0 (T_obs > valor crítico)")
        decision = "RECHAZO"
    else:
        print("DECISIÓN: NO se rechaza H0 (T_obs <= valor crítico)")
        decision = "NO RECHAZO"

    print()
    print("Interpretación:")
    if decision == "RECHAZO":
        print("  Los datos NO son consistentes con una distribución Binomial(5, p)")
        print("  con p estimado desde los datos.")
    else:
        print("  No hay evidencia suficiente para rechazar que los datos")
        print("  provengan de una distribución Binomial(5, p).")

    return decision


def main():
    print("\n" + "=" * 70)
    print("EJERCICIO 3: Test Chi-cuadrado - Bondad de ajuste Binomial")
    print("=" * 70)
    print()

    print(f"Datos:")
    print(f"  Monedas: {N_MONEDAS}")
    print(f"  Experimentos: {N_EXPERIMENTOS}")
    print(f"  Caras: {CARAS}")
    print(f"  Frecuencias: {FREC_OBS}")
    print()

    inciso_a()

    T_obs, p_estimado = inciso_b(CARAS, FREC_OBS, N_MONEDAS, N_EXPERIMENTOS)

    p_valor_sim = inciso_c(
        CARAS, FREC_OBS, N_MONEDAS, N_EXPERIMENTOS, p_estimado, T_obs, N_sim=1000
    )

    inciso_d(T_obs, p_valor_sim, alpha=0.05)

    print("\n" + "=" * 70)
    print("RESUMEN")
    print("=" * 70)
    print(f"p estimado: {p_estimado:.4f}")
    print(f"T observado: {T_obs:.4f}")
    print(f"p-valor simulado: {p_valor_sim:.4f}")


if __name__ == "__main__":
    main()
