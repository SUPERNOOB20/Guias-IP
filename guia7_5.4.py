# Ejercicio 5.4:
import numpy as np

def potenciaMatriz(d: int, p: int):
    # m = np.random.random((d, d))
    m = np.random.randint(1,11, (d, d))
    while p > 1:
        m *= m
        p -= 1
    return m

print(potenciaMatriz(5, 2))