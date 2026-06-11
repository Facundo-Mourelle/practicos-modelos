import scipy.stats as stats


def estadisticoT(frecuencias, probabilidades):
    t = 0
    K = len(frecuencias)
    n = sum(frecuencias)
    for k in range(K):
        t += (frecuencias[k] - n * probabilidades[k]) ** 2 / (n * probabilidades[k])
    return t


probabilidades = [0.25, 0.5, 0.25]
frecuencias = [141, 291, 132]
esperados = [141, 282, 141]

t0 = estadisticoT(frecuencias, probabilidades)
chi2_stat, p_valor_analitico = stats.chisquare(f_obs=frecuencias, f_exp=esperados)


print(f"Estadístico Chi-cuadrado: {chi2_stat:.4f}")
print(f"p-valor (Analítico): {p_valor_analitico:.4f}")
# df := grados de libertad. como k = 3 => k-1 = 2
print("p-valor: ", 1 - stats.chi2.cdf(t0, df=2))
