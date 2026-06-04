import numpy as np
import warnings

warnings.filterwarnings("ignore")

def simular_integral_1(N):
    """Simula la integral de sin(x)/x usando U~(0,1)"""
    # Exclusivamente en el rango (0, 1)
    u = np.random.rand(N)
    
    # Transformación de variables
    valores = np.sin(np.pi * (1 + u)) / (1 + u)
    
    media = np.mean(valores)
    S = np.std(valores, ddof=1)
    semi_ancho = 1.96 * (S / np.sqrt(N))
    
    return media, S, semi_ancho

def simular_integral_2(N):
    """Simula la integral de 3/(3+x^4) usando U~(0,1)"""
    u = 1 - np.random.rand(N)
    
    # Transformación de variables
    x = (1 - u) / u
    valores = 3 / ((u**2) * (3 + x**4))
    
    media = np.mean(valores)
    S = np.std(valores, ddof=1)
    semi_ancho = 1.96 * (S / np.sqrt(N))
    
    return media, S, semi_ancho

def imprimir_tabla(func_simulacion, nombre_integral):
    print(f"\n--- {nombre_integral} ---")
    print(f"{'N simulaciones':<15} | {'Media (I)':<12} | {'Desv. Est. (S)':<15} | {'Semiancho IC(95%)':<15}")
    print("-" * 65)
    
    # Evaluamos para los valores fijos pedidos por la tabla 
    for N in [1000, 5000, 7000]:
        media, S, semi_ancho = func_simulacion(N)
        print(f"{N:<15} | {media:<12.4f} | {S:<15.4f} | {semi_ancho:<15.4f}")
        
    # Buscamos el Ns exacto para que el semiancho sea justo inferior a 0.001 
    # Usamos la desviación estándar S calculada para aproximar Ns de forma eficiente
    Ns_estimado = int((1.96 * S / 0.001)**2) + 1
    
    _, _, semi_ancho_final = func_simulacion(Ns_estimado)
    
    print(f"\n=> Número de simulaciones necesarias (Ns): {Ns_estimado}")
    print(f"=> Semiancho alcanzado: {semi_ancho_final:.5f}")

# Ejecución de las simulaciones
imprimir_tabla(simular_integral_1, "Integral i: sin(x)/x")
imprimir_tabla(simular_integral_2, "Integral ii: 3/(3+x^4)")
