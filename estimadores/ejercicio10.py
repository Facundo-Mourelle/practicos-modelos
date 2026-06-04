import numpy as np
import scipy.stats as stats


def proximo_arribo(t_actual):
    """
    Genera el tiempo del próximo arribo utilizando el método de Adelgazamiento (Thinning).
    Tasa lambda(t) = 7 - 1/(t+1). La tasa máxima lambda_max = 7.
    """
    t = t_actual
    lambda_max = 7.0
    while True:
        # Generar tiempo de inter-arribo exponencial con tasa lambda_max
        u1 = np.random.uniform()
        t += -np.log(u1) / lambda_max

        # Probabilidad de aceptación
        lambda_t = 7.0 - 1.0 / (t + 1.0)
        u2 = np.random.uniform()

        if u2 <= lambda_t / lambda_max:
            return t


def tiempo_servicio(tasa):
    """
    Genera un tiempo de servicio Exponencial utilizando el método de la Transformada Inversa.
    """
    u = np.random.uniform()
    return -np.log(u) / tasa


def simular_corrida():
    """
    Simula el sistema hasta que se completen 1000 servicios.
    Devuelve el tiempo medio en el sistema y la cantidad de servicios en el Servidor 1.
    """
    t = 0.0
    n1 = 0  # Clientes en servidor 1 (cola + servicio)
    n2 = 0  # Clientes en servidor 2 (cola + servicio)

    cola1 = []  # guarda los tiempos de arribo de los clientes en S1
    cola2 = []  # guarda los tiempos de arribo de los clientes en S2

    NA = 0  # Llegadas acumuladas
    ND = 0  # Salidas acumuladas (servicios completados)
    servicios_S1 = 0

    tA = proximo_arribo(t)
    t1 = np.inf
    t2 = np.inf

    tiempo_total_sistema = 0.0

    # Detenemos cuando salen los primeros 1000 clientes
    while ND < 1000:
        evento_proximo = min(tA, t1, t2)

        # --- CASO 1: Próxima llegada ---
        if evento_proximo == tA:
            t = tA
            NA += 1
            tA = proximo_arribo(t)

            # Política de ruteo: Cola más corta, desempata Servidor 1
            if n1 <= n2:
                n1 += 1
                cola1.append(t)
                if n1 == 1:  # Si el servidor 1 estaba libre
                    t1 = t + tiempo_servicio(3.0)
            else:
                n2 += 1
                cola2.append(t)
                if n2 == 1:  # Si el servidor 2 estaba libre
                    t2 = t + tiempo_servicio(4.0)

        # --- CASO 2: Fin de servicio en Servidor 1 ---
        elif evento_proximo == t1:
            t = t1
            ND += 1
            n1 -= 1
            servicios_S1 += 1

            tiempo_llegada = cola1.pop(0)
            tiempo_total_sistema += t - tiempo_llegada

            if n1 > 0:
                t1 = t + tiempo_servicio(3.0)
            else:
                t1 = np.inf

        # --- CASO 3: Fin de servicio en Servidor 2 ---
        else:
            t = t2
            ND += 1
            n2 -= 1

            tiempo_llegada = cola2.pop(0)
            tiempo_total_sistema += t - tiempo_llegada

            if n2 > 0:
                t2 = t + tiempo_servicio(4.0)
            else:
                t2 = np.inf

    tiempo_medio_sistema = tiempo_total_sistema / 1000.0
    return tiempo_medio_sistema, servicios_S1


def analisis_estadistico():

    tiempos_medios = []
    servicios_s1_lista = []

    # Realizamos al menos 30 simulaciones iniciales para que la desviación estándar sea representativa
    N = 0
    while True:
        W_medio, count_S1 = simular_corrida()
        tiempos_medios.append(W_medio)
        servicios_s1_lista.append(count_S1)
        N += 1

        if N >= 30:
            std_W = np.std(tiempos_medios, ddof=1)
            std_C1 = np.std(servicios_s1_lista, ddof=1)

            error_estandar_W = std_W / np.sqrt(N)
            error_estandar_C1 = std_C1 / np.sqrt(N)

            # Criterios de parada dados por el inciso b) y c)
            if error_estandar_W < 0.01 and error_estandar_C1 < 0.1:
                break

    # Cálculo de los estimadores puntuales finales
    media_W = np.mean(tiempos_medios)
    media_C1 = np.mean(servicios_s1_lista)

    # --- Inciso d) Intervalos de Confianza al 90% ---
    # alfa = 0.10 => Z_0.95
    z_critico = stats.norm.ppf(0.95)

    ic_W_inf = media_W - z_critico * error_estandar_W
    ic_W_sup = media_W + z_critico * error_estandar_W

    ic_C1_inf = media_C1 - z_critico * error_estandar_C1
    ic_C1_sup = media_C1 + z_critico * error_estandar_C1

    print(f"--- RESULTADOS (Total de simulaciones: {N}) ---")
    print(f"\nTiempo Promedio en el Sistema (W):")
    print(f"  Estimación puntual: {media_W:.4f} horas")
    print(f"  Desviación Estándar Muestral del Estimador: {error_estandar_W:.4f}")
    print(f"  Intervalo de Confianza (90%): ({ic_W_inf:.4f}, {ic_W_sup:.4f})")

    print(f"\nNúmero Esperado de Servicios en S1 (C1):")
    print(f"  Estimación puntual: {media_C1:.2f} servicios")
    print(f"  Desviación Estándar Muestral del Estimador: {error_estandar_C1:.4f}")
    print(f"  Intervalo de Confianza (90%): ({ic_C1_inf:.2f}, {ic_C1_sup:.2f})")


# Ejecutar el programa
analisis_estadistico()
