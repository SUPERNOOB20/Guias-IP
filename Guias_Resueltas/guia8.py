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


# Test cases:
# print(existe_palabra("trigo", "tres_tristes_tigres.txt"))
# print(existe_palabra("tirgo", "tres_tristes_tigres.txt"))

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
# print(cantidad_apariciones("tres_tristes_tigres.txt", "tigres"))


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
# clonarSinComentarios("ejemploComentado2.txt")


# print(clonarSinComentarios("ejemploComentado2.txt"))     <--- NO hacer esto.

### Ejercicio 3:
from queue import LifoQueue as Pila

def reverso(nombre_archivo: str) -> str:
    archivo = open(nombre_archivo, "r")

    nombre_archivo_copia: str = "reverso.txt"
    archivo_copia = open(nombre_archivo_copia, "w")

    pila: Pila = Pila()
    for linea in archivo:
        pila.put(linea)

    while pila.qsize() > 0:
        elemento_cola = pila.get()
        archivo_copia.write(elemento_cola)

    archivo.close()
    archivo_copia.close()

    return archivo_copia

# Test case:
# print(reverso("tres_tristes_tigres.txt"))

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
    archivo = open(archivo_binario, mode='rb')
    leer_archivo = archivo.read()
    # print(leer_archivo)
    # print(len(leer_archivo))
    palabrasLegibles: list = []
    palabraLegible: str = ""
    for byte in leer_archivo:
        caracter_legible = chr(byte)
        # print(caracter_legible)
        if caracter_legible.isalnum() or caracter_legible in [" ", "_"]:
            palabraLegible += caracter_legible
        else:
            if len(palabraLegible) >= 5:     # O "while"; es lo mismo.
                palabrasLegibles.append(palabraLegible)
            palabraLegible = ""
    archivo.close()
    return palabrasLegibles

"""
# Test cases (Cuidado - ¡tardan un ratito!):
print(binarioLegible("Last Remote ~ Type A Personality.mp3"))
print(binarioLegible("nolemretaw umieR.jpg"))
print(binarioLegible("BillyTheBard11th - Excuse My Rudeness, But Could You Please RIP [Metal Cover] - copia.zip"))
print(binarioLegible("東方紅魔郷"))
"""



### Ejercicio 7:
def promedio_estudiante1(legajo: str, LU: str) -> float:
    file_notas_alumnos: str = open("notas.csv", "r")
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



def promedio_estudiante2(archivo_notas: str, LU: str) -> float:
    file_notas_alumnos: str = open("C:/Users/SUPERNOOB20/Documents/UBA/FCEN/2023/IP_2/Practicas/Guia8/notas.csv", "r")
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



# from queue import LifoQueue as Pila

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

# Test case:
# print(generaNumerosRandom(10,1,100))


### Ejercicio 9:
def cantidad_elementos(p: Pila) -> int:                                  # Donde "p" es de tipo *** IN ***
    lista_apilada: list = []
    while not p.empty():
        lista_apilada.append(p.get())
    res = len(lista_apilada)
    lista_apilada.reverse()
    while len(lista_apilada) > 0:
        p.put(lista_apilada[0])
        lista_apilada.remove(lista_apilada[0])
    return res


# Test case - pila [1,2,3,1000]:
"""
pilaEj19: Pila = Pila()
pilaEj19.put(1)
pilaEj19.put(2)
pilaEj19.put(3)
pilaEj19.put(1000)

cantidad_elementos(pilaEj19)
print(list(pilaEj19.queue), cantidad_elementos(pilaEj19), list(pilaEj19.queue))
"""



### Ejercicio 10:

"""
# Forma 1 (la mía) (funciona solo con "p" como *** INOUT *** :c):
def buscarElMaximo1(p: Pila) -> int:                                    # Donde "p" es de tipo *** IN ***
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

    reviertePila: Pila = Pila()
    while not p.empty():
        print("PIJa")
        elemento = p.get()
        reviertePila.put(elemento)
    p = reviertePila

    return maximo
"""


# Forma 2 (del profe):
def buscarElMaximo2 (p: Pila) -> int:
    p_copia: Pila = copiaPilaProfe(p)
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

