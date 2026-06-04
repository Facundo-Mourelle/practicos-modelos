import numpy as np
import time

def simular_cauchy_inversa(n_muestras, lambda_param=1.0):
    """Genera muestras de Cauchy(lambda) usando el Método de la Transformada Inversa."""
    # 1. Generar U ~ Uniforme(0, 1)
    u = np.random.uniform(0.0, 1.0, n_muestras)
    
    # 2. Aplicar la función inversa calculada teóricamente
    return lambda_param * np.tan(np.pi * (u - 0.5))

# --- Inciso d) Validación con 10.000 simulaciones ---
np.random.seed(42)
N_SIMULACIONES = 10000
lambdas = [1.0, 2.5, 0.3]

print(f"Ejecutando {N_SIMULACIONES} simulaciones (Transformada Inversa):")
print("-" * 60)
for lam in lambdas:
    muestras_inv = simular_cauchy_inversa(N_SIMULACIONES, lambda_param=lam)
    exitos = np.sum((muestras_inv > -lam) & (muestras_inv < lam))
    proporcion = exitos / N_SIMULACIONES
    print(f"Para lambda = {lam:3.1f} | Proporción en (-λ, λ): {proporcion:.4f} | Teórico: 0.5000")
