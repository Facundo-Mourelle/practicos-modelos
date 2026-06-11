import numpy as np
from scipy import stats

# ESTADISTICO, KS

DATOS = np.array(
    [
        15.22860536,
        16.2321714,
        10.1119561,
        36.72299321,
        17.49593589,
        8.46376635,
        9.79485269,
        1.53479053,
        27.59551348,
        7.82520791,
        40.60145536,
        25.02174735,
        49.10266584,
        50.67085322,
        2.70768636,
        9.18330789,
        10.40308179,
        34.74136011,
        6.82283137,
        3.17626161,
        33.67482894,
        30.34655637,
        3.6536329,
        3.25476304,
        14.77332745,
        9.97428217,
        1.57849658,
        27.47600572,
        12.45162807,
        46.91791271,
        44.03841737,
        3.3181228,
        35.82047148,
        20.12426236,
        1.72267967,
        2.33951729,
        6.26959703,
        9.1075566,
        28.01983651,
        38.08371186,
        15.69560109,
        5.69447539,
        3.37816632,
        20.2668814,
        23.34685662,
        137.51657441,
        4.74251574,
        1.88056595,
        0.36890593,
        41.10961135,
    ]
)

LAMDA = 0.05
n = len(DATOS)


def generar_exponencial(lamda):
    u = np.random.uniform()
    return -np.log(u) / lamda


def cdf_teorica(x, lamda):
    return 1 - np.exp(-lamda * x)


def calcular_estadistico_ks(datos, lamda):
    datos_sorted = np.sort(datos)

    d_mas = []
    d_menos = []
    for i in range(1, len(datos_sorted) + 1):
        fx = cdf_teorica(datos_sorted[i - 1], lamda)
        d_mas.append((i / len(datos_sorted)) - fx)
        d_menos.append(fx - ((i - 1) / len(datos_sorted)))
    return max(max(d_mas), max(d_menos))


def inciso_a_b(datos, lamda):
    print("INCISO B: Cálculo del estadístico")
    print("=" * 60)

    D_stat, D_mas, D_menos = calcular_estadistico_ks(datos, lamda)

    print(f"n = {n}")
    print(f"lambda = {lamda}")
    print(f"D+ = max(i/n - F_0(x_i)) = {D_mas:.6f}")
    print(f"D- = max(F_0(x_i) - (i-1)/n) = {D_menos:.6f}")
    print(f"\nEstadístico D observado = {D_stat:.6f}")

    return D_stat


def simular_ks_uniformes(n, lamda, N_sim=100000):
    D_sim = np.zeros(N_sim)

    for i in range(N_sim):
        U = np.random.uniform(0, 1, n)
        muestra = -np.log(U) / lamda
        D_sim_i, _, _ = calcular_estadistico_ks(muestra, lamda)
        D_sim[i] = D_sim_i

    return D_sim


def simular_ks_exponencial(n, lamda, N_sim=100000):
    D_sim = np.zeros(N_sim)

    for i in range(N_sim):
        muestra = generar_exponencial(lamda)
        D_sim_i, _, _ = calcular_estadistico_ks(muestra, lamda)
        D_sim[i] = D_sim_i

    return D_sim


def inciso_c(datos, lamda, D_stat):
    print("\n" + "=" * 60)
    print("INCISO C: Simulación con uniformes, alpha = 0.04")
    print("=" * 60)

    n = len(datos)
    N_sim = 100000

    print(f"Generando {N_sim} muestras Exp({lamda}) usando uniformes...")
    D_sim = simular_ks_uniformes(n, lamda, N_sim)

    D_crit_sim_04 = np.percentile(D_sim, 96)
    p_value_04 = np.mean(D_sim >= D_stat)

    print(f"\nValor crítico simulado (percentil 96): {D_crit_sim_04:.6f}")
    print(f"p-value simulado: {p_value_04:.6f}")
    print(f"D observado: {D_stat:.6f}")

    if D_stat > D_crit_sim_04:
        print(f"\nDECISIÓN: Se RECHAZA H0 (D > {D_crit_sim_04:.6f})")
        resultado = "RECHAZO"
    else:
        print(f"\nDECISIÓN: NO se rechaza H0 (D <= {D_crit_sim_04:.6f})")
        resultado = "NO RECHAZO"

    return resultado, D_crit_sim_04, p_value_04


