import numpy as np
import scipy.stats as stats


# --- 1. FUNCIONES DEL PROCESO DE LLEGADA ---
def tasa_llegada(t):
    """Calcula lambda(t) periódica cada 8 horas."""
    t_mod = t % 8
    if t_mod <= 4:
        return 4 + 2.5 * t_mod
    else:
        return 14 - 2.5 * (t_mod - 4)


def proxima_llegada(t_actual):
    """Genera el próximo arribo usando thinning"""
    t = t_actual
    lambda_max = 14.0
    while True:
        u1 = np.random.uniform()
        t = t - np.log(u1) / lambda_max
        if t > 16:  # El centro no recibe pacientes luego de 16 hs
            return float("inf")
        u2 = np.random.uniform()
        if u2 <= tasa_llegada(t) / lambda_max:
            return t


# --- 2. MOTOR DE SIMULACIÓN (Un día de 16hs) ---
def simular_jornada():
    """Simula una jornada completa usando la lógica Tandem del apunte."""
    t = 0
    NA = 0
    ND = 0
    n1 = 0
    n2 = 0
    tA = proxima_llegada(t)
    t1 = float("inf")
    t2 = float("inf")

    A1 = {}
    A2 = {}
    D = {}

    # Bucle principal de eventos
    while tA < float("inf") or t1 < float("inf") or t2 < float("inf"):
        eventoProximo = min(tA, t1, t2)

        # CASO 1: Próxima Llegada
        if eventoProximo == tA:
            t = tA
            NA += 1
            n1 += 1
            tA = proxima_llegada(t)

            if n1 == 1:
                Y1 = -np.log(np.random.uniform()) / 15
                t1 = t + Y1
            A1[NA] = t

        # CASO 2: Fin de servicio en servidor 1 (Admisión)
        elif eventoProximo == t1:
            t = t1
            n1 -= 1
            if n1 == 0:
                t1 = float("inf")
            else:
                Y1 = -np.log(np.random.uniform()) / 15
                t1 = t + Y1

            n2 += 1
            if n2 == 1:
                Y2 = -np.log(np.random.uniform()) / 12
                t2 = t + Y2

            numCliente = NA - n1
            A2[numCliente] = t

        # CASO 3: Fin de servicio en servidor 2 (Diagnóstico)
        else:
            t = t2
            ND += 1
            n2 -= 1
            if n2 == 0:
                t2 = float("inf")
            else:
                Y2 = -np.log(np.random.uniform()) / 12
                t2 = t + Y2

            numCliente = NA - n1 - n2
            D[numCliente] = t

    # Procesar métricas de la jornada
    tiempos_permanencia = [D[i] - A1[i] for i in range(1, NA + 1)]
    tiempo_promedio = np.mean(tiempos_permanencia) if NA > 0 else 0

    # ¿Quedaron pacientes después de las 16hs? (Cierre de puertas)
    quedan_pacientes = 1 if max(D.values()) > 16 else 0

    # Tiempo adicional esperado (en minutos)
    tiempo_adicional = max(0, max(D.values()) - 16) * 60

    return tiempo_promedio, quedan_pacientes, tiempo_adicional


# --- 3. CONTROL DE SIMULACIONES Y ESTIMADORES ---
def ejecutar_estudio():
    resultados_tiempo_prom = []
    resultados_prob = []
    resultados_tiempo_adic = []

    n_sims = 0

    # Criterios de parada
    detener_b = False
    detener_c = False
    detener_d = False

    print("Ejecutando simulaciones...")
    while not (detener_b and detener_c and detener_d) or n_sims < 100:
        n_sims += 1
        t_prom, q_pacientes, t_adic = simular_jornada()

        resultados_tiempo_prom.append(t_prom)
        resultados_prob.append(q_pacientes)
        resultados_tiempo_adic.append(t_adic)

        # Evaluar desviación estándar del estimador (S / sqrt(n))
        if n_sims >= 100:
            sd_b = np.std(resultados_tiempo_prom, ddof=1) / np.sqrt(n_sims)
            sd_c = np.std(resultados_prob, ddof=1) / np.sqrt(n_sims)
            sd_d = np.std(resultados_tiempo_adic, ddof=1) / np.sqrt(n_sims)

            detener_b = sd_b < 0.01
            detener_c = sd_c < 0.005
            detener_d = sd_d < 0.01

    # --- CÁLCULO DE INTERVALOS DE CONFIANZA (95%)  ---
    z = stats.norm.ppf(0.975)

    mean_b = np.mean(resultados_tiempo_prom)
    ic_b = (mean_b - z * sd_b, mean_b + z * sd_b)

    mean_c = np.mean(resultados_prob)
    ic_c = (mean_c - z * sd_c, mean_c + z * sd_c)

    mean_d = np.mean(resultados_tiempo_adic)
    ic_d = (mean_d - z * sd_d, mean_d + z * sd_d)

    print(f"Simulaciones totales realizadas: {n_sims}")
    print(
        f"b) Tiempo promedio de permanencia: {mean_b:.4f} horas. IC 95%: [{ic_b[0]:.4f}, {ic_b[1]:.4f}]"
    )
    print(
        f"c) Probabilidad de pacientes post 16hs: {mean_c:.4f}. IC 95%: [{ic_c[0]:.4f}, {ic_c[1]:.4f}]"
    )
    print(
        f"d) Tiempo adicional esperado: {mean_d:.4f} minutos. IC 95%: [{ic_d[0]:.4f}, {ic_d[1]:.4f}]"
    )


ejecutar_estudio()