def copiaPilaProfe(p: Pila) -> Pila:        # !!!!!!
    elements: [int] = []
    while not p.empty():
        elements.append(p.get())
    p_copy: Pila = Pila()
    for i in range(len(elements) - 1, -1, -1):      # Recorrre la lista "elements" en sentido inverso.
        p.put(elements[i])
        p_copy.put(elements[i])
    return p_copy

# ¡MI forma de copiar una pila!:
"""
def copiaCola(p: Cola) -> Cola:     # Copia la cola p en una nueva cola (p2) y devuelve esta última.
    lista_a_copiar: list = []
    p2: Cola = Cola()               # Inicializo p2
    while not p.empty():
        lista_a_copiar.append(p.get())
    for elemento in range(len(lista_a_copiar) - 1, -1, -1):
    # for elemento in range(0, len(lista_a_copiar)):
        p.put(lista_a_copiar[elemento])
        p2.put(lista_a_copiar[elemento])
    return p2
"""


## TEST CASES:

# Test case - [1,7,4,5]:
pila: Pila = Pila()
pila.put(1)
pila.put(7)
pila.put(4)
pila.put(5)

print("ANTES:", list(pila.queue))

# print(buscarElMaximo1(pila), "[1,7,4,5]")
# print(list(pila.queue))
# print(list(p.queue))
print(buscarElMaximo2(pila), "[1,7,4,5]")

print("DESPUÉS:", list(pila.queue))

# Test case - [7,2,8,7]:
pilaEj10: Pila = Pila()
p.put(7)
p.put(2)
p.put(8)
p.put(7)

print("ANTES:", list(p.queue))

# print(buscarElMaximo1(p), "[7,2,8,7]")
print(buscarElMaximo2(p), "[7,2,8,7]")
# Debería devolver ** 8 **: funciona bien :]

print("DESPUÉS:", list(p.queue))


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






### Ejercicio 12:

# ADVERTENCIA: ¡Todavía no está fixeado para números de 2 o más cifras!
def resuelvePostfix(formula: str) -> float:
    operadores: list = ["+", "-", "*", "/"]
    procesaCaracteres: Pila = Pila()               # Inicializa una pila para poder llevar anotadas las cuentas.
    procesaOperaciones: Pila = Pila()              # Inicializa una pila para poder operar matemáticamente dentro de ella.
    # print("formula1:", formula)
    formula = formula.replace(" ","")
    # print("formula2:", formula)
    alumrof = formula[::-1]
    for char in alumrof:
        procesaCaracteres.put(char)
    # print("formula:", formula)
    # print("alumrof:", alumrof)
    # print("procesaCaracteres: ", list(procesaCaracteres.queue))
    # print("procesaOperaciones:", list(procesaOperaciones.queue))
    while procesaCaracteres.qsize() >= 1:
        caracter = procesaCaracteres.get()                    # token: "el caracter es un OPERADOR".
        if caracter in operadores:
            a = float(procesaOperaciones.get())
            b = float(procesaOperaciones.get())
            if caracter == "+":
                resAtomico = b + a
            if caracter == "-":
                resAtomico = b - a
            if caracter == "*":
                resAtomico = b * a
            if caracter == "/":
                resAtomico = b / a
            procesaCaracteres.put(resAtomico)
        elif procesaCaracteres.qsize() == 0 and caracter not in operadores:
            # print("good ending:", list(procesaCaracteres.queue))
            # print("resultadooo:", caracter)
            return caracter
        else:                                   # token: "el caracter es un OPERANDO".
            procesaOperaciones.put(caracter)
    # print("bad ending:", list(procesaCaracteres.queue))
    return procesaCaracteres.get()





# Con la ayuda de Santiago Ibañez (¡este SÍ anda bien!):
from queue import Queue as Cola

def resuelvePostfix_Santi(formula: str) -> float:
    cola: Cola = Cola()

    res: str = formula                 # NO queremos modificar "formula" - ¡es de tipo ** IN **!
    numeroTemp: str = ""
    for i in res: 
        if i.isnumeric():
            numeroTemp += i
            res = res.replace(i, "", 1)
        if i == " " and numeroTemp != "":
            cola.put(numeroTemp)
            numeroTemp: str = ""
        if i == "+":
            cola.put(float(cola.get())+float(cola.get()))
            print(list(cola.queue))
        if i == "-":
            cola.put(float(cola.get())-float(cola.get()))
        if i == "*":
            cola.put(float(cola.get())*float(cola.get()))
        if i == "/":
            cola.put(float(cola.get())/float(cola.get()))

    return cola.get()

