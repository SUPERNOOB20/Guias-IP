## Ejercicio 1.1:
def contar_lineas(nombre_archivo: str) -> int:      # Donde "nombre_archivo" es de tipo *** IN ***.
    archivo = open(nombre_archivo, "r")
    cantidad_lineas: int = 0
    for linea in archivo:
        cantidad_lineas += 1
    return cantidad_lineas


## Ejercicio 1.2:

def existe_palabra(palabra: str, nombre_archivo: str) -> bool:      # "palabra" y "nombre_archivo" son de tipo *** IN ***.
    archivo = open(nombre_archivo, "r")
    for linea in archivo:
        if palabra in linea:
            return True
    return False

print(existe_palabra("trigo", "tres_tristes_tigres.txt"))
print(existe_palabra("tirgo", "tres_tristes_tigres.txt"))

## Ejercicio 1.3:
def cantidad_apariciones(nombre_archivo: str, palabra: str) -> int:                  # "nombre_archivo" y "palabra" son de tipo *** IN ***.
    archivo = open(nombre_archivo, "r")
    archivo_copia = archivo
    cantidad_apariciones: int = 0
    for linea in archivo_copia:
        while palabra in linea:
            linea = linea.replace(palabra, "", 1)
            cantidad_apariciones += 1
    return cantidad_apariciones

# Test case:
print(cantidad_apariciones("tres_tristes_tigres.txt", "tigres"))


### Ejercicio 2:
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

### Ejercicio 3:
from queue import LifoQueue

def reverso(nombre_archivo: str) -> str:
    archivo = open(nombre_archivo, "r")

    nombre_archivo_copia: str = "reverso.txt"
    archivo_copia = open(nombre_archivo_copia, "w")

    cola: LifoQueue = LifoQueue()
    for linea in archivo:
        cola.put(linea)

    while cola.qsize() > 0:
        elemento_cola = cola.get()
        archivo_copia.write(elemento_cola)

    archivo.close()
    archivo_copia.close()

    return archivo_copia

print(reverso("tres_tristes_tigres.txt"))

### Ejercicio 4:
def agregaAlFinal(nombre_archivo: str, frase: str) -> str:
    archivo = open(nombre_archivo, "w")
    for linea in range(len(archivo) - 1, len(archivo), 1):
        archivo[linea] = archivo[linea] + "\n" + frase
    archivo.close()
    return archivo

### Ejercicio 5:
def agregaAlPrincipio(nombre_archivo: str, frase: str) -> str:
    archivo = open(nombre_archivo, "w")
    for linea in range(0, 1, 1):
        archivo[linea] = frase + "\n" + archivo[linea]
    archivo.close()
    return archivo

### Ejercicio 6
def binarioLegible(archivo_binario: str) -> list:
    archivo = open(archivo_binario, "b")
    archivo.close()
    return
# chr(byte)

### Ejercicio 7:

# FORMA 1:
def promedio_estudiante1(archivo_notas: str, LU: str) -> float:
    file_notas_alumnos: str = open(archivo_notas, "r")
    notas_alumnos: list = []
    notas_del_alumno: list = []
    for linea in file_notas_alumnos:
        print("la linea es", linea)
        spliteada = linea.split()
        # spliteada = linea.strip("\n")
        # while '' in spliteada:
            # spliteada.remove('')
        notas_alumnos.append(spliteada)
        if LU in linea:
            notas_del_alumno.append(spliteada[len(spliteada) - 1])
    print("las notas son", str(notas_alumnos))
    print("las notas del alumno", LU, "son", str(notas_del_alumno))         
    return


# FORMA 2:
def promedio_estudiante2(archivo_notas: str, LU: str) -> float:
    file_notas_alumnos: str = open(archivo_notas, "r")
    notas_alumnos: list = []
    notas_del_alumno: list = []
    for linea in file_notas_alumnos:
        # print("la linea es", linea)
        spliteada = linea.strip("\n")
        spliteada = spliteada.split(", ")
        # while '' in spliteada:
            # spliteada.remove('')
        notas_alumnos.append(spliteada[len(spliteada) - 1])
        if LU in linea:
            notas_del_alumno.append(spliteada[len(spliteada) - 1])
    print("las notas son", str(notas_alumnos))
    print("las notas del alumno", LU, "son", str(notas_del_alumno))         
    return



