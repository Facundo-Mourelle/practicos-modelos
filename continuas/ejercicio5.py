import numpy as np
import random

def generar_muestra_max_min(n_muestras):
    lambdas = [1, 2, 3]

    print(f"{'Muestra':<9} | {'X1 (λ=1)':<9} | {'X2 (λ=2)':<9} | {'X3 (λ=3)':<9} | {'M (Máximo)':<11} | {'m (Mínimo)':<11}")
    print("-" * 75)

    muestras_M = []
    muestras_m = []

    for i in range(1, n_muestras + 1):
        u1, u2, u3 = random.random(), random.random(), random.random()

        x1 = -np.log(u1) / lambdas[0]
        x2 = -np.log(u2) / lambdas[1]
        x3 = -np.log(u3) / lambdas[2]
        M = max(x1, x2, x3)
        m = min(x1, x2, x3)
        # Almacenar para estadísticas opcionales
        muestras_M.append(M)
        muestras_m.append(m)
        # Imprimir los resultados de esta iteración
        print(f"{i:<9} | {x1:<9.4f} | {x2:<9.4f} | {x3:<9.4f} | {M:<11.4f} | {m:<11.4f}")

    # Análisis final teórico vs empírico (opcional, para verificar el comportamiento de 'm')
    print("-" * 75)
    promedio_m = sum(muestras_m) / n_muestras
    # Recordando que m ~ Exponencial(lambda_1 + lambda_2 + lambda_3) = E(6)
    esperanza_m_teorica = 1 / sum(lambdas) 
    
    print(f"Promedio de los 10 valores de M : {sum(muestras_M) / n_muestras:.4f}")
    print(f"Promedio de los 10 valores de m : {promedio_m:.4f}")
    print(f"Valor esperado teórico E[m]     : {esperanza_m_teorica:.4f} (1/6)")

# Ejecutar para 10 muestras
generar_muestra_max_min(10)
