import numpy as np
import scipy.stats as stats


def generar_exponencial(tasa):
    """
    Genera un valor de una v.a. exponencial usando el método de la
    transformada inversa a partir de una variable Uniforme(0,1).
    """
    u = np.random.uniform()
    return -np.log(u) / tasa


def simular_colapso_sistema(n=6, s=4, lambda_f=2, lambda_r=3):
    """
    Simula el modelo de reparación hasta el colapso del sistema.
    Retorna el tiempo T en el que ocurre el colapso.
    """
    t = 0.0
    r = 0  # Cantidad de máquinas averiadas (en reparación + en cola)

    # Inicialización: tiempos de falla para las 'n' máquinas en uso
    tiempos_falla = [t + generar_exponencial(lambda_f) for _ in range(n)]
    t_star = float("inf")  # Tiempo en el que finaliza la reparación actual

    while r <= s:
        # Encontrar el próximo evento (falla vs. fin de reparación)
        t_min_falla = min(tiempos_falla)
        evento_proximo = min(t_min_falla, t_star)

        # CASO 1: Ocurre una falla antes de que termine una reparación
        if evento_proximo == t_min_falla:
            t = t_min_falla
            r += 1

            # Condición de colapso: si las averiadas superan los repuestos
            if r > s:
                break

            # Si es la única máquina averiada, comienza a repararse enseguida
            if r == 1:
                t_star = t + generar_exponencial(lambda_r)

            # La máquina averiada sale de circulación (tiempo infinito)
            idx_maquina = tiempos_falla.index(t_min_falla)
            tiempos_falla[idx_maquina] = float("inf")

        # CASO 2: Termina una reparación antes de otra falla
        else:
            t = t_star
            r -= 1

            # La máquina reparada (o su reemplazo) vuelve al servicio.
            # Ocupamos un slot "infinito" en la lista de máquinas en uso.
            idx_libre = tiempos_falla.index(float("inf"))
            tiempos_falla[idx_libre] = t + generar_exponencial(lambda_f)

            # Si aún hay máquinas averiadas en cola, comienza la reparación de la siguiente
            if r > 0:
                t_star = t + generar_exponencial(lambda_r)
            else:
                t_star = float("inf")

    return t


def analisis_incisos_b_al_e():
    print("--- INICIANDO SIMULACIONES ---")

    # Parámetros generales
    n_maq = 6
    s_repuestos = 4
    lambda_f = 2
    lambda_r = 3
    z_95 = stats.norm.ppf(0.975)  # Aprox 1.96 para un IC del 95%

    # --- INCISOS B y C: Tiempo Medio hasta la falla del sistema ---
    print("\n Incisos b) y c)")
    tiempos_colapso = []
    error_estandar_media = float("inf")
    umbral_error = 0.01

    # Simulamos por lotes para mayor eficiencia
    while error_estandar_media >= umbral_error:
        # Agregamos 100 simulaciones al registro
        for _ in range(100):
            t_colapso = simular_colapso_sistema(n_maq, s_repuestos, lambda_f, lambda_r)
            tiempos_colapso.append(t_colapso)

        n_sim = len(tiempos_colapso)
        # S(n) / sqrt(n)
        desviacion_muestral = np.std(tiempos_colapso, ddof=1)
        error_estandar_media = desviacion_muestral / np.sqrt(n_sim)

    media_estimada = np.mean(tiempos_colapso)
    ic_media_inf = media_estimada - z_95 * error_estandar_media
    ic_media_sup = media_estimada + z_95 * error_estandar_media

    print(f"  - Simulaciones necesarias: {n_sim}")
    print(f"  - Tiempo medio estimado hasta la falla: {media_estimada:.4f} horas")
    print(
        f"  - Desviación estándar muestral del estimador (Error Estándar): {error_estandar_media:.4f}"
    )
    print(
        f"  - Intervalo de Confianza (95%): [{ic_media_inf:.4f}, {ic_media_sup:.4f}] horas"
    )

    # --- INCISOS D y E: Probabilidad de que el sistema falle antes de 90 min (1.5 horas) ---
    print("\n Incisos d) y e)")
    fallos_antes_90_min = []
    error_estandar_prop = float("inf")
    umbral_error_prop = 0.01

    while error_estandar_prop >= umbral_error_prop:
        for _ in range(100):
            # Reutilizamos la función. Evaluamos si colapsó antes de t=1.5
            t_colapso = simular_colapso_sistema(n_maq, s_repuestos, lambda_f, lambda_r)
            fallos_antes_90_min.append(1 if t_colapso < 1.5 else 0)

        n_sim_prop = len(fallos_antes_90_min)
        p_estimado = np.mean(fallos_antes_90_min)

        # Evitar división por cero en las primeras iteraciones si p=0 o p=1
        if p_estimado > 0 and p_estimado < 1:
            # Desviación estándar del estimador de proporción: sqrt(p * (1-p) / (n-1))
            error_estandar_prop = np.sqrt(
                (p_estimado * (1 - p_estimado)) / (n_sim_prop - 1)
            )

    ic_prop_inf = p_estimado - z_95 * error_estandar_prop
    ic_prop_sup = p_estimado + z_95 * error_estandar_prop

    print(f"  - Simulaciones necesarias: {n_sim_prop}")
    print(f"  - Probabilidad estimada de falla antes de 90 min: {p_estimado:.4f}")
    print(f"  - Desviación estándar muestral del estimador: {error_estandar_prop:.4f}")
    print(f"  - Intervalo de Confianza (95%): [{ic_prop_inf:.4f}, {ic_prop_sup:.4f}]")


if __name__ == "__main__":
    analisis_incisos_b_al_e()