# promedio_estudiante1("notas.csv", "937/21")
# promedio_estudiante2("notas.csv", "937/21")



##### Pilas #####

## Recuerdo:
# FIFO queue == Queue     == Cola
# LIFO queue == LIFOQueue == Pila



from queue import LifoQueue as Pila

p: Pila = Pila()              # Inicia la pila (constructor)
p.put(1)                      # Apilar
elemento = p.get()            # Desapilar
p.empty()                     # Devuelve True si la pila "p" está vacia. Si no, devuelve False.





### Ejercicio 8:
from random import randint


def generaNumerosRandom(n: int, desde: int, hasta: int) -> Pila:         # Donde todos los parámetros de entrada son de tipo *** IN ***
    pilaOutput: Pila = Pila()
    while n > 0:
        numeroAleatorio = randint(desde, hasta)
        pilaOutput.put(numeroAleatorio)
        n -= 1
    print(list(pilaOutput.queue))
    return pilaOutput

print(generaNumerosRandom(10,1,100))


### Ejercicio 9:
def cantidad_elementos(p: Pila) -> int:                                  # Donde "p" es de tipo *** IN ***
    return



### Ejercicio 10:

# Forma 1 (la mía):
def buscar_el_maximo1(p: Pila) -> int:                                    # Donde "p" es de tipo *** IN ***
    lista_de_la_pila: list = []
    maximo: int = 72727
    while not p.empty():
        numerito = p.get()
        lista_de_la_pila.append(numerito)
    # print(str(lista_de_la_pila))
    lista_de_la_pila_COPIA: list = lista_de_la_pila.copy()
    for elemento in lista_de_la_pila_COPIA:
        p.put(elemento)
    # print(list(p.queue))
    maximo = max(lista_de_la_pila)
    return maximo



# Forma 2 (del profe):
def buscarElMaximo2 (p: LifoQueue) -> int:
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

## TEST CASES:

# Test case - [1,7,4,5]:

"""
pila: LifoQueue = LifoQueue()
pila.put(1)
pila.put(7)
pila.put(4)
pila.put(5)

buscarElMaximo(pila)
print(buscarElMaximo1(pila), "[1,7,4,5]")
print(buscarElMaximo2(pila), "[1,7,4,5]")


# Test case - [7,2,8,7]:
pilaEj10: Pila = Pila()
p.put(7)
p.put(2)
p.put(8)
p.put(7)
print(buscar_el_maximo(p))
# Debería devolver ** 8 **: funciona bien :]
"""



### Ejercicio 11:
def esta_bien_balanceada(s: str) -> bool:
    brackets: list = []
    for i in s:
        if i == "(" or i == ")":
            brackets.append(i)
    return (brackets[0] == "(") and (cantidadDeApariciones("(", brackets) == cantidadDeApariciones("(", brackets)) and (brackets[(len(brackets)) - 1] == ")") and (not "()" in s)

def cantidadDeApariciones(e: str, s: list) -> int:
    contadorApariciones: int = 0
    s2 = s.copy()
    while e in s2:
        contadorApariciones += 1
        s2.remove(e)
    return contadorApariciones

"""
# TEST CASES:
print(esta_bien_balanceada("1 + (2 * 3 - (20 / 5))"))        # Debería dar True
print(esta_bien_balanceada("10 * ( 1 + ( 2 * (-1)))"))       # Debería dar True
print(esta_bien_balanceada("1 + ) 2 * 3 ( ()"))              # Debería dar False
print(esta_bien_balanceada("1 + ()"))                        # Debería dar False.                   NO ----> Tip: probar a implementar algo que cuando encuentre "(" y después ")", halla un "isnumeric()" en el medio
print(esta_bien_balanceada("1 + (())"))                      # Debería dar False
print(esta_bien_balanceada("1 + (()())"))                    # Debería dar False
"""





##### COLAS #####

from queue import Queue as Cola

c: Cola = Cola()             # Inicia la cola (constructor)
c.put(1)                     # Encolar
elemento = c.get()           # Desencolar ()
c.empty()                    # Devuelve True si la pila "p" está vacia. Si no, devuelve False.




### Ejercicio 13:




