import math
import random

def estimar_integral_1():
    # Integral i: g(u) = e^u * sqrt(2u)
    n = 1
    u = random.random()
    X = math.exp(u) * math.sqrt(2 * u)
    
    media = X
    scuad = 0.0  # S^2 inicial
    
    while n < 100 or math.sqrt(scuad / n) >= 0.01:
        n += 1
        u = 1-random.random()
        X = math.exp(u) / math.sqrt(2 * u)
        
        media_ant = media
        media = media_ant + (X - media_ant) / n
        scuad = scuad * (1 - 1 / (n - 1)) + n * (media - media_ant) ** 2
        
    desvio_estimador = math.sqrt(scuad / n)
    return media, n, desvio_estimador

def estimar_integral_2():
    n = 1
    u = 1.0 - random.random()
    
    # Expresión simplificada para el cambio de variables
    term = (1.0 - u) / u
    X = 2 * (term ** 2) * math.exp(-(term ** 2)) / (u ** 2)
    
    media = X
    scuad = 0.0
    
    while n < 100 or math.sqrt(scuad / n) >= 0.01:
        n += 1
        u = 1.0 - random.random()
        
        term = (1.0 - u) / u
        X = 2 * (term ** 2) * math.exp(-(term ** 2)) / (u ** 2)
        
        media_ant = media
        media = media_ant + (X - media_ant) / n
        scuad = scuad * (1 - 1 / (n - 1)) + n * (media - media_ant) ** 2
        
    desvio_estimador = math.sqrt(scuad / n)
    return media, n, desvio_estimador

# Ejecución de las simulaciones
print("--- Resultados de la Simulación Monte Carlo ---")
int1, n1, dest1 = estimar_integral_1()
print(f"Integral i) Valor estimado: {int1:.4f}")
print(f"            Simulaciones requeridas (n): {n1}")
print(f"            Desvío estándar del estimador: {dest1:.5f}")

int2, n2, dest2 = estimar_integral_2()
print(f"\nIntegral ii) Valor estimado: {int2:.4f} (Valor teórico exacto: {math.sqrt(math.pi)/2:.4f})")
print(f"             Simulaciones requeridas (n): {n2}")
print(f"             Desvío estándar del estimador: {dest2:.5f}")
