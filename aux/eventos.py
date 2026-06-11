import numpy as np


# =====================================================================
# SECCIÓN A CAMBIAR: PARÁMETROS DEL SISTEMA
# =====================================================================
T_FIN = 100.0  # Duración de la jornada de simulación
mu_servicio = 13.0
# =====================================================================


def correr_una_simulacion():
    # Inicialización de variables de tiempo y estado
    t = 0.0
    estado_servidor = 0  # 0 = Libre, 1 = Ocupado
    cola = 0

    # Inicialización de la lista de Eventos Futuros (tiempos absolutos)
    # Se genera el primer arribo (puede ser homogéneo o no homogéneo usando Módulo 2)
    # Supongamos arribos con tasa lambda=5
    tA = -np.log(np.random.rand()) / 5.0
    tD = float('inf')                    # No hay salidas programadas al inicio

    # Variables contadoras/acumuladoras de interés
    clientes_atendidos = 0
    tiempo_permanencia_total = 0
    registro_arribos = {}  # Para trackear cuándo llegó cada cliente y restar al salir

    while min(tA, tD) < T_FIN or estado_servidor == 1 or cola > 0:
        evento_proximo = min(tA, tD)

        # CASO 1: El próximo evento es un ARRIBO
        if evento_proximo == tA:
            t = tA
            # --- SECCIÓN A CAMBIAR: LÓGICA DE ARRIBO ---
            registro_arribos[clientes_atendidos] = t
            if estado_servidor == 0:
                estado_servidor = 1
                # Programar fin de servicio
                tD = t + (-np.log(np.random.rand()) / mu_servicio)
            else:
                cola += 1

            # Programar el siguiente arribo
            tA = t + (-np.log(np.random.rand()) / 5.0)
            # Si pasamos la hora de cierre, no agendamos más arribos
            if tA > T_FIN:
                tA = float('inf')
            # -------------------------------------------

        # CASO 2: El próximo evento es un FIN DE SERVICIO
        else:
            t = tD
            # --- SECCIÓN A CAMBIAR: LÓGICA DE SALIDA ---
            # Registrar datos del cliente que se va
            tiempo_permanencia_total += (t -
                                         registro_arribos[clientes_atendidos])
            clientes_atendidos += 1

            if cola > 0:
                cola -= 1
                # Programar siguiente fin de servicio para el próximo en cola
                tD = t + (-np.log(np.random.rand()) / mu_servicio)
            else:
                estado_servidor = 0
                tD = float('inf')
            # -------------------------------------------

    # Retornar la métrica de interés de esta corrida
    return tiempo_permanencia_total / max(1, clientes_atendidos)


# BUCLE GLOBAL: Ejecutar muchas corridas para obtener medias e intervalos de confianza
resultados_corridas = []
for _ in range(1000):  # Cambiar según condición de parada estadística (Módulo 1)
    resultados_corridas.append(correr_una_simulacion())

print(
    f"Eventos Discretos - Promedio de permanencia global: {np.mean(resultados_corridas):.4f}")
