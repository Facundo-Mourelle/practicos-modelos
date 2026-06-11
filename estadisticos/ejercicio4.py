import numpy as np
from scipy import stats

# Datos del ejercicio
datos = np.array([86.0, 133.0, 75.0, 22.0, 11.0, 144.0,
                 78.0, 122.0, 8.0, 146.0, 33.0, 41.0, 99.0])
# H0: provienen de Exp(u=50)
# => x ~ F(x)= 1 - e^(-x/50)
n = len(datos)
theta = 50.0

# Agrupamos en 3 intervalos ya que F(x) puede ir al infinito

# 1. Definir los cortes para 3 intervalos equiprobables (p = 1/3, 2/3)

# F(x1) = 1/3 => 1 - e^(x1/50) = 1/3  <=> x1 = -50 * ln(2/3)
corte1 = -theta * np.log(2/3)
# F(x2) = 2/3 => 1 - e^(x1/50) = 2/3  <=> x1 = -50 * ln(1/3)
corte2 = -theta * np.log(1/3)

# 2. Contar frecuencias observadas
o1 = np.sum(datos < corte1)
o2 = np.sum((datos >= corte1) & (datos < corte2))
o3 = np.sum(datos >= corte2)

observados = np.array([o1, o2, o3])
esperados = np.array([n/3, n/3, n/3])

# 3. Calcular estadístico y p-valor
# grados de libertad = 2 ya que tenemos la media y no estimamos
# ningun otro parametro, entonces ddof = k - 1 = 3-1 = 2
T, _ = stats.chisquare(f_obs=observados, f_exp=esperados, ddof=2)
p_valor = 1 - stats.chi2.cdf(T, df=2)

print(f"Estadístico T: {T:.4f}")
print(f"p-valor: {p_valor:.4f}")
