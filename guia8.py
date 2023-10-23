# Ejercicio 2:
"""
def clonarSinComentarios(nombre_archivo: str):      # Devuelve nombre_archivo pero SIN las líneas comentadas.
    archivo = open(nombre_archivo, r)
    for i in len(contenido):
        linea = readline()
        if "#" in linea:
    return
"""


# print(clonarSinComentarios(C:/tuvieja/hola.txt))


"""
def clonarSinComentarios(nombre_archivo_input: str) -> None:
    
    # Abro archivo de input
    archivo_input = open(nombre_archivo_input, "r")
    
    # Abro archivo de output
    nombre_archivo_output: str = "ejercicio_2_output.txt"
    archivo_output = open(nombre_archivo_output, "w")
    
    for linea in archivo_input.readlines():
        if "#" not in linea:
            archivo_output.write(linea)
            
    archivo_input.close()
    archivo_output.close()
"""
    


def clonarSinComentarios(nombre_archivo_input: str) -> None:
    
    # Abro archivo de input
    archivo_input = open(nombre_archivo_input, "r")
    
    # Abro archivo de output
    nombre_archivo_output: str = "ejercicio_2_output.txt"
    archivo_output = open(nombre_archivo_output, "w")
    
    for linea in archivo_input.readlines():
        if not es_un_comentario(linea):
            archivo_output.write(linea)
            
    archivo_input.close()
    archivo_output.close()
    # return

def es_un_comentario(line: str) -> bool:
    for caracter in line:
        if caracter != " ":
            if caracter == "#":
                return True         # SÍ es un comentario
            return False            # NO es un comentario
    return False                    # Caso todos chars " ".




# clonarSinComentarios("ejemploComentado.txt")
clonarSinComentarios("ejemploComentado2.txt")


# print(clonarSinComentarios("ejemploComentado2.txt"))     <--- NO hacer esto.








# Ejercicio 10:

from queue import LifoQueue

"""
# NO RESPETA LA ESPECIFICACIÓN (no usa la pila como un parámetro de tipo "in"):

def buscarElMaximo (p: LifoQueue) -> int:
    while not p.empty():        # p.qsize() > 1:
        a = p.get()
        if p.empty():
            return a
        b = p.get()
        if a > b:
            p.put(a)
        else:
            p.put(b)
    
    return p.get()
"""



def buscarElMaximo (p: LifoQueue) -> int:
    p_copia : LifoQueue() = copiaQueue(p)
    while not p_copia.empty():        # p.qsize() > 1:
        a = p_copia.get()
        if p_copia.empty():
            return a
        b = p_copia.get()
        if a > b:
            p_copia.put(a)
        else:
            p_copia.put(b)
    
    return p_copia.get()

def copiaQueue(p: LifoQueue) -> LifoQueue:
    elements: [int] = []
    while not p.empty():
        elements.append(p.get())
    p_copy: LifoQueue = LifoQueue()
    for i in range(len(elements) - 1, -1, -1):   # Recorrre la lista "elements" en sentido inverso.
        p.put(elements[i])
        p_copy.put(elements[i])
    return p_copy

# TEST CASE - [1,7,4,5]:
pila: LifoQueue = LifoQueue()
pila.put(1)
pila.put(7)
pila.put(4)
pila.put(5)

# buscarElMaximo(pila)
# print(buscarElMaximo(pila))



# Ejercicio 16.1:
import numpy as np
from queue import Queue     # Va a ser una FIFO Queue

"""
def armarSecuenciaDeBingo() -> Queue:
    cola: Queue = Queue()
    # cola = np.random.randint(100, size=(1, 12))
    return cola
"""

def armarSecuenciaDeBingo() -> Queue:
    l: list = []
    for i in range(0, 100):
        l.append(i)
    np.random.shuffle(l)
    result: Queue = Queue()
    for elem in l:
        result.put(elem)
    return result

q = armarSecuenciaDeBingo()
# print(q.get())


# Ejercicio 16.2:
"""
# NO RESPETA la especificación:
def jugarCartonDeBingo(carton: list, bolillero: Queue) -> int:
    jugadas: int = 0
    while len(carton) != 0:         # El cartón todavía no fue completado.
        for i in range(0, len(carton)):
            if carton[i] == bolillero.get():
                carton.remove[i]
        jugadas += 1
            
    return jugadas
"""






def jugarCartonDeBingo(carton: list, bolillero: Queue) -> int:
    jugadas: int = 0
    casillasCompletadas = 0
    while casillasCompletadas != len(carton):         # El cartón todavía no fue completado.
        bolillaExtraida = bolillero.get()
        if bolillaExtraida in carton:
            # carton.remove(bolillaExtraida)
            casillasCompletadas += 1
    jugadas += 1
            
    return jugadas


cartonBingo: list = []
for i in range(0,10):
    cartonBingo.append(q.get())

a = list(range(0,100))

bolillero: Queue = Queue()
# bolillero = np.random.shuffle(a)      <--- NO

for i in range(0,len(a)):
    bolillero.put(a[i])

print(jugarCartonDeBingo(cartonBingo, bolillero))



"""
print(bolillero)
print(bolillero)
print(bolillero)
"""
# print(a)

"""
# Ejercicio 19:
def agruparPorLongitud(nombre_archivo: str) -> dict:
    archivo = open(nombre_archivo)
    return



agruparPorLongitud
"""