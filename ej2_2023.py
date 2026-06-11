import numpy as np


def lambda_real(t):
    """Función de intensidad del enunciado."""
    if 0 <= t < 3:
        return t + 3
    elif 3 <= t <= 5:
        return 10 - 2 * t
    else:
        return 0


def simular_poisson_no_homogeneo_mejorado():
    # Definición de los 4 intervalos definidos en el inciso b: (t_inicio, t_fin, lambda_local)
    intervalos = [(0.0, 1.5, 4.5), (1.5, 3.0, 6.0), (3.0, 4.0, 4.0), (4.0, 5.0, 2.0)]

    t = 0.0
    tiempos_eventos = []
    idx_intervalo = 0

    # Simulación recorriendo los tramos temporales
    while t < 5.0 and idx_intervalo < len(intervalos):
        t_inicio, t_fin, lambda_local = intervalos[idx_intervalo]

        # 1. Avanzar el tiempo usando la tasa del intervalo actual
        u1 = np.random.uniform(0, 1)
        t += -np.log(u1) / lambda_local

        # 2. Controlar si saltamos al siguiente intervalo
        if t > t_fin:
            # Por falta de memoria reajustamos el tiempo al límite del tramo y avanzamos de índice
            t = t_fin
            idx_intervalo += 1
            continue

        # 3. Criterio de Aceptación / Rechazo (Thinning)
        u2 = np.random.uniform(0, 1)
        if u2 <= lambda_real(t) / lambda_local:
            # Guardamos como float nativo de Python para una impresión limpia
            tiempos_eventos.append(float(t))

    return tiempos_eventos


# --- EJECUCIÓN Y REPORTE ESTRUCTURADO ---
if __name__ == "__main__":
    eventos_simulados = simular_poisson_no_homogeneo_mejorado()

    print("=" * 60)
    print("REPORTE DE SIMULACIÓN: PROCESO DE POISSON NO HOMOGÉNEO")
    print("=" * 60)
    print(f"Cantidad total de eventos detectados: {len(eventos_simulados)}")
    print("-" * 60)
    # Formateamos la lista para mostrar solo 3 decimales por cada tiempo de arribo
    tiempos_formateados = [round(elem, 3) for elem in eventos_simulados]
    print(f"Tiempos de eventos de arribo:\n{tiempos_formateados}")
    print("=" * 60)
