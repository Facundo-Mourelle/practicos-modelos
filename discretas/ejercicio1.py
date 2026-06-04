import numpy as np

def simular_coincidencias(n=100, r=10, iteraciones=1000000):
    exitos_totales = []
    primeras_r_coinciden = 0
    exactamente_r_primeras = 0
    
    # Creamos el mazo original [1, 2, ..., 100]
    mazo_original = list(range(1, n + 1))
    
    for _ in range(iteraciones):
        # Barajado (Algoritmo de permutación aleatoria del texto)
        mazo = mazo_original[:]
        for j in range(n - 1, 0, -1):
            indice = np.random.randint(0, j+1)
            mazo[j], mazo[indice] = mazo[indice], mazo[j]
        
        # Contar coincidencias totales
        coincidencias = sum(1 for i, carta in enumerate(mazo, 1) if carta == i)
        exitos_totales.append(coincidencias)
        
        # Evaluar inciso (a)
        primeras_r = all(mazo[i] == (i + 1) for i in range(r))
        if primeras_r:
            primeras_r_coinciden += 1
            # Verificar si las restantes NO tienen coincidencias
            restantes_coinciden = any(mazo[i] == (i + 1) for i in range(r, n))
            if not restantes_coinciden:
                exactamente_r_primeras += 1
                
    print(f"--- Resultados de la Simulación ({iteraciones} iteraciones) ---")
    print(f"E(X) estimada: {np.mean(exitos_totales):.4f}")
    print(f"Var(X) estimada: {np.var(exitos_totales):.4f}")
    print(f"Prob. primeras {r} coincidencias: {primeras_r_coinciden/iteraciones}")
    print(f"Prob. exactamente {r} en las primeras {r}: {exactamente_r_primeras/iteraciones}")

# Ejecutar
simular_coincidencias(iteraciones=100)
simular_coincidencias(iteraciones=1000)
simular_coincidencias(iteraciones=10000)
simular_coincidencias(iteraciones=100000)