# Test case (¡extraído del enunciado!)
expresion = "3 4 + 5 * 2 -"
resultado = resuelvePostfix(expresion)
resultado_s = resuelvePostfix_Santi(expresion)

print("(" + expresion + ")      ", "Mi resolucion (usa 2 pilas):", resultado, "              (" + expresion + ")") # Debería devolver 33.
print("(" + expresion + ")      ", "Resolucion de Santi (usa 1 cola):", resultado_s, "              (" + expresion + ")") # Debería devolver 33.

# Test case (inventado):
expresion2 = "71 2005 + 2 *"
resultado2 = resuelvePostfix(expresion2)
print(expresion2)
resultado2_s = resuelvePostfix_Santi(expresion2)

print("(" + expresion2 + ")      ", "Mi resolucion (usa 2 pilas):", resultado2, "              (" + expresion2 + ")") # Debería devolver 4152.
print("(" + expresion + ")      ", "Resolucion de Santi (usa 1 cola):", resultado2_s, "              (" + expresion2 + ")") # Debería devolver 4152.





##### COLAS #####

# from queue import Queue as Cola

c: Cola = Cola()             # Inicia la cola (constructor)
c.put(1)                     # Encolar
elemento = c.get()           # Desencolar ()
c.empty()                    # Devuelve True si la pila "p" está vacia. Si no, devuelve False.



### Ejercicio 13:
from random import randint


def generaNumerosRandom_COLA(n: int, desde: int, hasta: int) -> Cola:         # Donde todos los parámetros de entrada son de tipo *** IN ***
    colaOutput: Cola = Cola()
    while n > 0:
        numeroAleatorio = randint(desde, hasta)
        colaOutput.put(numeroAleatorio)
        n -= 1
    print(list(colaOutput.queue))
    return colaOutput

"""
# Test case:
print(generaNumerosRandom(10,1,100))
print(generaNumerosRandom_COLA(10,1,100))
"""

# Comparando el Ejercicio 8 (pila/Pila) y el Ejercicio 13 (cola/FIFOqueue), ¿son... lo mismo? No lo sé... @.@






### Ejercicio 14:
def cantidad_elementos (c: Cola) -> int:           # Donde c es de tipo *** IN ***.
    contador_de_elementos: int = 0
    print("c: ", list(c.queue))
    c_copia: Cola = Cola()                         # Inicializo una futura copia de c para restaurar c antes de terminar la función (recordemos que "c" debe ser de tipo *** IN ***).

    while not c.empty():
        c_copia.put(c.get())
        contador_de_elementos += 1

    print("c: ", list(c.queue))

    while not c_copia.empty():
        c.put(c_copia.get())



    return contador_de_elementos


"""
# Test case:
colaEj14: Cola = Cola()
colaEj14.put(7)
colaEj14.put(2)
colaEj14.put(7)
colaEj14.put("WYSI")
colaEj14.put("WHEN YOU FUCKING SEE IT")

print("ANTES:", list(colaEj14.queue))
print("colaEj14 tiene", cantidad_elementos(colaEj14),"elementos.")
print("DESPUÉS:", list(colaEj14.queue))
"""





### Ejercicio 15:

# Forma 1 (la mía) (funciona solo con "c" como *** INOUT *** :c)
"""
def buscarElMaximo_COLA_1(c: Cola) -> int:                                    # Donde "p" es de tipo *** IN ***
    lista_de_la_cola: list = []
    maximo: int = 72727
    while not c.empty():
        numerito = c.get()
        lista_de_la_cola.append(numerito)
    # print(str(lista_de_la_pila))
    lista_de_la_cola_COPIA: list = lista_de_la_cola.copy()
    for elemento in lista_de_la_cola_COPIA:
        c.put(elemento)
    # print(list(p.queue))
    maximo = max(lista_de_la_cola)
    return maximo
"""


# Forma 2 (del profe):
def buscarElMaximo_COLA_2 (c: Cola) -> int:
    c_copia: Queue() = copiaCola(c)
    while not c_copia.empty():        # p.qsize() > 1:
        a = c_copia.get()
        if c_copia.empty():
            return a
        b = c_copia.get()
        if a > b:
            c_copia.put(a)
        else:
            c_copia.put(b)
    
    # c_copia2: Pila() = ()


    # while not c.empty():
      #   c_copia2.put(c_copia.get())
        


    return c_copia.get()

