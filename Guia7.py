##### Primera Parte #####

"""
Guía de cómo cargar scripts en Python (para retrasados mentales):
Paso 1: Abrir una terminal desde 0
Paso 2: cd E:\
Paso 3: python
Paso 4: import Guia7 (¡SIN EL ".py"!)
"""

# Ejercicio 1.1
def pertenece1 (s: list, e: int) -> bool:       # "s" es una lista de enteros; "e" es un entero
    for posicion in range(0, len(s)):
        if s[posicion] == e:
            return True
    return False

def pertenece2 (s: list, e: int) -> bool:
    posicion = 0
    while posicion < len(s):
        if s[posicion] == e:
            return True
        posicion += 1
    return False

def pertenece2punto5 (s: list, e: int) -> bool:
    posicion = 0
    while posicion < len(s):
        if s[posicion] == e:
            return True
        else:
            posicion += 1
    return False

from queue import Queue

def pertenece3 (s: list, e: int) -> bool:
    cola: Queue = Queue()

    while len(s) >= 2:          # "Mueve" mi lista "s" a la queue "cola"
        cola.put(s[0])
        s.pop(0)
    s.clear()

    while cola.qsize() != 0:    # ¿Pertenece "e" a "cola"?
        compare: int = cola.get()
        if compare == e:
            return True
    return False
    

# TEST CASES:
"""
print(pertenece1([1,2,3,4,5], 3))
print(pertenece1([1,2,3,4,5], 8))
print(pertenece1([], -2))

print(pertenece2([1,2,3,4,5], 3))
print(pertenece2([1,2,3,4,5], 8))
print(pertenece2([], -2))

print(pertenece2punto5([1,2,3,4,5],3))
print(pertenece2punto5([1,2,3,4,5],8))
print(pertenece2punto5([],-2))

print(pertenece3([1,2,3,4,5],3))
print(pertenece3([1,2,3,4,5],8))
print(pertenece3([],-2))
"""

# Respuesta: Sí se podría implementar esta función con un tipado genérico..
# .. para buscar caracteres dentro de strings..
# .. (siempre y cuando la especificación nos lo permita)




# Ejercicio 1.2:
# (6%3) == 0

def divideATodos (s: list, e: int) -> bool:
    for numero in range(0, len(s)):
        if s[numero] % e != 0:
            return False
    return True

# TEST CASES:
"""
print(divideATodos([0, 5, 10, 1000, 155], 5))
print(divideATodos([], 3))
print(divideATodos([2,4,6,7,8,10], 2))
"""





# Ejercicio 1.3:
def sumaTotal(s: list) -> int:
    acumulador: int = 0
    for i in s:
        acumulador += i
    return acumulador

# TEST CASES:
"""
print(sumaTotal([1,2,3,4,5,6,7,8,9]))
print(sumaTotal([10,20,30,40]))
print(sumaTotal([]))
"""



# Ejercicio 1.4:
def ordenados(s: list) -> bool:
    
    if len(s) == 0:
        return True
    
    for posicion in range(0, len(s) - 1):
        if s[posicion] >= s[posicion + 1]:
            return False
    return True
    
# TEST CASES:
"""
print(ordenados ([1,2,3,4,5]))
print(ordenados ([1,2,3,4,3]))
print(ordenados ([]))
"""




# Ejercicio 1.5:
def algunaMayorA7 (palabras: list) -> bool:
    for palabra in palabras:
        if len(palabras[palabra]) > 7:
            return True
    return False

# Ejercicio 1.6:

# from math import trunc

