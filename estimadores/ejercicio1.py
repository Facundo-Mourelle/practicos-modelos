import random
import math

def simular_ejercicio1():
    # Inicialización de variables
    # Para calcular S^2(n) recursivamente necesitamos al menos 2 datos iniciales
    z1 = random.gauss(0, 1)
    z2 = random.gauss(0, 1)
    
    n = 2
    media = (z1 + z2) / 2
    # Varianza muestral inicial para n=2
    scuad = ((z1 - media)**2 + (z2 - media)**2) / (n - 1) 
    
    # Condición de parada: n >= 100 y S(n)/sqrt(n) < 0.1
    # Equivalente a: n < 100 o sqrt(scuad/n) >= 0.1
    while n < 100 or math.sqrt(scuad / n) >= 0.1:
        n += 1
        z = random.gauss(0, 1) # Generar una nueva normal estándar
        
        # Actualización recursiva de la media muestral
        media_ant = media
        media = media_ant + (z - media_ant) / n
        
        # Actualización recursiva de la varianza muestral S^2(n)
        scuad = scuad * (1 - 1 / (n - 1)) + n * (media - media_ant)**2
        
    return n, media, scuad

# Ejecución de la simulación
datos_efectivos, media_muestral, varianza_muestral = simular_ejercicio1()

print(f"a) Número de datos generados efectivamente: {datos_efectivos}")
print(f"b) Media muestral de los datos generados: {media_muestral:.4f}")
print(f"c) Varianza muestral de los datos generados: {varianza_muestral:.4f}")
