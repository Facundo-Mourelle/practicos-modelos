import numpy as np
import random

def simular_transformada_inversa(n):
    muestras = []
    # La transformada inversa tiene una tasa de aceptación del 100%
    for _ in range(n):
        u = random.random()
        x = np.exp(u)
        muestras.append(x)
    return muestras, n # El número de intentos es igual a n

def simular_aceptacion_rechazo(n):
    muestras = []
    intentos = 0
    
    while len(muestras) < n:
        intentos += 1
        # 1. Generar Y ~ U(1, e)
        u1 = np.random.uniform()
        y = 1 + (np.e - 1) * u1
        # 2. Generar U ~ U(0, 1) y evaluar condición
        u2 = random.random()
        if u2 <= 1 / y:
            muestras.append(y)
    return muestras, intentos

# --- Ejecución y Análisis ---
N_SIMULACIONES = 10000

print(f"--- Ejecutando {N_SIMULACIONES} simulaciones ---\n")

# 1. Ejecutar métodos
muestras_ti, intentos_ti = simular_transformada_inversa(N_SIMULACIONES)
muestras_ar, intentos_ar = simular_aceptacion_rechazo(N_SIMULACIONES)

# 2. Calcular estadísticos estimados (Promedio)
promedio_ti = sum(muestras_ti) / N_SIMULACIONES
promedio_ar = sum(muestras_ar) / N_SIMULACIONES
valor_esperado_real = np.e - 1

print("b) Comparación de Valor Esperado (Promedio) y Eficiencia:")
print(f"   Valor Esperado Teórico : {valor_esperado_real:.6f}")
print(f"   Promedio Trans. Inversa: {promedio_ti:.6f} (Error: {abs(promedio_ti - valor_esperado_real):.6f})")
print(f"   Promedio Acept/Rechazo : {promedio_ar:.6f} (Error: {abs(promedio_ar - valor_esperado_real):.6f})")

print(f"\n   Eficiencia (Intentos totales para {N_SIMULACIONES} muestras):")
print(f"   Trans. Inversa: {intentos_ti} iteraciones (C=1.0)")
print(f"   Acept/Rechazo : {intentos_ar} iteraciones (C empírico={intentos_ar/N_SIMULACIONES:.3f}, C teórico={valor_esperado_real:.3f})")

# 3. Calcular estimación de probabilidad P(X <= 2)
# Usaremos las muestras de la Transformada Inversa para la estimación
casos_favorables = sum(1 for x in muestras_ti if x <= 2)
prob_estimada = casos_favorables / N_SIMULACIONES
prob_real = np.log(2)

print("\nc) Estimación de Probabilidad P(X <= 2):")
print(f"   Valor Real P(X <= 2) : {prob_real:.6f}")
print(f"   Prob. Estimada       : {prob_estimada:.6f} (Error: {abs(prob_estimada - prob_real):.6f})")
