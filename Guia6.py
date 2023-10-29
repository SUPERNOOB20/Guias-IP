# Ejercicio 1.1
def imprimir_hola_mundo() -> str:
    print("¡Hola Mundo!")

# print(imprimir_hola_mundo()) <--- NO (devuelve "None")
imprimir_hola_mundo()
 
# Ejercicio 1.2
def imprimir_un_verso() -> str:         # PR II
    print("And after all that I've done\n After all of my pain\n After all that I've become\n Will I disappear, disappear\n Like a ghost in the breeze?\n Like fading memories\n Like the world you left was only just a dream\n So I'll disappear, I'll disappear, I'll disappear")
    
# print(imprimir_un_verso()) <--- NO (devuelve "None")
imprimir_un_verso()

# Ejercicio 1.3

import math

def raizDeDos() -> int:
    sqrt2 = round((math.sqrt (2)),4)
    print(sqrt2)
    
raizDeDos()


# Ejercicio 1.4
def factorial_de_dos() -> int:
    fact2 = math.factorial(2)
    print(fact2)
    
factorial_de_dos()


# Ejercicio 1.5
def perimetro() -> float:   # Devuelve el perímetro de una circunferencia de radio 1
    print('a')
    print('b')
    print('c')
    return (2 * math.pi)

print("Ejercicio 1.5: " + str(perimetro()))

# Ejercicio 2.1
"""
def imprimir_saludo(nombre: str) -> str:
    print("Hola " + nombre)

#   ^^^Esto es un procedimiento: el "print()" se ejecuta de forma interna, y... ¡NO printea nada!^^^
    """


def imprimir_saludo(nombre: str) -> str:
    return ("Hola " + nombre)

print(imprimir_saludo("pepe"))



# Ejercicio 2.2

def raiz_cuadrada_de(numero: int) -> int:
    return math.sqrt(numero)


# Ejercicio 2.3

def farenheit_a_celsius(temp_far: float) -> float:
    celsius = ((temp_far - 32) * 5) / 9
    return celsius

# Ejercicio 2.4

"""
# FORMA 1:
def imprimir_dos_veces(estribillo: str) -> str:          # Devuelve bis(estribillo)
    bis = estribillo * 2
    return bis
"""

# FORMA 2:
def imprimir_dos_veces(estribillo: str) -> str:          # Devuelve bis(estribillo)
    a = estribillo
    b = "\n \n"
    c = estribillo
    return print(a,b,c)

# Test de ejemplo: Probar: 
# Guia6.imprimir_dos_veces("And after all that I've done\n After all of my pain\n After all that I've become\n Will I disappear, disappear\n Like a ghost in the breeze?\n Like fading memories\n Like the world you left was only just a dream\n So I'll disappear, I'll disappear, I'll disappear")


# Ejercicio 2.5

def es_multiplo_de(n: int, m: int) -> bool:
    if n % m == 0:
        return True
    else:
        return False

# EJEMPLOS:
# es_multiplo_de (9,3) == True
# es_multiplo_de (3,9) == False

# Ejercicio 2.6

def es_par(numero: int) -> bool:
    return es_multiplo_de (numero, 2)

# Ejercicio 2.7

# Ejemplos:
# cantidad_de_pizzas(2,5) son 10 porciones, dividido 8... 2 pizzas :)
# cantidad_de_pizzas(4,2) ---> 1 pizza
# cantidad_de_pizzas(3,2) ---> 1 pizza
# cantidad_de_pizzas(3,3) ---> 2 pizzas
# cantidad_de_pizzas(9 7) ---> 7 pizzas

def cantidad_de_pizzas(comensales: int, min_cant_de_porciones: int) -> int:
    porciones = comensales * min_cant_de_porciones
    pizzas = math.ceil(porciones / 8)
    return pizzas


# Ejercicio 3.1
def alguno_es_0(numero1: float, numero2: float) -> bool:
    return numero1 == 0 or numero2 == 0

