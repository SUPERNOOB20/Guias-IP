# Ejercicio 2:

def es_un_comentario(line: str) -> bool:
    for c in line:
        if c!= " ":
            if c == "#":
                return True         # SÍ es un comentario
            return False            # NO es un comentario
    return False                    # Caso todos chars " ".
    

def clonarSinComentarios(nombre_archivo_input: str) -> None:    # Clona un archivo sin las líneas que empiecen con "#".
    
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
    
    


clonarSinComentarios("ejercicio_2_input.txt")
    
    
    
    
    
# Ejercicio 10:
from queue import LifoQueue

def copiar(p: LifoQueue[int]) -> LifoQueue[int]:
    elements: [int] = []
    while not p.empty():
        elements.append(p.get())
    p_copy: LifoQueue[int] = LifoQueue()
    for i in range(len(elements) - 1, -1, -1)   # Recorrre la lista "elements" en sentido inverso.
        p.put(elements[i])
        p_copy.put(elements[i])
    return p_copy


def buscarElMaximo (p: LifoQueue[int]) -> int:
    p_copy : LifoQueue[int] = LifoQueue()
    value = p_copy.get()
    while not p_copy.empty():
        next_value = p_copy.get()
        value = max(next_value, value)
    return


# Ejercicio 16:

# random.shuffle()
from numpy import random
from queue import Queue

def armarSecuenciaDeBingo() -> Queue[int]:
    l : [int] = []
    for i in range(0, 99+1, 1):
        l.append(i)
    random.shuffle(i)
    result: Queue[int] = Queue()
    for elem in l:
        result.put(elem)
    return result
        
        

def jugarCartonDeBingo(carton: list[int], bolillero: Queue[int]) -> [int]:
    jugadas: int = 0
    casillas_completadas_en_carton: int = 0
    while not bolillero.empty():
        # saco una bola
        bola = bolillero.get()
        jugadas += 1
        if bola in carton:
            casillas_completadas_en_carton += 1
        # chequeo si gané
        if casillas_completadas_en_carton == len(carton):
            return jugadas
    return -1 # Caso imposible?


q = Queue()
q.put(30)







# Ejercicio 19:
def agruparPorLongitud(nombre_archivo_input: str) -> dict:
    
    # Abro archivo de input:
    archivo_input = open(nombre_archivo_input, "r")
    
    result: dict = ()
    for linea in archivo_input.readlines():
            for palabra in linea.split():
                if len(palabra) not in result:    
                    result[len(palabra)] = 1
                else:
                    result[len(palabra)] += 1
                    
    archivo_input.close()
    return result

print(agruparPorLongitud("Ejercicio19.txt"))





# Ejercicio 21:
def laPalabraMasFrecuente(nombre_archivo_input: str) -> str:
    archivo_input = open(nombre_archivo_input, "r")
    
    palabra_apariciones: dict = {}
    for linea in archivo_input.readlines():
        for palabra in line.split():
            if palabra not in palabra_apariciones:
                palabra_apariciones[palabra] = 1
            else:
                palabra_apariciones[palabra] += 1
                
    palabra_con_mas_apariciones, maxima_apariciones = " ", 0
    for palabra, apariciones in palabra_apariciones.items():
        if apariciones > maxima_apariciones:
            palabra_con_mas_apariciones = palabra
            maxima_apariciones = apariciones
            
    archivo_input.close()
    return palabra_con_mas_apariciones



print(laPalabraMasFrecuente("ejercicio_19.txt"))
