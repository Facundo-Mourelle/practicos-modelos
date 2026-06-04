import numpy as np

# Función para calcular la tasa de llegada lambda(t)
def lambda_t(t):
    t_ciclo = t % 10  # Ciclo periódico de 10 horas
    if t_ciclo <= 5:
        return 4 + 3 * t_ciclo  # Sube linealmente de 4 a 19
    else:
        return 19 - 3 * (t_ciclo - 5)  # Baja linealmente de 19 a 4

# Generador de próximo arribo usando el método de adelgazamiento (Thinning)
def generar_proxima_llegada(t_actual, T_max=100):
    t = t_actual
    lambda_max = 19.0
    while True:
        # arribo exponencial
        u1 = np.random.uniform()
        t += -np.log(u1) / lambda_max
        if t > T_max:
            return float('inf')
        # cond aceptacion
        u2 = np.random.uniform()
        if u2 <= lambda_t(t) / lambda_max:
            return t

# Simulación de una única réplica (Inciso a)
def simular_una_replica():
    t = 0.0
    n = 0
    NA = 0
    ND = 0

    tA = generar_proxima_llegada(0.0)
    tD = float('inf')

    tiempos_llegada = {}
    tiempos_permanencia = []
    solicitudes_completadas_post_T = 0

    while tA < float('inf') or tD < float('inf'):
        evento_proximo = min(tA, tD)

        # CASO 1: Llegada
        if evento_proximo == tA:
            t = tA
            NA += 1
            n += 1
            tiempos_llegada[NA] = t

            tA = generar_proxima_llegada(t)

            if n == 1:
                Y = -np.log(np.random.rand()) / 13.0
                tD = t + Y

        # CASO 2: Salida
        else:
            t = tD
            ND += 1
            n -= 1

            # Registrar tiempo de permanencia (D[i] - A[i])
            t_llegada = tiempos_llegada[ND]
            tiempos_permanencia.append(t - t_llegada)

            # Verificar si se completó después de T = 100
            if t > 100.0:
                solicitudes_completadas_post_T += 1

            if n == 0:
                tD = float('inf')
            else:
                Y = -np.log(np.random.rand()) / 13.0
                tD = t + Y


    promedio_permanencia = np.mean(tiempos_permanencia) if tiempos_permanencia else 0
    prob_post_T = 1.0 if solicitudes_completadas_post_T > 0 else 0.0
 
    return promedio_permanencia, prob_post_T

# --- Ciclo de Simulación Global con Criterio de Parada ---
promedios_permanencia = []
proporciones_post_T = []

# Forzamos un mínimo de réplicas para calcular la desviación estándar de manera estable
MIN_REPLICAS = 30
replica = 0

while True:
    replica += 1
    w_i, p_i = simular_una_replica()
    promedios_permanencia.append(w_i)
    proporciones_post_T.append(p_i)
 
    if replica >= MIN_REPLICAS:
        std_w = np.std(promedios_permanencia, ddof=1) / np.sqrt(replica)
        std_p = np.std(proporciones_post_T, ddof=1) / np.sqrt(replica)
 
        # Condición de parada simultánea para b y c (S/sqrt(n) < 0.01)
        if std_w < 0.01 and std_p < 0.01:
            break

print(f"Número total de réplicas ejecutadas: {replica}")
print(f"b) Tiempo promedio estimado en el sistema: {np.mean(promedios_permanencia):.4f} horas")
print(f"c) Probabilidad estimada de solicitudes completadas post T: {np.mean(proporciones_post_T):.4f}")
