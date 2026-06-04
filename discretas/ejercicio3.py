import numpy as np

def simular_n():
    vistos = set()
    n_lanzamientos = 0
    while len(vistos) < 11:
        n_lanzamientos += 1
        suma = np.random.randint(1, 7) + np.random.randint(1, 7)
        vistos.add(suma)
    return n_lanzamientos

def ejecutar_experimento(iteraciones_lista):
    print(f"{'Iteraciones':>12} | {'Media':>8} | {'Desv. Est':>10} | {'P(N >= 15)':>10} | {'P(N <= 9)':>10}")
    print("-" * 65)
    
    for iters in iteraciones_lista:
        resultados = np.array([simular_n() for _ in range(iters)])
        
        media = np.mean(resultados)
        desviacion = np.std(resultados, ddof=1)
        p_ge_15 = np.mean(resultados >= 15)
        p_le_9 = np.mean(resultados <= 9)
        
        print(f"{iters:12d} | {media:8.2f} | {desviacion:10.2f} | {p_ge_15:10.4f} | {p_le_9:10.4f}")

if __name__ == "__main__":
    ensayos = [100, 1000, 10000, 100000]
    ejecutar_experimento(ensayos)
