import numpy as np


# =====================================================================
# SECCIÓN A CAMBIAR: TASA VARIABLE Y COTA MÁXIMA
# =====================================================================
def lambda_t(t):
    # Ejemplo: lambda(t) = 3 + 4/(t + 1)
    return 3.0 + 4.0 / (t + 1.0)


T_MAX = 3.0       # Tiempo final del proceso
# El valor máximo que puede tomar lambda(t) en el intervalo [0, T_MAX]
LAMBDA_MAX = 7.0
# =====================================================================

t = 0.0
arribos = []

while t < T_MAX:
    u1 = np.random.rand()
    # Avanzar el tiempo usando la tasa máxima (proceso homogéneo auxiliar)
    t += -np.log(u1) / LAMBDA_MAX

    if t < T_MAX:
        u2 = np.random.rand()
        # Criterio de Aceptación / Rechazo (Adelgazamiento)
        if u2 <= lambda_t(t) / LAMBDA_MAX:
            arribos.append(t)  # Guardamos el instante del arribo aceptado

print("Proceso de Poisson No Homogéneo:")
print(f"Cantidad total de eventos generados: {len(arribos)}")
print(f"Tiempos de arribo: {arribos[:5]} ... (primeros 5)")
