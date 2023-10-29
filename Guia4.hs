-- Ejercicio 1:
fibonacci :: Integer -> Integer
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n - 1) + fibonacci (n - 2)



-- Ejercicio 2:
parteEnteraTramposa :: Float -> Integer
parteEnteraTramposa x
    | x == fromIntegral (ceiling x) = ceiling x            -- Caso x ∈ Z. Comparamos dos Floats y devolvemos un integer.
    | otherwise = (ceiling x) - 1                          -- Caso x ∈/ Z
-- doc ceiling ---> @'ceiling' x@ returns the least integer not less than @x@

parteEnteraRecursion :: Float -> Integer
parteEnteraRecursion a
    | a <  0    = parteEnteraRecursionNegativo a
    | a == 0    = 0
    | otherwise = parteEnteraRecursionPositivo a    -- Caso a > 0

parteEnteraRecursionNegativo :: Float -> Integer
parteEnteraRecursionNegativo b
    | b >= 0     = 0
    | otherwise  = -1 + parteEnteraRecursionNegativo (b + 1)

parteEnteraRecursionPositivo :: Float -> Integer
parteEnteraRecursionPositivo d
    | d < 1     = 0
    | otherwise = 1 + parteEnteraRecursionPositivo (d - 1)



{-
"Tests":
parteEnteraTramposa    727   ==  727
parteEnteraTramposa (-727)   == -727
parteEnteraTramposa 72.7     ==  72
parteEnteraTramposa (-72.7)  == -73
-}


{-
"Tests":
parteEnteraRecursion    727   ==  727
parteEnteraRecursion (-727)   == -727
parteEnteraRecursion 72.7     ==  72
parteEnteraRecursion (-72.7)  == -73
-}




-- Ejercicio 3:    Mentira ---> ¡Vamos a usar el algoritmo de Euclides! <--- Mentira
esDivisible :: Integer -> Integer -> Bool       -- Ej: 4 es divisible por 2. Recibe dos naturales de entrada.
esDivisible a b
    | a == 0 = True
    | b == 0 = undefined

    | a < b = False
    | a == b = True
    | otherwise = esDivisible (a - b) b



-- Ejercicio 4:
sumaImpares :: Integer -> Integer -- Sea n un número natural dado como parámetro. sumaImpares suma los primeros n números impares.
sumaImpares n
    | n == 1 = 1
    | otherwise = (2 * n - 1) +  sumaImpares (n - 1)


-- Ejercicio 5:
medioFact :: Integer -> Integer -- Sea n un número natural dado como parámetro. medioFact n = n!!
medioFact 1 = 1
medioFact 2 = 2
medioFact n = n * medioFact (n - 2)



-- Ejercicio 6:
sumaDigitos :: Integer -> Integer
sumaDigitos n
    | n < 10    =  n
    | otherwise = (n `mod` 10) + sumaDigitos (n `div` 10)




-- Ejercicio 7:

-- Manera 1 (vista en clases)
todosDigitosIgualesW :: Integer -> Bool     -- Recibe un número natural n como parámetro
todosDigitosIgualesW n
    | n < 10 = True
    | otherwise = (primerDigitoW == segundoDigitoW) && (todosDigitosIgualesW (sacarPrimerDigitoW))
    where primerDigitoW      = n `mod` 10
          segundoDigitoW     = (n `div` 10) `mod` 10
          sacarPrimerDigitoW = n `div` 10





-- Manera 2 (lo mismo, pero con auxiliares):
todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n
    | n < 10 = True
    | otherwise = primerDigito n == segundoDigito n && todosDigitosIguales (sacarPrimerDigito n)


primerDigito :: Integer -> Integer
primerDigito n = n `mod` 10

segundoDigito :: Integer -> Integer
segundoDigito n = (n `div` 10) `mod` 10

sacarPrimerDigito :: Integer -> Integer
sacarPrimerDigito n = n `div` 10






-- Ejercicio 8:
iesimoDigito :: Integer -> Integer -> Integer       -- ¡Ojo! n ∈ N≥0.    1 ≤ i ≤ cant digitos (n).
iesimoDigito n i = primerDigito (n `div` (10^(cantDigitos(n) - i)))

