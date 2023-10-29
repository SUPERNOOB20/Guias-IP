-- Ejercicio 1:
-- 1.
longitud :: [t] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

-- 2.
ultimo :: [t] -> t       -- Requiere: ¡[t] *NO* es una lista vacía!
ultimo (xs) = head (reverse (xs))

-- 3.
principio :: [t] -> [t]
principio (xs) = tail (reverse (xs))

-- 4.
reverso :: [t] -> [t]
reverso s = reverse s



-- Ejercicio 2:
-- 1.
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece e []     = False
pertenece e (x:xs) = e == x || pertenece e xs

-- 2.
todosIguales :: (Eq t) => [t] -> Bool      -- La consigna no nos proporciona una especificación :(
todosIguales []       = True               -- "Asumimos" este caso base
todosIguales [a]      = True
todosIguales (x:y:ys) = x == y && todosIguales (y:ys)

-- 3.
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos []        = True
todosDistintos [a]       = True
todosDistintos (x:xs)    = (cantidadDeApariciones x (x:xs)) < 2 && todosDistintos (xs)        -- ¡Ojo! Mi lista (x:xs) se va a ir ACHICANDO.

cantidadDeApariciones :: (Eq t) => t -> [t] -> Int
cantidadDeApariciones t [] = 0
cantidadDeApariciones t (x:xs)
    | t == x    = 1 + cantidadDeApariciones t (xs)
    | otherwise = cantidadDeApariciones t (xs)

-- 4.
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos (xs) = not (todosDistintos (xs))

-- 5.
quitar :: (Eq t) => t -> [t] -> [t]
quitar t [] = []
quitar t (x:xs)
    | (pertenece t (x:xs)) == False = (x:xs)
    | t == x                        = (xs)
    | otherwise                     = x : (quitar t (xs))                     -- Caso "t /= x"

-- 6.
quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos t [] = []
quitarTodos t (x:xs)
    | t == x     = (xs)
    | otherwise  = x : (quitarTodos t (xs))

-- 7.
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos []  = []
eliminarRepetidos [x] = [x]
eliminarRepetidos (x:xs)
    | (cantidadDeApariciones x (x:xs)) > 1 = eliminarRepetidos (quitar x (x:xs))
    | otherwise = x : eliminarRepetidos (xs)

-- 8.
mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos s r = esPermutacion s r                     -- Solo es un cambio de nombre (¡¡¡NO me gusta el nombre "mismosElementos!!!" >:c)

esPermutacion :: (Eq t) => [t] -> [t] -> Bool
esPermutacion []  []  = True
esPermutacion []  [_] = False
esPermutacion [_] []  = False
esPermutacion [a] [b]
    | a == b = True
    | otherwise = False
esPermutacion (x:xs) (y:ys)
    | (x:xs) == (y:ys) = True
    | otherwise = (cantidadDeApariciones x (x:xs) == cantidadDeApariciones x (y:ys))
    && (cantidadDeApariciones y (x:xs) == cantidadDeApariciones y (y:ys))
    && esPermutacion (quitarTodos x (quitarTodos y (x:xs))) (quitarTodos x (quitarTodos y (y:ys)))
esPermutacion _ _ = False

-- 9.
capicua :: (Eq t) => [t] -> Bool
capicua xs = xs == reverse xs




-- Ejercicio 3 (estos ejercicios serán todos en Z):
-- 1.
sumatoria :: [Integer] -> Integer
sumatoria []     = 0
sumatoria (x:xs) = x + sumatoria (xs)

-- 2.
productoria :: [Integer] -> Integer
productoria []     = 1
productoria (x:xs) = x * productoria (xs)

-- 3.
maximo :: [Integer] -> Integer
maximo []       = undefined
maximo [a]      = a
maximo (x:y:ys)
    | x > y     = maximo (x:ys)
    | otherwise = maximo (y:ys)

-- 4.
sumarN :: Integer -> [Integer] -> [Integer]
sumarN _ []     = []        -- Notemos que la especificación NO nos restringe el "caso vacío"
sumarN n (x:xs) = (x + n) : (sumarN n xs)

-- 5.
sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero [] = undefined
sumarElPrimero (x:xs) = sumarN x (x:xs)

-- 6.
sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo []   = undefined
sumarElUltimo (xs) = reverse (sumarN (head (reverse xs)) (reverse xs))

-- 7.
pares :: [Integer] -> [Integer]         -- Alt + 62
pares [] = []
pares xs
    | x `mod` 2 == 0 = x : (pares (tail xs))        -- Caso "x es par"
    | otherwise      = pares (tail xs)              -- Caso "x es par"
    where          x = head xs

-- 8.
multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN _ [] = []
multiplosDeN n (x:xs)
    | x `mod` n == 0 = x : (pares xs)
    | otherwise      =      pares xs

-- 9.
ordenar :: [Integer] -> [Integer]
ordenar []     = []
ordenar (x:xs) = (ordenar (quitar (maximo (x:xs)) (x:xs))) ++ (maximo (x:xs) : [])





-- Ejercicio 4 (estos ejercicios serán todos en "[Char]"):
-- 1.
sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos []  = []
sacarBlancosRepetidos [a] = [a]
sacarBlancosRepetidos (x:xs)
    | x == ' ' && (head xs) == ' ' = sacarBlancosRepetidos (xs)
    | otherwise                    = x : (sacarBlancosRepetidos xs)

-- 2.
contarPalabras ::  [Char] -> Integer
contarPalabras [] = 0
contarPalabras [a]
    | a == ' '  = 0
    | otherwise = 1
contarPalabras (x:xs) = contarPalabrasSinBRep (sacarBlancosRepetidos (x:xs))

contarPalabrasSinBRep :: [Char] -> Integer
contarPalabrasSinBRep [] = 0
contarPalabrasSinBRep [a]
    | a == ' '  = 0
    | otherwise = 1
contarPalabrasSinBRep (x:xs)
    | head xs == ' ' = 1 + contarPalabrasSinBRep xs
    | otherwise      =     contarPalabrasSinBRep xs

-- 3.
palabras :: [Char] -> [[Char]]
palabras []     = [[]]
palabras [a]    = [[a]]
palabras (x:xs) = (palabrasSinBREP (sacarBlancosIncorrectos (x:xs)))

palabrasSinBREP :: [Char] -> [[Char]]
palabrasSinBREP []         = [[]]
palabrasSinBREP [a]        = [[a]]
palabrasSinBREP (x:' ':xs) = [x] : palabrasSinBREP xs
palabrasSinBREP (x:xs)     = (x : (head (palabrasSinBREP xs))) : tail (palabrasSinBREP xs)

sacarBlancosIncorrectos :: [Char] -> [Char]        -- Ejemplo: sacarBlancosIncorrectos [' ', ' ', ' ', ' ', 'a', 'b', ' ', ' ', ' ', 'c', 'd', ' ', ' ', ' ', ' '] = ['a, 'b', ' ', 'c', 'd']
sacarBlancosIncorrectos xs = sacaPrimerosBlancos (sacaUltimosBlancos (sacarBlancosRepetidos xs))

sacaPrimerosBlancos :: [Char] -> [Char]
sacaPrimerosBlancos []       = []
sacaPrimerosBlancos [a]      = [a]
sacaPrimerosBlancos (' ':xs) = sacaPrimerosBlancos xs
sacaPrimerosBlancos zs       = zs

sacaUltimosBlancos :: [Char] -> [Char]
sacaUltimosBlancos []     = []
sacaUltimosBlancos [a]    = [a]
sacaUltimosBlancos (x:xs) = reverse (sacaPrimerosBlancos (reverse (x:xs)))

-- 4.
palabraMasLarga :: [Char] -> [Char]
palabraMasLarga xs = maximoPalabras (palabras xs)                -- "maximoPalabras" o "comparaPalabras"

maximoPalabras :: [[Char]] -> [Char]
maximoPalabras [[]]                 = []                         -- Caso base de 0 elementos
maximoPalabras [a]                  = a                          -- Caso base de 1 elemento // a :: [Char]
maximoPalabras (x:y:ys)                                          -- Recursión (2 o más elementos)
    | (longitud x) > (longitud y) = maximoPalabras (x:ys)
    | otherwise                   = maximoPalabras (y:ys)

-- Test: palabraMasLarga ['p','a','l','a','b','r','a',' ','M','a','s',' ','L','a','r','g','a'] = "palabra"

-- 5.
aplanar :: [[Char]] -> [Char]
aplanar [[]] = []
aplanar [a]  = (head a) : aplanar [(tail a)]    -- a :: [Char]
aplanar (x:xs) = (aplanar [x]) ++ (aplanar xs)  -- x :: [Char]  //  xs :: [[Char]]

{-

Test suite para el ejercicio de arriba:
1) aplanar [[]]                      = ""
2) aplanar ["palabra"]               = "palabra"
3) aplanar ["palabra", "xd", "hoal"] = "palabraxdhoal"