def esPalindromo(texto: str) -> bool:
    if len(texto) % 2 == 0:         # Caso par.
        for posicionCaracter in range(0, (len(texto) // 2)):
            if texto[posicionCaracter] != texto[len(texto) - posicionCaracter - 1]:
                return False
    else:                           # Caso impar.
        for posicionCaracter in range(0, (len(texto) - 1) // 2):
            print("vamo bien")
            if texto[posicionCaracter] != texto[len(texto) - posicionCaracter - 1]:
                return False
    return True


# Ejercicio 1.7:
def fortalezaContrasenia(contrasenia: str) -> str:
    if (len(contrasenia) > 8) and esUnaContraseniaVariada(contrasenia):
        return "VERDE"
    if len(contrasenia) < 5:
        return "ROJA"
    return "AMARILLA"

def esUnaContraseniaVariada (contra: str) -> bool:
    tieneMinuscula = False
    tieneMayuscula = False
    tieneNumero    = False
    for caracter in contra:
        if caracter in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]:
            tieneMinuscula = True
        if caracter in ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]:
            tieneMayuscula = True
        if caracter in ["0","1","2","3","4","5","6","7","8","9"]:
            tieneNumero = True
    return tieneMinuscula and tieneMayuscula and tieneNumero




# Ejercicio 1.8:
def devuelveSueldoActual(historial: list) -> float:
    saldoActual = 0
    for tupla in historial:
        if tupla[0] == "I":         # Caso "ingresó plata".
            saldoActual -= tupla[1]
        else:                       # Caso "retiró plata".
            saldoActual += tupla[1]
    return saldoActual

# TEST CASE:
# print([("I", 2000), ("R", 20),("R", 1000),("I", 300)])
# ^^^^ ¡Debería devolver 1280! ^^^^                                        âêîôû xd


# Ejercicio 1.9:
vocales: list = ["a","e","i","o","u","A","E","I","O","U","á","é","í","ó","ú","Á","É","Í","Ó","Ú"]

def tiene3OMasVocalesDistintas(palabra: str) -> bool:
    vocalesDistintas: list = []
    for caracter in palabra:
        if caracter in vocales and caracter not in vocalesDistintas:
            vocalesDistintas.append(caracter)
    return len(vocalesDistintas) >= 3

"""
# TEST CASES:
print("Esto debería ser False:",tiene3OMasVocalesDistintas("arbol"))
print("Esto debería ser True:",tiene3OMasVocalesDistintas("dinOsáUriO"))
"""



##### Segunda Parte #####

# Ejercicio 2.1:

def borraPosicionesPares(lista: list) -> list:      # Donde "lista" es un parámetro de tipo *** INOUT ***.
    for posicion in range(1, len(lista), 2):
        lista[posicion] = 0
    return lista

"""
# TEST CASES:
print(borraPosicionesPares([1,2,3,4,5,6,7,8,9]))
print(borraPosicionesPares([]))
print(borraPosicionesPares([727]))
"""

# Ejercicio 2.2:

def devuelvePosicionesPares(lista: list) -> list:      # Donde "lista" es un parámetro de tipo *** IN ***.
    listaDeSalida = lista.copy()
    for posicion in range(1, len(listaDeSalida), 2):
        listaDeSalida[posicion] = 0
    return listaDeSalida

"""
# TEST CASES:

a: list = [1,2,3,4,5,6,7,8,9]
b: list = []
c: list = [727]

print(a, devuelvePosicionesPares(a), a)
print(b, devuelvePosicionesPares(b), b)
print(c, devuelvePosicionesPares(c), c)
"""



# Ejercicio 2.3:

"""
def devuelveSinVocales(cadenaDeChars: str) -> str:
    cadenaOutput = cadenaDeChars.copy()
    for caracter in range(0, len(cadenaOutput), 1):
        if cadenaOutput[caracter] in vocales:
            cadenaOutput.remove(caracter)
    return cadenaOutput

def devuelveSinVocales(cadenaDeChars: str) -> str:
    cadenaOutput: str = cadenaDeChars.strip("aeiouAEIOUáéíóúÁÉÍÓÚ")
    return cadenaOutput
"""

vocales_str: str = "aeiouAEIOUáéíóúÁÉÍÓÚ"

"""
def devuelveSinVocales(cadenaDeChars: str) -> str:          # Donde "cadenaDeChars" es un parámetro de tipo *** INOUT ***.
    for vocal in vocales_str:
        print(vocal)
        cadenaDeChars = cadenaDeChars.replace(vocal, "")
    return cadenaDeChars
"""

def devuelveSinVocales(cadenaDeChars: str) -> str:          # Donde "cadenaDeChars" es un parámetro de tipo *** IN ***.
    cadenaOutput = cadenaDeChars
    for vocal in vocales_str:
        print(vocal)
        cadenaOutput = cadenaOutput.replace(vocal, "")
    return cadenaOutput


"""
# TEST CASE:
cadenaDeChars: str = "holacomoandas"
print(cadenaDeChars, devuelveSinVocales(cadenaDeChars), cadenaDeChars)      # holacomoandas debería devolver hlcmnds
"""


# Ejercicio 2.4:

# Notar que lo implementaremos de forma SUPER SIMILAR al ejercicio anterior:
def reemplazaVocales(s: str) -> str:    # Reemplaza las vocales por el caracter "_"  ;  "s" es de tipo *** IN ***.
    cadenaOutput = s
    for vocal in vocales_str:
        print(vocal)
        cadenaOutput = cadenaOutput.replace(vocal, "_")
    return cadenaOutput

"""
# TEST CASE (idéntico al ejercicio anterior):
cadenaDeChars: str = "holacomoandas"
print(cadenaDeChars, reemplazaVocales(cadenaDeChars), cadenaDeChars)      # "holacomoandas" debería devolver "h_l_c_m__nd_s"
"""


# Ejercicio 2.5:
def daVueltaStr (s: str) -> str:        # "s" es de tipo *** IN ***.
    s_invertido = s [::-1]         # ¡Recordemos que en Python los strings se pasan por copia! (Son un tipo de dato PRIMITIVO).
    return s_invertido

# TEST CASE:
""" print(daVueltaStr("Hola.")) """

# Ejercicio 2.6:


def eliminarRepetidosFOR (s:str) -> str:       # "s" es de tipo *** IN ***.
    s_sin_rep = s
    for caracter in s_sin_rep:
        quitaUnaAparicion: str = s_sin_rep
        quitaUnaAparicion = quitaUnaAparicion.replace(caracter, "", 1)
        if caracter in quitaUnaAparicion:
            s_sin_rep = s_sin_rep.replace(caracter, "", 1)
    return s_sin_rep



def eliminarRepetidosWHILE (s:str) -> str:       # "s" es de tipo *** IN ***.
    s_sin_rep = s
    for caracter in s_sin_rep:
        quitaUnaAparicion: str = s_sin_rep.replace(caracter, "", 1)
        while caracter in quitaUnaAparicion:
            s_sin_rep = s_sin_rep.replace(caracter, "", 1)
            quitaUnaAparicion = quitaUnaAparicion.replace(caracter, "", 1)
            # print(caracter)
            # print(quitaUnaAparicion)
    return s_sin_rep


# Test cases:
"""
textoATestear: str = "HOOOOOOLLLLLLLLLLAAAAAAAAAAAAAAAAAASxd"

print(textoATestear, eliminarRepetidosFOR(textoATestear), textoATestear)
print(textoATestear, eliminarRepetidosWHILE(textoATestear), textoATestear)
"""


# Ejercicio 3:
##### (notas: list, ) -> str:    <--- NO

def aprobado (notas: list[int]) -> int:            # Notar que notas es de tipo *** IN ***.
    res = 1
    promedioTotal = promedio(notas)
    if (min(notas) >= 4) and (4 <= promedioTotal < 7):
        res = 2
    elif (min(notas) < 4) or (promedioTotal < 4):
        res = 3
    return res

def promedio(numeros: list[int]) -> int:
    return (sum(numeros)) // len(numeros)


"""
# Test cases:
Notas1 = [8,4,10,7,10,10,10,10,10]
Notas2 = [0]
Notas3 = [5, 10, 4]

print(Notas1, aprobado(Notas1), Notas1)
print(Notas2, aprobado(Notas2), Notas2)
print(Notas3, aprobado(Notas3), Notas3)
"""


# Ejercicio 4.1:

# NOTA: Anda medio a los ponchazos :c
def armaListaDeEstudiantes() -> list:
    listaDeEstudiantes: list = []
    estudianteUno = input("Ingrese el nombre de un estudiante: ")
    if estudianteUno != "listo":
        listaDeEstudiantes.append(estudianteUno)
        while input() != "listo":
            estudianteDosOMas = input("Ingrese el nombre de otro estudiante: ")
            if estudianteDosOMas != "listo":
                listaDeEstudiantes.append(estudianteDosOMas)
    return listaDeEstudiantes

# Para testear la función, simplemente la invoco:
# print(armaListaDeEstudiantes())

# Ejercicio 4.2:
# Partiendo del ejercicio 1.8 (def "devuelveSueldoActual"):
def devuelveHistorial() -> list:
    monedero = 0
    historial: list = []
    operacion: str = input("Seleccione la operación a realizar: \n (C) Cargar créditos. \n (D) Descontar créditos. \n (X) Finalizar la simulación (termina el programa). \n ")

    while operacion != "X":
        monto: float = float(input("Seleccione el monto de créditos a ingresar/retirar: "))
        historial.append((operacion, monto))
        for tupla in historial:
            if tupla[0] == "C":         # Caso "cargó créditos": "C".
                monedero -= tupla[1]
            else:                       # Caso "descontar créditos": "D".
                monedero += tupla[1]
        operacion = input("Seleccione la operación a realizar: \n (C) Cargar créditos. \n (D) Descontar créditos. \n (X) Finalizar la simulación (termina el programa). \n ")
    # return monedero
    return historial


# De nuevo, como en el ejercicio anterior: Para testear la función, simplemente la invoco:
# print(devuelveHistorial())




# Ejercicio 4.3:
import random
"""
def sieteYMedio():
    # carta = 8             # La defino así para que entre en el while.
    # while carta == 8 or carta == 9:
        # carta = random.randint(0,12)
    acumulador: int = 0
    historial: list = []
    carta = random.choice([1, 2, 3, 4, 5, 6, 7, 10, 11, 12])
    acumulador += carta
    while acumulador <= 7.5:
        print("Llevás", acumulador, "puntos.")
        while input("¿Seguís o te plantás?\n(S) ¡Sigo! :D\n(N) Me planto :S\n ") != "N":
            carta = random.choice([1, 2, 3, 4, 5, 6, 7, 10, 11, 12])
            acumulador += carta
            historial.append(carta)
        print("Fin del juego.\nPuntuación: " + str(acumulador) + ".\nCartas obtenidas: " + str(historial) + ".")
        return
    print("Fin del juego.\nAcumulaste " + str(acumulador) + ".\n¡Perdiste! D:")
    return
"""

def sieteYMedio() -> str:
    # carta = 8             # La defino así para que entre en el while.
    # while carta == 8 or carta == 9:
        # carta = random.randint(0,12)
    acumulador: int = 0
    historial: list = []
    carta = random.choice([1, 2, 3, 4, 5, 6, 7, 10, 11, 12])
    if carta in [10, 11, 12]:
        acumulador += 0.5
    else:
        acumulador += carta
    historial.append(carta)
    while acumulador < 7.5:
        print("Llevás", acumulador, "puntos.")
        if input("¿Seguís o te plantás?\n(S) ¡Sigo! :D\n(N) Me planto :S\n ") != "N":
            carta = random.choice([1, 2, 3, 4, 5, 6, 7, 10, 11, 12])
            if carta in [10, 11, 12]:
                acumulador += 0.5
            else:
                acumulador += carta
            historial.append(carta)
        else:
            print("Fin del juego.\nPuntuación: " + str(acumulador) + ".\nCartas obtenidas: " + str(historial) + ".")
            return
    if acumulador == 7.5:
        return ("Fin del juego.\nPuntuación: " + str(acumulador) + ".\nCartas obtenidas: " + str(historial) + ".\n¡Ganaste! :D")
    else:
        return ("Fin del juego.\nPuntuación: " + str(acumulador) + ".\nCartas obtenidas: " + str(historial) + ".\n¡Perdiste! D:")


print(sieteYMedio())


# Ejercicio 5.1:
def perteneceACadaUno(s: list[list[int]], e: int) -> list[bool]:        # Donde tanto "s" como "e" son de tipo *** IN ***.
    res: list[bool] = []
    for lista in s:
        if pertenece1(lista, e):
            res.append(True)
        else:
            res.append(False)
    return res

"""
# Test cases:
print(perteneceACadaUno([[]], 3))
print(perteneceACadaUno([[10,30,2,1,4,23],[1,3,2],[4],[],[3]], 3))
"""


# Ejercicio 5.2:
def esMatriz1(s: list[list[int]]) -> bool:       # Donde "s" es de tipo *** IN ***.
    todasLasFilasMidenLoMismo: bool = True
    for filaMatriz in s:
        if len(filaMatriz) != len(s[0]):
            todasLasFilasMidenLoMismo = False
    return (len(s) > 0) and (len(s[0]) > 0) and todasLasFilasMidenLoMismo


def esMatriz2(s: list[list[int]]) -> bool:       # Donde "s" es de tipo *** IN ***.
    todasLasFilasMidenLoMismo: bool = True
    for filaMatriz in range(0, len(s)):
        if len(s[filaMatriz]) != len(s[0]):
            todasLasFilasMidenLoMismo = False
    return (len(s) > 0) and (len(s[0]) > 0) and todasLasFilasMidenLoMismo


"""
# Test cases:
print(esMatriz2([[1,2,3], [4,5,6], [7,8,9]]))         # Debería devolver "True".
print(esMatriz2([[0]]))                               # Debería devolver "True".
print(esMatriz2([[1,2], [7,2,7], [7,8]]))             # Debería devolver "False".
"""


# Ejercicio 5.3:
def filasOrdenadas(m: list[list[int]]) -> list[bool]:       # Donde "m" es de tipo *** IN ***.
    res: list = []
    for fila in m:
        if ordenados(fila) == True:
            res.append(True)
        else:
            res.append(False)
    return res

"""
# Test cases (¡mismos que el ítem anterior!):
print(filasOrdenadas([[1,2,3], [4,5,6], [7,8,9]]))         # Debería devolver [True, True, True].
print(filasOrdenadas([[0]]))                               # Debería devolver... ¿?.
print(filasOrdenadas([[1,2], [7,2,7], [7,8]]))             # Debería devolver [True, False, True].
"""

# Ejercicio 5.4:
# * Copypastee aquí xd *