cantDigitos :: Integer -> Integer
cantDigitos n
    | n < 10 = 1
    | otherwise = 1 + cantDigitos (n `div` 10)

-- ¿Cómo podemos hacer más declarativo el código de arriba? Duda para preguntar en clase





-- Ejercicio 9:
-- Idea: Saco el primer digito, saco el último, los comparo. && esCapicua de sacar primer y úlitmo digito.

esCapicua :: Integer -> Bool
esCapicua n
    | n < 10    = True
    | n < 100   = primerDigito n == ultimoDigito n
    | otherwise = primerDigito n == ultimoDigito n && esCapicua (sacarPrimerDigito (sacarUltimoDigito n))       -- Caso "n >= 100"


ultimoDigito :: Integer -> Integer
ultimoDigito n = iesimoDigito n 1

sacarUltimoDigito :: Integer -> Integer
sacarUltimoDigito n = n - ((ultimoDigito n) * (10 ^ (cantDigitos (n) - 1)))



-- Ejercicio 10:
-- a)
f1 :: Integer -> Integer        -- Recordemos que f1 va "de N_0 a N"
f1 n = 2 ^ (n+1) - 1

-- b)
f2 :: Integer -> Float -> Float          -- f2 va "de N a R a R"
f2 n 1 = fromInteger (n) + 1
f2 n q = (q^(n+1) - 1) / (q-1)

-- c)
f3 :: Integer -> Float -> Float
f3 n q = f2 (2*n) q

-- d)
f4 :: Integer -> Float -> Float
f4 n q = f3 n q - f2 n q + q ^ n




-- Ejercicio 11:
-- a)
eAprox :: Integer -> Float
eAprox 0 = 1
eAprox n = (1 / fromIntegral(factorial n) + eAprox (n - 1))


factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial (n - 1)

-- b)
e :: Float
e = eAprox 10




-- Ejercicio 12:
raizDe2Aprox :: Integer -> Float
raizDe2Aprox n = sucesionDeDos (n) - 1

sucesionDeDos :: Integer -> Float
sucesionDeDos 1 = 2
sucesionDeDos n = 2 + 1 / sucesionDeDos (n - 1)



-- Ejercicio 13:
sumatoriaDoble :: Integer -> Integer -> Float       -- (n,m ∈ N) ---> R
sumatoriaDoble a b = sumatoriaDobleHasta a b b

sumatoriaDobleHasta :: Integer -> Integer -> Integer -> Float
sumatoriaDobleHasta 1 1 _ = 1
sumatoriaDobleHasta n m j
    | m == 1       = (fromInteger n)**(fromInteger m) + sumatoriaDobleHasta (n - 1)   j         j
    | otherwise    = (fromInteger n)**(fromInteger m) + sumatoriaDobleHasta  n       (m - 1)    j

-- CASO DE TEST PARA EL EJERCICIO 13:
-- sumatoriaDoble 3 3 == 56


-- Ejercicio 14:
sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias q n m = sumaPotenciasHasta q n m m

sumaPotenciasHasta :: Integer -> Integer -> Integer -> Integer -> Integer
sumaPotenciasHasta q 1 1 _ = q * q     -- q^2
sumaPotenciasHasta q n m j
    | m == 1       = q ^ (n + m) + sumaPotenciasHasta q (n - 1)   j       j
    | otherwise    = q ^ (n + m) + sumaPotenciasHasta q  n       (m - 1)  j

-- CASO DE TEST PARA EL EJERCICIO 14:
-- sumaPotencias 2 2 3 == 84





-- Ejercicio 15:
sumaRacionales :: Integer -> Integer -> Float
sumaRacionales n m = sumaRacionalesHasta n m m

sumaRacionalesHasta :: Integer -> Integer -> Integer -> Float
sumaRacionalesHasta 1 1 _ = 1
sumaRacionalesHasta n m j
    | m == 1 = (fromInteger n) + sumaRacionalesHasta (n - 1) j j
    | otherwise = ((fromInteger n) / (fromInteger m)) + sumaRacionalesHasta n (m - 1) j