# Ejercicio 3.2
def ambos_son_0(numero1: float, numero2: float) -> bool:
    return numero1 == 0 and numero2 == 0

# Ejercicio 3.3
def es_nombre_largo(nombre: str) -> bool:
    # length(nombre) >= 8 == True
    return len(nombre) >= 3 and len(nombre) <= 8

print(es_nombre_largo("nahuel"))



# Ejercicio 3.4

# Devuelve True si el año pasado como parámetro es bisiesto. Si no, devuelve False.
def es_bisiesto(año: int) -> bool:
    a = es_multiplo_de (año, 400)
    b = es_multiplo_de (año, 4) and not es_multiplo_de (año, 100)
    return a or b

"""
print(es_bisiesto(1900))
print(es_bisiesto(1904))
print(es_bisiesto(2023))
print(es_bisiesto(2024))
"""



# Ejercicio 4

# Ejemplos de min y max
# max(2,3,4)
# min(2,3,4)

##### CONSULTAS PARA PREGUNTAR EL LUNES EN CLASE:
# ¿Cómo mejoro la declaratividad en "peso_pino()"?
# ¿Está bien tipar las funciones con tipos "inventados" como altura, peso, y sirve...?

# altura: float   (En metros)
# peso: float     (En kg)
# sirve: bool     (Si sirve el pino, devuelve True. Si no, devuelve False)


def peso_pino(altura: float) -> float:       # Toma la altura de un pino en metros y devuelve su peso en kg
    centimetros_pino = altura * 100
    if altura <= 3:
        peso = centimetros_pino * 3
    else:
        peso = 900 + (altura - 3) * 200
    return peso

def es_pino_util(peso: float) -> bool:     # Toma el peso en kg de un pino y devuelve True si sirve (e.o.c devuelve False).
    a = 400 == min (peso, 400)
    b = 1000 == max (peso, 1000)
    sirve = a and b
    return sirve

def sirve_pino(altura: float) -> bool:
    return es_pino_util(peso_pino(altura))

"""
print("pino de 100kg"  + " da " + str(es_pino_util(100)))
print("pino de 500kg"  + " da " + str(es_pino_util(500)))
print("pino de 1500kg" + " da " + str(es_pino_util(1500)))

print(peso_pino(2)) # == 600
print(peso_pino(5)) # == 1300

print(sirve_pino(2)) # == True
print(sirve_pino(5)) # == False
"""


"""
TEST CASES:
peso_pino(2) == 600
peso_pino(5) == 1300

sirve_pino(2) == True
sirve_pino(5) == False
"""





# Ejercicio 5.1
def devolver_el_doble_si_es_par(numero: float) -> float:
    res = numero
    if numero % 2 == 0:
        res = numero * 2
    return res


# Ejercicio 5.2
def devolver_valor_si_es_par_sino_el_que_sigue1(numero: int) -> int:
    if numero % 2 == 0:
        res = numero
    if numero % 2 != 0:
        res = numero + 1
    return res

def devolver_valor_si_es_par_sino_el_que_sigue2(numero: int) -> int:
    if numero % 2 == 0:
        res = numero
    else:
        res = numero + 1
    return res

# Conclusión: Sí, ambas formas de implementación funcionan correctamente :]

# Ejercicio 5.3

# 2 if (NO NOS SIRVE):
"""
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9_v1(numero: int) -> int:
    res = numero
    if numero % 3 == 0:
        res = 2 * numero
    if numero % 9 == 0:
        res = 3 * numero
    return res
"""

# if-then-else (NO NOS SIRVE):
"""
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9_v1(numero: int) -> int:
    if numero % 3 == 0:
        res = 2 * numero
    else:
        res = numero
    return res
"""


# if-elif-else (SÍ NOS SIRVE):
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9_v2(numero: int) -> int:
    if numero % 3 == 0:
        res = 2 * numero
    elif numero % 9 == 0:
        res = 3 * numero
    else:
        res = numero
    return res

