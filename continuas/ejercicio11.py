import random
import numpy as np

def cauchy_transformada_inversa(lamda):
    U = random.random()  # Genera una variable uniforme U(0, 1)
    return lamda * np.tan(np.pi * (U - 0.5))

def simular_proporciones(N_sim=10000):
    lambdas = [1, 2.5, 0.3]
    print(f"Probabilidad Teórica para cualquier intervalo (-λ, λ): 0.5")
    print("-" * 65)

    
    for lamda in lambdas:
        exitos = 0
        for _ in range(N_sim):
            # Usamos el algoritmo de transformada inversa del inciso b
            X = cauchy_transformada_inversa(lamda)
            if -lamda < X < lamda:
                exitos += 1
        
        proporcion_muestral = exitos / N_sim
        print(f"Para λ = {lamda:<4} -> Proporción Simulada: {proporcion_muestral:.4f} (Error: {abs(0.5 - proporcion_muestral):.4f})")

simular_proporciones()