{-

Casos de test para el Ejercicio 15:
[*] sumaRacionales 4 2 = 15
[*] sumaRacionales 4 3 = 18,33333333333...

-}






-- Ejercicio 16:
-- a)
menorDivisor :: Integer -> Integer
menorDivisor 1 = undefined  -- Según la especificación dada para este ejercicio, xd
menorDivisor n = menorDivisorDesde 2 n

menorDivisorDesde :: Integer -> Integer -> Integer
menorDivisorDesde k n
    | n `mod` k == 0 = k
    | otherwise      = menorDivisorDesde (k + 1) n

-- b)
esPrimo :: Integer -> Bool      -- Notemos que... ¡un número p es primo sii menorDivisor p = p!
esPrimo p = (menorDivisor p) == p

-- c)
sonCoprimos :: Integer -> Integer -> Bool
sonCoprimos n m = not (tienenAlgoEnComun (listaDivisores n) (listaDivisores m))

-- Ejemplos:
-- sonCoprimos 10 15 = False
-- sonCoprimos 11 15 = True




tienenAlgoEnComun :: [Integer] -> [Integer] -> Bool -- Devuelve true sii ambas listas tienen AL MENOS ***UN*** elemento en común        -- #pragma
-- tienenAlgoEnComun [] []                                = False      -- #pragma
tienenAlgoEnComun _ []                                 = False      -- #pragma
tienenAlgoEnComun [] _                                 = False      -- #pragma
tienenAlgoEnComun [a] [b]                              = a == b     -- #pragma
tienenAlgoEnComun (x:xs) (y:ys)                                     -- #pragma
    | (x `pertenece` (y:ys)) || (y `pertenece` (x:xs)) = True       -- #pragma
    | otherwise = tienenAlgoEnComun xs ys                           -- #pragma


pertenece :: (Eq t) => t -> [t] -> Bool     -- FUNCIÓN SACADA DEL EJERCICIO 2.1 DE Guia5.hs
pertenece _ []     = False
pertenece a (x:xs) = a == x || pertenece a xs

listaDivisores :: Integer -> [Integer] -- Dado un natural n, devuelve una lista con todos sus divisores
listaDivisores n = eliminarRepetidos (listaDivisoresRecursion 2 n)

listaDivisoresRecursion :: Integer -> Integer -> [Integer]  -- Hace recursión sobre "menorDivisorDesde" hasta que k valga n.
listaDivisoresRecursion k n
    | k == n              = [k]     -- Caso base
    | otherwise           = [menorDivisorDesde k n] ++ listaDivisoresRecursion (menorDivisorDesde (k + 1) n) n



quitar :: (Eq t) => t -> [t] -> [t]                     -- FUNCIÓN EXTRAÍDA DEL EJERCICIO 2.5 DE Guia5.hs
quitar t [] = []
quitar t (x:xs)
    | (pertenece t (x:xs)) == False = (x:xs)
    | t == x                        = (xs)
    | otherwise                     = x : (quitar t (xs))                     -- Caso "t /= x"

cantidadDeApariciones :: (Eq t) => t -> [t] -> Integer      -- FUNCIÓN EXTRAÍDA DEL EJERCICIO 2.3 DE Guia5.hs
cantidadDeApariciones t [] = 0
cantidadDeApariciones t (x:xs)
    | t == x    = 1 + cantidadDeApariciones t (xs)
    | otherwise = cantidadDeApariciones t (xs)


eliminarRepetidos :: (Eq t) => [t] -> [t]   -- Porque soy tan imbécil que no pude resolver los duplicados de listaDivisoresRecursion "^-^   //  FUNCIÓN EXTRAÍDA DEL EJERCICIO 2.7 DE Guia5.hs
eliminarRepetidos []  = []
eliminarRepetidos [x] = [x]
eliminarRepetidos (x:xs)
    | (cantidadDeApariciones x (x:xs)) > 1 = eliminarRepetidos (quitar x (x:xs))
    | otherwise = x : eliminarRepetidos (xs)