# Conclusión: Ninguna de las dos implementaciones sugeridas en el enunciado resolvió nuestro problema (tuvimos que idear una nueva implementación, distinta).


# Ejercicio 5.4:
def lindo_nombre(nombre: str) -> str:
    res = "Tu nombre tiene menos de 5 caracteres"
    if len(nombre) >= 5:
        res = "Tu nombre muchas letras!"
    return res

# Ejercicio 5.5:
def elRango(numero: float) -> str:
    res = ""
    if numero < 5:
        res = "Menor a 5"
    elif 10 <= numero <= 20:
        res = "Entre 10 y 20"
    elif numero > 20:
        res = "Mayor a 20"
    return res

# Ejercicio 5.6:
def elRango(sexo: str, edad: int) -> str:
    res = "Andá de vacaciones"
    if ((sexo == "F") and (18 <= edad < 60)) or ((sexo == "M") and (18 <= edad < 65)):
        res = "Te toca trabajar"
    return res





# Ejercicio 6.1:
def de1a10():
    i = 1
    while i <= 10:
        print(i)
        i += 1
    return


# Ejercicio 6.2:
def paresDe10a40():
    i = 10
    while i <= 40: 
        print(i)
        i += 2
    return


# Ejercicio 6.3:
def ecoPor10():
    i = 1
    while i <= 10:
        print("eco")
        i += 1

# print(ecoPor10())

# Ejercicio 6.4:
def set_off(countdown: int):
    while countdown >= 0:
        print(countdown)
        countdown -= 1
    print("Despegue")
    return

# print(set_off(13))

# Ejercicio 6.5:
def viajeAlPasado(partida: int, llegada: int):      # Donde "partida" es el año de partida; y "llegada" es el año de llegada. Requiere que "partida > llegada".
    año = partida
    while año > llegada:
        año -= 1
        print("Viajó un año al pasado, estamos en el año: ", año,".")
    print("Llegamos, es el año ",año," :]")
    return


# Ejercicio 6.6:
def viajeHastaAristoteles(partida: int):    # Viaja hasta después del 364 a.C. (año "-364")
    año = partida
    while año > (-364):
        año -= 20
        print("Viajó veinte años al pasado, estamos en el año: ", año,".")
    print("Llegamos, es el año ",año,", ¡vamos a conocer a Aristóteles! :3")
    return


# Ejercicio 7.1:
def de1a10_FOR():
    for num in range(1,11,1):
        print("eco")
        # print(num)
    return

# print(de1a10_FOR())

# Ejercicio 7.2:
def paresDe10a40_FOR():
    for i in range(10,42,2):
        print(i)


# paresDe10a40_FOR()

# Ejercicio 7.3:
def ecoPor10_FOR():
    for i in range(1,11,1):
        print("eco")
    return

# Ejercicio 7.4:
def set_off_FOR(countdown: int):
    for conteo in range(countdown, 0, -1):
        print(conteo)
    print("0")
    print("Despegue")

# print(set_off_FOR(7))


# Ejercicio 7.5:
def viajeAlPasado_FOR(partida: int, llegada: int):
    for año in range(partida, llegada, -1):
        print("Viajó un año al pasado, estamos en el año: " + str(año) + ".")
    print("Llegamos, es el año " + str(llegada) + " :]")

# print("EJERCICIO 7.5:")
# viajeAlPasado_FOR(2023, 2002)

# Ejercicio 7.6:
def viajeHastaAristoteles_FOR(partida: int):    # Viaja hasta después del 364 a.C. (año "-364")
    for año in range (partida, -364, -20):
        año -= 20
        print("Viajó veinte años al pasado, estamos en el año:", str(año) + ".")
    print("Llegamos, es el año", str(año) + ", ¡vamos a conocer a Aristóteles! :3")
    return

# print("EJERCICIO 7.6:")
# viajeHastaAristoteles_FOR(2023)


