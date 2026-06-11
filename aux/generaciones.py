import numpy as np

# =====================================================================
# SECCIÓN A CAMBIAR: DEFINICIÓN DE TRANSFORMADAS INVERSAS
# Modifica la expresión matemática según la distribución del enunciado.
# =====================================================================


def generar_exponencial(lamda):
    u = np.random.rand()
    return -np.log(1.0 - u) / lamda  # O también -np.log(u) / lamda


def generar_uniforme_discreta(m, k):
    u = np.random.rand()
    return int(np.floor(u * (k - m + 1)) + m)


def generar_cauchy(lamb=1):
    u = np.random.rand()
    return lamb * np.tan(np.pi * (u - 0.5))
# =====================================================================