def inciso_d(datos, lamda, D_stat):
    print("\n" + "=" * 60)
    print("INCISO D: Simulación Exp(0.05), alpha = 0.0004")
    print("=" * 60)

    n = len(datos)
    N_sim = 100000

    print(f"Generando {N_sim} muestras Exp({lamda}) directamente...")
    D_sim = simular_ks_exponencial(n, lamda, N_sim)

    D_crit_sim_004 = np.percentile(D_sim, 99.96)
    p_value_004 = np.mean(D_sim >= D_stat)

    print(f"\nValor crítico simulado (percentil 99.96): {D_crit_sim_004:.6f}")
    print(f"p-value simulado: {p_value_004:.6f}")
    print(f"D observado: {D_stat:.6f}")

    if D_stat > D_crit_sim_004:
        print(f"\nDECISIÓN: Se RECHAZA H0 (D > {D_crit_sim_004:.6f})")
        resultado = "RECHAZO"
    else:
        print(f"\nDECISIÓN: NO se rechaza H0 (D <= {D_crit_sim_004:.6f})")
        resultado = "NO RECHAZO"

    return resultado, D_crit_sim_004, p_value_004


# INCISO E PARCIAL 2024
# def inciso_e(datos, lamda, d_obs):
#    print("\n" + "=" * 60)
#    print("inciso e: estadístico ks con uniforms específicos")
#    print("=" * 60)

#    print(f"uniforms dados: {u_dados}")

#    muestra_sim = -np.log(u_dados) / lamda
#    print(f"\nmuestra simulada (exp({lamda})):")
#    for i, (u, x) in enumerate(zip(u_dados, muestra_sim), 1):
#        print(f"  u{i} = {u:.2f} -> x{i} = {x:.4f}")

#    d_sim, d_plus, d_minus = calcular_estadistico_ks(muestra_sim, lamda)

#    print("\nresultados:")
#    print(f"  d_sim = {d_sim:.6f}")
#    print(f"  d+ = {d_plus:.6f}")
#    print(f"  d- = {d_minus:.6f}")

#    if d_sim >= d_obs:
#        print(f"\nd_sim = {d_sim:.6f} >= d_obs = {d_obs:.6f}  ->  es extremo")
#        es_extremo = true
#    else:
#        print(f"\nd_sim = {d_sim:.6f} < d_obs = {d_obs:.6f}  ->  no es extremo")
#        es_extremo = false

#    return D_sim, es_extremo


def verificacion_scipy(datos, lamda):
    print("\n" + "=" * 60)
    print("VERIFICACIÓN con scipy.stats.kstest")
    print("=" * 60)

    ks_stat, ks_pvalue = stats.kstest(datos, "expon", args=(0, 1 / lamda))
    print(f"KS statistic: {ks_stat:.6f}")
    print(f"p-value: {ks_pvalue:.6f}")


def main():
    print("\n" + "=" * 60)
    print("EJERCICIO 2: Prueba de Kolmogorov-Smirnov")
    print("=" * 60 + "\n")

    D_stat = inciso_a_b(DATOS, LAMDA)

    res_c, crit_c, pval_c = inciso_c(DATOS, LAMDA, D_stat)

    res_d, crit_d, pval_d = inciso_d(DATOS, LAMDA, D_stat)

    verificacion_scipy(DATOS, LAMDA)

    print("\n" + "=" * 60)
    print("RESUMEN")
    print("=" * 60)
    print(f"D observado: {D_stat:.6f}")
    print(f"\nInciso c) alpha=0.04: {res_c} (crítico={crit_c:.6f}, p={pval_c:.6f})")
    print(f"Inciso d) alpha=0.0004: {res_d} (crítico={crit_d:.6f}, p={pval_d:.6f})")


if __name__ == "__main__":
    main()
