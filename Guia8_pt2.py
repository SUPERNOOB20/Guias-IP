# Ejercicio 6:
# def binarioLegible() ->
# chr(byte)


# Ejercicio banco:

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

print(a_clientes(clientes_cola))



# Ejercicio 11:
def esta_bien_balanceada(s: str) -> bool:
    brackets: list = []
    for i in s:
        if i == "(" or i == ")":
            brackets.append(i)
    return (brackets[0] == "(") and (cantidadDeApariciones("(", brackets) == cantidadDeApariciones("(", brackets)) and (brackets[(len(brackets)) - 1] == ")")

def cantidadDeApariciones(e: str, s: list) -> int:
    contadorApariciones: int = 0
    s2 = s.copy()
    while e in s2:
        contadorApariciones += 1
        s2.remove(e)
    return contadorApariciones


# TEST CASES:
print(esta_bien_balanceada("1 + (2 * 3 - (20 / 5))"))        # Debería dar True
print(esta_bien_balanceada("10 * ( 1 + ( 2 * (-1)))"))       # Debería dar True
print(esta_bien_balanceada("1 + ) 2 * 3 ( ()"))              # Debería dar False
print(esta_bien_balanceada("1 + ()"))                        # Debería dar False. Tip: probar a implementar algo que cuando encuentre "(" y después ")", halla un "isnumeric()" en el medio





# Ejercicio 7:
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



def promedio_estudiante2(legajo: str, LU: str) -> float:
    file_notas_alumnos: str = open("notas.csv", "r")
    notas_alumnos: list = []
    notas_del_alumno: list = []
    for linea in file_notas_alumnos:
        print("la linea es", linea)
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



promedio_estudiante1("notas.csv", "937/21")
promedio_estudiante2("notas.csv", "937/21")



##### Pilas #####

## Recuerdo:
# FIFO queue == Queue     == Cola
# LIFO queue == LIFOQueue == Pila



from queue import LifoQueue as Pila

p = Pila()              # Inicia la pila (constructor)
p.put(1)                # Apilar
elemento = p.get()      # Desapilar
p.empty()               # Devuelve True si la pila "p" está vacia. Si no, devuelve False.





# Ejercicio 8:
def generaNumerosRandom(n: int, desde: int, hasta: int) -> Pila:         # Donde todos los parámetros de entrada son de tipo *** IN ***
    return




# Ejercicio 9:
def cantidad_elementos(p: Pila) -> int:                                  # Donde "p" es de tipo *** IN ***
    return



# Ejercicio 10:


def buscar_el_maximo(p: Pila) -> int:                                    # Donde "p" es de tipo *** IN ***
    lista_de_la_pila: list = []
    maximo: int = 72727
    while not p.empty():
        numerito = p.get()
        lista_de_la_pila.append(numerito)
    print(str(lista_de_la_pila))
    lista_de_la_pila_COPIA: list = lista_de_la_pila.copy()
    for elemento in lista_de_la_pila_COPIA:
        p.put(elemento)
    print(list(p.queue))
    return maximo


pilaEj10 = Pila()
p.put(7)
p.put(2)
p.put(8)
p.put(7)
buscar_el_maximo(p)