-- d)
nEsimoPrimo :: Integer -> Integer               -- Por la especificación dada, n >= 1
nEsimoPrimo n = cuentaHastaNEsimoPrimo 3 1 n

cuentaHastaNEsimoPrimo :: Integer -> Integer -> Integer -> Integer
-- cuentaHastaNEsimoPrimo 1 _ = 2
cuentaHastaNEsimoPrimo m k n     -- k cuenta cuántos primos voy contando (¡hasta llegar al nEsimo!)
    | k == n = m - 1
    | (esPrimo m == True) = cuentaHastaNEsimoPrimo (m + 1)   (k + 1)    n
    | otherwise           = cuentaHastaNEsimoPrimo (m + 1)    k         n       -- Caso "m NO es primo"



-- Ejercicio 17
esFibonacci :: Integer -> Bool      -- POR ESPECIFICACIÓN DADA: N >= 0
-- esFibonacci 0 = True
esFibonacci n = chequeaFibonacci n 0

chequeaFibonacci :: Integer -> Integer -> Bool
chequeaFibonacci n i
    | n <  (fibonacci i) = False
    | n == (fibonacci i) = True
    | otherwise          = chequeaFibonacci n (i + 1) -- Caso "n > fibonacci i" (Cuando todavía no llegué a n)


mayorDigitoPar :: Integer -> Integer    -- Si n no tiene ningún dígito par, res = -1
mayorDigitoPar n
    | (digitosPares n) == [] = -1
    | otherwise = maximo (digitosPares n)

maximo :: [Integer] -> Integer              -- FUNCIÓN EXTRAÍDA DEL EJERCICIO 3.3 DE Guía5.hs
maximo []       = undefined
maximo [a]      = a
maximo (x:y:ys)
    | x > y     = maximo (x:ys)
    | otherwise = maximo (y:ys)

digitosPares :: Integer -> [Integer]    -- Ejemplo: digitosPares 1234 = [2, 4]
digitosPares n
    | (n < 10) && (n `mod` 2 == 0) = [n]
    | (n < 10) && (n `mod` 2 /= 0) = []
    | n `mod` 2 == 0 = [primerDigito n] ++ digitosPares (sacarPrimerDigito n)
    | otherwise      = digitosPares (sacarPrimerDigito n)




-- Ejercicio 19:
esSumaInicialDePrimos :: Int -> Bool    -- Por especificación, n >= 0
esSumaInicialDePrimos n = chequeaSumaInicialPrimos n 1 2

chequeaSumaInicialPrimos :: Int -> Int -> Int -> Bool
chequeaSumaInicialPrimos n i s      -- i := itera n-ésimos primos    //    s := suma primos
    | n <  s    = False
    | n == s    = True 
    | otherwise = chequeaSumaInicialPrimos n (i + 1) (s + nEsimoPrimoInt (i + 1))        -- Caso "n > s" (Cuando todavía no llegué a n)

{-

CASOS DE TEST para el Ejercicio 19:
[*] esSumaInicialDePrimos 2  == True
[*] esSumaInicialDePrimos 5  == True
[*] esSumaInicialDePrimos 10 == True
[*] esSumaInicialDePrimos 17 == True
[*] esSumaInicialDePrimos 28 == True

(¡todos los demás antes de 28 dan False!)

-}




esPrimoInt :: Int -> Bool                                -- Misma función del ejercicio 16b, pero con Int
esPrimoInt p = (menorDivisorInt p) == p


menorDivisorInt :: Int -> Int                            -- Misma función del ejercicio 16a, pero con Int
menorDivisorInt 1 = undefined  
menorDivisorInt n = menorDivisorDesdeInt 2 n


menorDivisorDesdeInt :: Int -> Int -> Int                -- ídem
menorDivisorDesdeInt k n
    | n `mod` k == 0 = k
    | otherwise      = menorDivisorDesdeInt (k + 1) n