## Ejercicio 16.1:
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


## Ejercicio 16.2:
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
for i in range(0,12):
    cartonBingo.append(q.get())
# print(cartonBingo)

a = list(range(0,100))

bolillero: Queue = Queue()
# bolillero = np.random.shuffle(a)      <--- NO

for i in range(0,len(a)):
    bolillero.put(a[i])

######## print(jugarCartonDeBingo(cartonBingo, bolillero))



"""
print(bolillero)
print(bolillero)
print(bolillero)
"""
# print(a)



## Ejercicio 18.2:

# str ---> Nombre y Apellido
# int ---> DNI
# bool ---> tipo de cuenta  (¿Tiene cuenta bancaria preferencial?)
# bool ---> ¿Tiene prioridad?

from queue import Queue

def a_clientes(clientes_cola: Queue) -> Queue:
    cola_de_atencion: Queue = Queue()
    lista_clientes: list = []
    
    while not clientes_cola.empty():
        lista_clientes.append(clientes_cola.get())
    # print(lista_clientes)
    for i in range(0, len(lista_clientes)):
        if lista_clientes[i][3] == True:
            clientePrio = lista_clientes[i]
            cola_de_atencion.put(clientePrio)
            lista_clientes[i] = "BORRAR"
            # lista_clientes.remove(clientePrio)
            print("ok")
    while "BORRAR" in lista_clientes:
        lista_clientes.remove("BORRAR")
    for i in range(0, len(lista_clientes)):
        if lista_clientes[i][2] == True:
            clientePref = lista_clientes[i]
            cola_de_atencion.put(clientePref)
            # lista_clientes.remove(clientePref)
            lista_clientes[i] = "BORRAR"
            print("recontraok")
    while "BORRAR" in lista_clientes:
        lista_clientes.remove("BORRAR")
    for i in range(0, len(lista_clientes)):
        cola_de_atencion.put(lista_clientes[i])
        print("wat")
    print(list(cola_de_atencion.queue))
    return cola_de_atencion


clientes_cola: Queue = Queue()
clientes_cola.put(("cuarto", 1, True, False))
clientes_cola.put(("quinto", 4, False, False))
clientes_cola.put(("primero2", 2, True, True))
clientes_cola.put(("primero1", 5,True, True))
clientes_cola.put(("primero3", 4, False, True))

# print(a_clientes(clientes_cola))

while not clientes_cola.empty():
    clientes_cola.get()



### Ejercicio 19:
def agruparPorLongitud(nombre_archivo: str) -> dict:
    archivo = open(nombre_archivo,"r", encoding = "utf8")
    diccionarioOutput: dict = {}            # Inicializo el diccionario a devolver
    
    for linea in archivo.readlines():       # Separo el archivo en líneas
        palabras = linea.split()            # Separo cada línea: Ln8:"hola que tal" ---> ["hola", "que", "tal"]
        for palabra in palabras:
            palabra = palabra.strip("()[]{},.;:")
            if palabra in diccionarioOutput:
                diccionarioOutput[palabra] += 1
            else:
                diccionarioOutput[palabra] = 1


    archivo.close()

    return diccionarioOutput

# print(agruparPorLongitud("PRII.txt"))





### Ejercicio 21:

def laPalabraMasFrecuente(nombre_archivo: str) -> str:
    archivo = open(nombre_archivo,"r", encoding = "utf8")
    diccionario: dict = {}                  # Inicializo un diccionario a usar
    
    for linea in archivo.readlines():       # Separo el archivo en líneas
        palabras = linea.split()            # Separo cada línea: Ln8:"hola que tal" ---> ["hola", "que", "tal"]
        for palabra in palabras:
            palabra = palabra.strip("()[]{},.;:")
            if palabra in diccionario:
                diccionario[palabra] += 1
            else:
                diccionario[palabra] = 1

    # listaValores: list = []
    # for clave, valor in diccionario:
        # listaValores.append[valor]
    # listaValores.append(diccionario.values())
    a = max(diccionario.values())
    # print(diccionario.values())
    # print(a)
    for clave in diccionario:
        if diccionario[clave] == a:
            return clave
    return # palabraMasFrecuente

print(laPalabraMasFrecuente("PRII.txt"))