def copiaCola(p: Cola) -> Cola:     # Copia la cola p en una nueva cola (p2) y devuelve esta última.
    lista_a_copiar: list = []
    p2: Cola = Cola()               # Inicializo p2
    while not p.empty():
        lista_a_copiar.append(p.get())
    for elemento in lista_a_copiar:
    # for elemento in range(0, len(lista_a_copiar)):
        p.put(elemento)
        p2.put(elemento)
    return p2



###### Testeo de "copiaCola":
copiameEsta: Cola = Cola()
copiameEsta.put(1)
copiameEsta.put(2)
copiameEsta.put(3)

print("\nEMPIEZA TESTEO\n")
print("ANTES:", list(copiameEsta.queue))

print(list(copiaCola(copiameEsta).queue))

print("DESPUES: ", list(copiameEsta.queue))
print("\nFIN TESTEO\n")



## TEST CASES:

# Test case - [1,7,4,5]:
colaEj15: Cola = Cola()
colaEj15.put(1)
colaEj15.put(7)
colaEj15.put(4)
colaEj15.put(5)

print("ANTES:", list(colaEj15.queue))

# print(buscarElMaximo1(colaEj15), "[1,7,4,5]")
print(buscarElMaximo_COLA_2(colaEj15), "[1,7,4,5]")

print("DESPUÉS:", list(colaEj15.queue))

# Test case - [7,2,8,7]:
c15: Cola = Cola()
c15.put(7)
c15.put(2)
c15.put(8)
c15.put(7)

print("ANTES:", list(c15.queue))

# print(buscarElMaximo1(c15), "[7,2,8,7]")
print(buscarElMaximo_COLA_2(c15), "[7,2,8,7]")
# Debería devolver ** 8 **: funciona bien :]

print("DESPUÉS:", list(c15.queue))

print("gud ending          a")

######### CONCLUSIÓN: La diferencia entre el ejercicio 10 y el ejercicio 15 es que...
# ... para el ejercicio 15, hay que invertir la fila, porque "Queue" (la cola) es de tipo "FIFO" :]



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






# Ejercicio 17:
def n_pacientes_urgentes(c: Cola[(int, str, str)]) -> int:
    c2: Cola[(int, str, str)] = copiaCola(c)           # Inicializa una copia de c (¡recordemos que "c" es de tipo *** IN *** !)
    contador_de_urgentes: int = 0
    
    while not c2.empty():
        paciente = c2.get()
        if paciente[0] in [1,2,3]:
            contador_de_urgentes += 1
        
        
    return contador_de_urgentes

"""
# Test case (mío):
colaPacientes: Cola[(int, str, str)] = Cola()
colaPacientes.put((1, "pepe", "chotología"))
colaPacientes.put((8, "alfredo", "pediatría"))
colaPacientes.put((3, "tu vieja", "quimioterapia"))
colaPacientes.put((2, "pepa", "ginecología"))

print(list(colaPacientes.queue))

print(n_pacientes_urgentes(colaPacientes))
# (Debería dar 3)



# Test case de "nardos322":
pacientes = Queue()
pacientes.put((1,'n','cirujia'))
pacientes.put((6,'a','otorrino'))
pacientes.put((4,'x','dermatologo'))
pacientes.put((3,'y','oftalmologia'))
pacientes.put((3,'y','oftalmologia'))
print(list(pacientes.queue))
print(n_pacientes_urgentes(pacientes))
"""





## Ejercicio 18.1: (En el cuadernillo de IP)
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


### Ejercicio 20 (NOTA: Este ejercicio está relacionado con el ejercicio 7):


# Idea: hacer un diccionario "dict {str : list[float]}" con todas las notas y luego recorrer todas las keys y asignarles...
# ... el promedio de cada list[float] :D

def promedio_estudiante20(archivo_notas: str, LU: str) -> float:
    file_notas_alumnos: str = open(archivo_notas, "r")
    notas_alumnos: list = []
    notas_del_alumno: list = []
    diccionarioLista: dict[str, list[float]] = {}
    diccionarioPromedios: dict[str, float] = {}
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


print(promedio_estudiante2("notas.csv", "937/21"))


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

# Test case:
# print(laPalabraMasFrecuente("PRII.txt"))





### Ejercicio 22:

