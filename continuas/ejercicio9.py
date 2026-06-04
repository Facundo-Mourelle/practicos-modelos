import numpy as np

def normal_reproche_ross():
    while True:
        # Generamos dos exponenciales independientes mediante inversión
        u1, u2 = np.random.rand(), np.random.rand()
        y1 = -np.log(u1)
        y2 = -np.log(u2)
        
        # Condición de aceptación del Ejemplo 5f
        if y2 >= ((y1 - 1) ** 2) / 2:
            # Asignamos signo aleatorio
            if np.random.rand() < 0.5:
                return y1
            else:
                return -y1

def normal_metodo_polar():
    while True:
        # Generar puntos en el cuadrado [-1, 1]x[-1, 1]
        v1 = 2 * np.random.rand() - 1
        v2 = 2 * np.random.rand() - 1
        s = v1**2 + v2**2
        
        # Aceptar si está dentro del círculo unitario (excluyendo el origen)
        if 0 < s < 1:
            # Retorna una de las dos variables normales generadas
            return v1 * np.sqrt((-2 * np.log(s)) / s)
            # La otra variable disponible es: v2 * np.sqrt((-2 * np.log(s)) / s)

def normal_razon_uniformes():
    # Límites del rectángulo envolvente para N(0,1)
    u_max = 1.0
    v_max = np.sqrt(2 / np.e)
    v_min = -v_max
    
    while True:
        u = np.random.rand()
        v = np.random.uniform(v_min, v_max)
        z = v / u
        
        # Condición de aceptación exacta
        if z**2 <= -4 * np.log(u):
            return z


def evaluar_metodos(n_muestras=10000):
    # Vectorizar la generación llamando a las funciones escritas
    muestras_ross = np.array([normal_reproche_ross() for _ in range(n_muestras)])
    muestras_polar = np.array([normal_metodo_polar() for _ in range(n_muestras)])
    muestras_razon = np.array([normal_razon_uniformes() for _ in range(n_muestras)])
    
    # Estructura para mostrar resultados
    metodos = {
        "A) Rechazo (Ross 5f)": muestras_ross,
        "B) Método Polar": muestras_polar,
        "C) Razón entre Uniformes": muestras_razon
    }
    
    print(f"--- Resultados sobre {n_muestras:,} valores ---")
    print(f"{'Método':<25} | {'Media Muestral':<15} | {'Varianza Muestral':<17}")
    print("-" * 65)
    
    for nombre, datos in metodos.items():
        media = np.mean(datos)
        # ddof=1 para usar el denominador (n - 1) de la varianza muestral insesgada
        varianza = np.var(datos, ddof=1) 
        print(f"{nombre:<25} | {media:>14.5f} | {varianza:>17.5f}")

if __name__ == "__main__":
    # Fijamos semilla para reproducibilidad si es necesario
    np.random.seed(42)
    evaluar_metodos()
