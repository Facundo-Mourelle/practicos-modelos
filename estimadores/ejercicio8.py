import numpy as np

# Tasa de llegada del proceso de Poisson no homogéneo
def lambda_t(t):
    t_ciclo = t % 10
    if t_ciclo <= 5:
        return 4 + 3 * t_ciclo
    else:
        return 19 - 3 * (t_ciclo - 5)

# Generador de próximo arribo (Thinning)
def generar_proxima_llegada(t_actual, T_max=100):
    t = t_actual
    lambda_max = 19.0
    while True:
        u1 = np.random.rand()
        t += -np.log(u1) / lambda_max
        if t > T_max:
            return float('inf')
        u2 = np.random.rand()
        if u2 <= lambda_t(t) / lambda_max:
            return t

# Simulación de una única réplica
def simular_una_replica_con_descansos():
    t = 0.0
    n = 0
    NA = 0
    ND = 0
    
    tA = generar_proxima_llegada(0.0)
    tD = float('inf')

    # Excepción: la primera solicitud se atiende de inmediato
    t_fin_descanso = float('inf')
    
    tiempos_llegada = {}
    tiempos_permanencia = []
    tiempo_total_descanso = 0.0
    
    while tA < float('inf') or tD < float('inf') or t_fin_descanso < float('inf'):
        evento_proximo = min(tA, tD, t_fin_descanso)
        
        # --- CASO 1: Llegada de una solicitud ---
        if evento_proximo == tA:
            t = tA
            NA += 1
            n += 1
            tiempos_llegada[NA] = t
            
            tA = generar_proxima_llegada(t)
            
            # Si el servidor estaba libre y NO en descanso (inicio de simulación)
            if n == 1 and t_fin_descanso == float('inf') and tD == float('inf'):
                Y = -np.log(np.random.rand()) / 13.0
                tD = t + Y
                
        # --- CASO 2: Fin de servicio ---
        elif evento_proximo == tD:
            t = tD
            ND += 1
            n -= 1
            
            # Registrar permanencia
            t_llegada = tiempos_llegada[ND]
            tiempos_permanencia.append(t - t_llegada)
            
            if n > 0:
                # Hay clientes en cola, seguir atendiendo
                Y = -np.log(np.random.rand()) / 13.0
                tD = t + Y
            else:
                # Cola vacía, inicia descanso
                tD = float('inf')
                if t < 100:  # Validar que estemos en horario operativo
                    descanso = np.random.uniform(0, 0.3)
                    tiempo_total_descanso += descanso
                    t_fin_descanso = t + descanso
                    
        # --- CASO 3: Fin de descanso ---
        elif evento_proximo == t_fin_descanso:
            t = t_fin_descanso
            if n > 0:
                # Si durante el descanso llegaron clientes, comenzar atención
                t_fin_descanso = float('inf')
                Y = -np.log(np.random.rand()) / 13.0
                tD = t + Y
            else:
                # Si sigue vacío, tomar otro descanso
                if t < 100:
                    descanso = np.random.uniform(0, 0.3)
                    tiempo_total_descanso += descanso
                    t_fin_descanso = t + descanso
                else:
                    # Si ya pasaron las 100 hrs y no hay trabajos, finaliza la jornada
                    t_fin_descanso = float('inf')
                    
    promedio_permanencia = np.mean(tiempos_permanencia) if tiempos_permanencia else 0
    return promedio_permanencia, tiempo_total_descanso

# --- Ciclo de Simulación Global ---
promedios_permanencia = []
tiempos_descanso = []

MIN_REPLICAS = 30
replica = 0

while True:
    replica += 1
    w_i, d_i = simular_una_replica_con_descansos()
    promedios_permanencia.append(w_i)
    tiempos_descanso.append(d_i)
    
    # Evaluar criterios estadísticos después de un mínimo de réplicas
    if replica >= MIN_REPLICAS:
        std_w = np.std(promedios_permanencia, ddof=1) / np.sqrt(replica)
        std_d = np.std(tiempos_descanso, ddof=1) / np.sqrt(replica)
        
        # Parar cuando ambas desviaciones del estimador sean menores a 0.05
        if std_w < 0.05 and std_d < 0.05:
            break

print(f"Simulaciones realizadas: {replica}")
print(f"b) Tiempo promedio de permanencia por solicitud: {np.mean(promedios_permanencia):.4f} horas")
print(f"c) Tiempo medio que el servidor pasa descansando: {np.mean(tiempos_descanso):.4f} horas")