sitiosWebSacados: dict[str, Pila] = {}



## Ejercicio 22.1:
historiales: dict[str, Pila] = {}

## Ejercicio 22.2:
def visitar_sitio(historiales: dict[str, Pila], usuario: str, sitio: str) -> dict[str, Pila]:         # Devuelve un nuevo historial
    nuevo_sitio: Pila = Pila()      # Inicializo una nueva pila (para luego ponerla en el diccionario).
    nuevo_sitio.put(sitio)
    historiales[usuario] = nuevo_sitio
    # print(list(nuevo_sitio.queue))
    return historiales

## Ejercicio 22.3:
def navegar_atras(historiales: dict[str, Pila], usuario: str) -> dict[str, Pila]:        # Saca el sitio web actual del historial.    
    sacar = historiales.get(usuario)            # sacar es un "value" (la key es **usuario**)
    sitiosWebSacados[usuario] = sacar
    return

## Ejercicio 22.4:
def navegar_adelante(historiales: dict[str, Pila], usuario: str) -> dict[str, Pila]:        # Vuelve a agregar el sitio web sacado al historial.
    poner = sitiosWebSacados.get(usuario)       # poner es un "value" (la key es **usuario**)
    historiales[usuario] = poner
    return


# print(visitar_sitio({},'Guest', 'www.campusexactas.com.ar'))

# Test cases (¡los que están en el enunciado!):
# historiales = {}
"""
visitar_sitio(historiales, "Usuario1", "google.com")
visitar_sitio(historiales, "Usuario1", "facebook.com")
navegar_atras(historiales, "Usuario1")
visitar_sitio(historiales, "Usuario2", "youtube.com")
navegar_adelante(historiales, "Usuario1")

print(historiales)
print(sitiosWebSacados)

def ver_diccionario(historial) -> None:
    for usuario, paginas in historial.items():
        print(f"Usuario: {usuario}, Historial: {paginas.queue}")

print(ver_diccionario(historiales))
print(ver_diccionario(sitiosWebSacados))
"""





# Ejercicio 23.1:
def agregar_producto(inventario: dict[str, dict[float, int]], nombre: str, precio: float, cantidad: int):    # Requiere: "nombre" no está en "inventario"
    print(nombre, cantidad)
    productos: dict[float,int] = {}       # Inicializo el diccionario que estará como "value"
    productos[precio] = cantidad
    inventario[nombre] = productos
    productos = {}                        # Vacío el diccionario que usé como "value"
    print(nombre, cantidad)
    return

# Ejercicio 23.2:
def actualizar_stock(inventario, nombre, cantidad):
    for key in inventario:
        if key == nombre:
            key_previa = inventario[key]
            for stock in key_previa:
                key_previa[stock] = cantidad
    
    return

# Ejercicio 23.3:
def actualizar_precios(inventario, nombre, precio):
    # print("inventariooo:", inventario)
    for key in inventario:
        if key == nombre:
            key_previa = inventario[key]
            print("inventario[key] =", inventario[key])
            for k, v in key_previa.items():
                key_previa.clear()
                key_previa[precio] = v
            print(key_previa)
    # print("inventariooo:", inventario)
    return

# Ejercicio 23.4:
"""
def calcular_valor_inventario_forma1(inventario):
    valorTotal: float = 0.0
    for key in inventario:
        valorTotal += (list(inventario[key].items()))[0][0] * (list(inventario[key].items()))[0][1]
            
    return valorTotal
"""

def calcular_valor_inventario(inventario):
    valorTotal: float = 0.0
    for key in inventario:
        for k, v in inventario[key].items():
            valorTotal += k * v
            
    return valorTotal



##### TEST CASE:

inventario = {}
# print(inventario)
agregar_producto(inventario, "Camisa", 20.0, 50)
agregar_producto(inventario, "Pantalón", 30.0, 30)
# print("inventario viejo:", inventario)
actualizar_stock(inventario, "Camisa", 10)
# print("inventario nuevo:", inventario)
valor_total = calcular_valor_inventario(inventario)

print("Valor total del inventario:", valor_total)           # Debería imprimir 1300.0

actualizar_precios(inventario, "Camisa", 50.0)

valor_total = calcular_valor_inventario(inventario)
print("Valor total del inventario:", valor_total)           # Debería imprimir... ¿1800.0?

#####






print("Llegamos al final del código :]")