-}


-- 6.
aplanarConBlancos :: [[Char]] -> [Char]
aplanarConBlancos [[]] = []
aplanarConBlancos [a] = a                                                           -- a :: [Char]
aplanarConBlancos (x:xs) = ((aplanar [x]) ++ [' ']) ++ (aplanarConBlancos xs)       -- x :: [Char]  //  xs :: [[Char]]

-- Test: aplanarConBlancos ["palabra", "mas", "larga"] = "palabra mas larga"

-- 7.
aplanarConNBlancos :: [[Char]] -> Integer -> [Char]         -- n pertenece a N_0
aplanarConNBlancos [[]] _ = []
aplanarConNBlancos [a] _ = a                                                           -- a :: [Char]
aplanarConNBlancos (x:xs) n = ((aplanar [x]) ++ (nBlancos n)) ++ (aplanarConNBlancos xs n)       -- x :: [Char]  //  xs :: [[Char]]

nBlancos :: Integer -> [Char]
nBlancos 0 = []
nBlancos n = [' '] ++ nBlancos (n - 1)

-- Test: aplanarConBlancos ["palabra", "mas", "larga"] 10 = "palabra          mas          larga"
-- Consejito: Probar también con n = 10000 <:]



-- Ejercicio 5:
-- 1.
sumaAcumulada :: (Num t) => [t] -> [t]
sumaAcumulada [] = []
sumaAcumulada [a] = [a]
sumaAcumulada (xs) = sumaAcumulador xs 0

sumaAcumulador :: (Num t) => [t] -> t -> [t]
sumaAcumulador []  _    = []
sumaAcumulador [a] k    = [a + k]
sumaAcumulador (x:xs) k = (x + k) : (sumaAcumulador xs (x + k))

-- 2.
descomponerEnPrimos :: [Integer] -> [[Integer]]     -- REQUIERE: ¡¡¡Todos los elementos de entrada son mayores o iguales a 2!!!
descomponerEnPrimos []     = [[]]
descomponerEnPrimos [x]    = [factores x (x - 1)]
descomponerEnPrimos (x:xs) = (factores x (x - 1)) : (descomponerEnPrimos (xs))
-- x :: [Integer]     //      xs :: [[Integer]]


factores :: Integer -> Integer -> [Integer] -- Dado un número cualquiera, devuelve una lista con sus factores
factores 2 _          = [2]
factores _ 1          = []
factores n k
    | n `mod` k == 0  = [k] ++ factores n (k - 1)            -- Caso "k es factor de n"
    | otherwise       =        factores n (k - 1)            -- Caso "k NO es factor de n"