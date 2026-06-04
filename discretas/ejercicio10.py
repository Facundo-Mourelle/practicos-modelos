import random
import math
import numpy as np

def generar_x():
    U = random.random()
    V = random.random()
    if U < 0.5:
        # Geom(p=0.5)
        return int(math.log(1 - V) / math.log(1 - 1/2)) + 1
    else:
        # Geom(p=1/3)
        return int(math.log(1 - V) / math.log(1 - 1/3)) + 1

# Simulación
repeticiones = 1000
resultados = [generar_x() for _ in range(repeticiones)]
esperanza_estimada = np.mean(resultados)

print(f"E(X) Exacta: 2.500")
print(f"E(X) Estimada ({repeticiones} reps): {esperanza_estimada:.3f}")
