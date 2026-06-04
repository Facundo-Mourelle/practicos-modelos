import numpy as np

# Definición de las funciones de intensidad para cada inciso
def lambda_i(t):
    return 3 + 4 / (t + 1)

def lambda_ii(t):
    return (t - 2)**2 - 5 * t + 17

def lambda_iii(t):
    if 2 <= t <= 3:
        return t**2 - 1
    elif 3 < t <= 6:
        return 1 - t / 6
    else:
        return 0

def simular_poisson_no_homogeneo(func_lambda, cota_lambda, T_max, t_inicial=0):
    """
    Algoritmo de adelgazamiento estándar (Thinning).
    Retorna el número de eventos aceptados y la lista con sus tiempos de arribo.
    """
    t = t_inicial
    NT = 0
    eventos = []
    
    while t < T_max:
        # Generar el tiempo hasta el próximo evento usando el proceso homogéneo mayorante
        u1 = np.random.uniform()
        t += -np.log(1 - u1) / cota_lambda
        
        if t <= T_max:
            # Criterio de aceptación/rechazo
            u2 = np.random.uniform()
            if u2 < func_lambda(t) / cota_lambda:
                NT += 1
                eventos.append(t)
                
    return NT, eventos

# --- Ejecución de las simulaciones del inciso a) ---
print("--- INCISO A: Adelgazamiento Estándar ---")

# i) T = 3, cota = 7
nt_i, ev_i = simular_poisson_no_homogeneo(lambda_i, cota_lambda=7, T_max=3)
print(f"i) Cantidad de eventos: {nt_i}. Tiempos: {[round(float(e), 3) for e in ev_i]}")

# ii) T = 5, cota = 21
nt_ii, ev_ii = simular_poisson_no_homogeneo(lambda_ii, cota_lambda=21, T_max=5)
print(f"ii) Cantidad de eventos: {nt_ii}. Tiempos: {[round(float(e), 3) for e in ev_ii]}")

# iii) T = 6, cota = 8, empezando en t = 2 por definición del enunciado
nt_iii, ev_iii = simular_poisson_no_homogeneo(lambda_iii, cota_lambda=0.5, T_max=6, t_inicial=2)
print(f"iii) Cantidad de eventos: {nt_iii}. Tiempos: {[round(float(e), 3) for e in ev_iii]}")


def poisson_adelgazamiento_intervalos(func_lambda, limites, cotas_lambda, t_inicial=0):
    """
    Algoritmo de adelgazamiento mejorado segmentando por subintervalos.
    'limites': lista con los extremos derechos de cada intervalo.
    'cotas_lambda': lista con las cotas superiores de cada intervalo.
    """
    t = t_inicial
    NT = 0
    eventos = []
    j = 0  # Índice del intervalo actual
    num_intervalos = len(limites)
    
    # Generar el primer salto exponencial bajo la primera tasa
    t += -np.log(1 - np.random.uniform()) / cotas_lambda[j]
    
    while j < num_intervalos:
        if t <= limites[j]:
            # El evento cae dentro del intervalo actual 'j'
            u = np.random.uniform()
            if u < func_lambda(t) / cotas_lambda[j]:
                NT += 1
                eventos.append(t)
            # Avanzar el tiempo con la tasa del intervalo actual
            t += -np.log(1 - np.random.uniform()) / cotas_lambda[j]
        else:
            # El evento se pasa del intervalo actual. 
            # Reescalamos el tiempo restante excedido con la tasa del próximo intervalo 'j+1'
            if j + 1 < num_intervalos:
                t = limites[j] + (t - limites[j]) * cotas_lambda[j] / cotas_lambda[j + 1]
            j += 1
            
    return NT, eventos

# --- Ejecución de las simulaciones mejoradas del inciso b) ---
print("\n--- INCISO B: Adelgazamiento Mejorado por Intervalos ---")

# i) Intervalos: [0,1), [1,2), [2,3]
nt_i_m, ev_i_m = poisson_adelgazamiento_intervalos(lambda_i, limites=[1, 2, 3], cotas_lambda=[7.0, 5.0, 4.334])
print(f"i) Mejorado - Eventos: {nt_i_m}. Tiempos: {[round(float(e), 3) for e in ev_i_m]}")

# ii) Intervalos: [0,2), [2,4), [4,5]
nt_ii_m, ev_ii_m = poisson_adelgazamiento_intervalos(lambda_ii, limites=[2, 4, 5], cotas_lambda=[21.0, 6.0, 1.0])
print(f"ii) Mejorado - Eventos: {nt_ii_m}. Tiempos: {[round(float(e), 3) for e in ev_ii_m]}")

# iii) Intervalos: [2, 2.5), [2.5, 3], (3, 6]
nt_iii_m, ev_iii_m = poisson_adelgazamiento_intervalos(lambda_iii, limites=[2.5, 3.0, 6.0], cotas_lambda=[0.1, 0.5, 0.5], t_inicial=2)
print(f"iii) Mejorado - Eventos: {nt_iii_m}. Tiempos: {[round(float(e), 3) for e in ev_iii_m]}")
