import numpy as np

# Configuración
n_iter = 1000
cajas = [1, 2, 3]
prob_cajas = [0.40, 0.32, 0.28]
medias = {1: 3, 2: 4, 3: 5}

tiempos = []
elecciones = []

# Simulación
for _ in range(n_iter):
    caja_elegida = np.random.choice(cajas, p=prob_cajas)
    espera = np.random.exponential(medias[caja_elegida])
    
    elecciones.append(caja_elegida)
    tiempos.append(espera)

tiempos = np.array(tiempos)
elecciones = np.array(elecciones)

# a) Estimar P(T < 4)
p_t_menor_4 = np.mean(tiempos < 4)

# b) Estimar P(Ci | T > 4)
mas_4 = tiempos > 4
elecciones_mas_4 = elecciones[mas_4]
total_mas_4 = len(elecciones_mas_4)

p_c1_dado_mas_4 = np.sum(elecciones_mas_4 == 1) / total_mas_4
p_c2_dado_mas_4 = np.sum(elecciones_mas_4 == 2) / total_mas_4
p_c3_dado_mas_4 = np.sum(elecciones_mas_4 == 3) / total_mas_4

print(f"Estimación P(T < 4): {p_t_menor_4:.4f}")
print(f"Probabilidades dado T > 4: Caja 1: {p_c1_dado_mas_4:.4f}, Caja 2: {p_c2_dado_mas_4:.4f}, Caja 3: {p_c3_dado_mas_4:.4f}")
