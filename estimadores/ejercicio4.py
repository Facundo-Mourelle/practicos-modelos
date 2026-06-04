import numpy as np

def estimar_pi_inciso_a():
    n = 0
    dentro_circulo = 0
    sd_p = float('inf')
    p_hat = 0
    
    # Se exigen al menos 2 datos para calcular la desviación estándar
    while n < 2 or sd_p >= 0.01:
        n += 1
        x, y = np.random.uniform(-1, 1, 2)
        if x**2 + y**2 <= 1:
            dentro_circulo += 1
            
        p_hat = dentro_circulo / n
        if n > 1:
            # Desviación estándar del estimador de la proporción
            sd_p = np.sqrt((p_hat * (1 - p_hat)) / n)
            
    pi_est = 4 * p_hat
    print(f"--- Inciso A ---")
    print(f"Simulaciones (n): {n}")
    print(f"Proporción estimada (p_hat): {p_hat:.4f}")
    print(f"Pi estimado: {pi_est:.4f}")
    print(f"Desviación Estándar: {sd_p:.4f}\n")

def estimar_pi_inciso_b(ancho_maximo):
    n = 0
    dentro_circulo = 0
    ancho = float('inf')
    z = 1.96 # Valor Z para 95% de confianza
    p_hat = 0
    
    while n < 2 or ancho >= ancho_maximo:
        n += 1
        x, y = np.random.uniform(-1, 1, 2)
        if x**2 + y**2 <= 1:
            dentro_circulo += 1
            
        p_hat = dentro_circulo / n
        if n > 1:
            sd_p = np.sqrt((p_hat * (1 - p_hat)) / n)
            # Ancho del intervalo para Pi
            ancho = 2 * 4 * z * sd_p
            
    pi_est = 4 * p_hat
    print(f"Ancho objetivo: < {ancho_maximo}")
    print(f"Simulaciones (n) necesarias: {n}")
    print(f"Pi estimado: {pi_est:.4f}")
    print(f"Ancho final obtenido: {ancho:.5f}\n")

# Ejecución
estimar_pi_inciso_a()
print("--- Inciso B ---")
for w in [0.1, 0.05, 0.001]:
    estimar_pi_inciso_b(w)