nEsimoPrimoInt :: Int -> Int                             -- Misma función del ejercicio 17, pero con Int
nEsimoPrimoInt n = cuentaHastaNEsimoPrimoInt 3 1 n


cuentaHastaNEsimoPrimoInt :: Int -> Int -> Int -> Int    -- ídem
cuentaHastaNEsimoPrimoInt m k n                             
    | k == n                 = m - 1
    | (esPrimoInt m == True) = cuentaHastaNEsimoPrimoInt (m + 1)   (k + 1)    n
    | otherwise              = cuentaHastaNEsimoPrimoInt (m + 1)    k         n       -- Caso "m NO es primo"





-- Ejercicio 20:
tomaValorMax :: Int -> Int -> Int
tomaValorMax a b
    | a == b = b
    | otherwise = devuelveValorM a b (sumaDivisores a) a       


devuelveValorM :: Int -> Int -> Int -> Int -> Int
devuelveValorM a b s i           -- "s" de "suma" ("s" es el máximo actual    //   "i" es el valor m al que corresponde "s")
    | (a == b) && ((max (sumaDivisores b) s) == (sumaDivisores b)) = b         -- Caso base (ya "recorrí todo")  //  ¡"max" es una función del prelude! Aunque podríamos también, en su lugar, usar maximo2 (de la práctica 1).
    | (a == b) && ((max (sumaDivisores b) s) == s)                 = i         -- Caso base (ya "recorrí todo")  //  ¡"max" es una función del prelude! Aunque podríamos también, en su lugar, usar maximo2 (de la práctica 1).
    | (max (sumaDivisores a) s)              == (sumaDivisores a)  = devuelveValorM (a + 1) b (sumaDivisores a) a
    | otherwise                                                    = devuelveValorM (a + 1) b s i

sumaDivisores :: Int -> Int
sumaDivisores n = sum (listaDivisoresInt n)


listaDivisoresInt :: Int -> [Int] -- Dado un natural n, devuelve una lista con todos sus divisores
listaDivisoresInt n = eliminarRepetidos (listaDivisoresRecursionInt 2 n)

listaDivisoresRecursionInt :: Int -> Int -> [Int]  -- Hace recursión sobre "menorDivisorDesde" hasta que k valga n.
listaDivisoresRecursionInt k n
    | k == n              = [k]     -- Caso base
    | otherwise           = [menorDivisorDesdeInt k n] ++ listaDivisoresRecursionInt (menorDivisorDesdeInt (k + 1) n) n

{-

TEST SUITCASE PARA EJERCICIO 20:
[*] sumaDivisores 2 7   == 6
[*] sumaDivisores 42 43 == 42
[*] sumaDivisores 42 47 == 42
[*] sumaDivisores 42 48 == 48

-}





-- Ejercicio 21:
-- Idea: Aplico doble sumatoria en ***p** y ***q*** y encajo p y q en la ecuación:
-- si == se cumple, sumo 1 y hago recursión. Otherwise, solo recursión

pitagoras :: Integer -> Integer -> Integer -> Integer -- ¡¡¡OJO!!!       ***** m, n, r ∈ N≥0 *****
pitagoras m n r = pitagorasDobleRecursion m n r n

pitagorasDobleRecursion :: Integer -> Integer -> Integer -> Integer -> Integer
pitagorasDobleRecursion 0 0 _ _ = 1          -- 0^2 + 0^2 <= r^2 (para todo r ∈ N≥0)
pitagorasDobleRecursion m n r j              -- Donde "r" y "j" son FIJOS.
    | (n == 0) && (m^2 <= r^2)  = 1 + pitagorasDobleRecursion (m - 1)   j        r j
    | (n == 0) && (m^2 >  r^2)  =     pitagorasDobleRecursion (m - 1)   j        r j
    | (m^2 + n^2) <= r^2        = 1 + pitagorasDobleRecursion  m       (n - 1)   r j
    | otherwise                 =     pitagorasDobleRecursion  m       (n - 1)   r j


-- Notar que, en este ejercicio, ¡la propia consigna nos da el test suitcase en el PDF! :]