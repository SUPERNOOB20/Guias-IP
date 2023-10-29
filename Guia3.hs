-- Ejercicio 1

f :: Int -> Int
f 1 = 8
f 4 = 131

g :: Int -> Int
g 8 = 16
g 16 = 4
g 131 = 1

h :: Int -> Int
h x = f (g(x))

k :: Int -> Int
k x = g (f(x))




-- Ejercicio 2
-- a)

absoluto :: Int -> Int
absoluto x = abs(x)


-- b)
maximoabsoluto :: Int -> Int -> Int
maximoabsoluto x y
    | absoluto (x) >= absoluto (y) = absoluto (x)
    | otherwise = absoluto (y)


-- c)
maximo3 :: Int -> Int -> Int -> Int
maximo3 x y z
    | x >= y && y >= z = x
    | x >= z && z >= y = x
    | y >= x && x >= z = y
    | y >= z && z >= x = y
    | z >= x && x >= y = z
    | otherwise = z


-- d)
algunoEs0 :: Float -> Float -> Bool
algunoEs0 x y
    | x == 0 = True
    | y == 0 = True
    | otherwise = False


algunoEs0PM :: Float -> Float -> Bool
algunoEs0PM _ 0 = True
algunoEs0PM 0 _ = True
algunoEs0PM _ _ = False


algunoEs0Mezclita :: Float -> Float -> Bool
algunoEs0Mezclita a b
    | a == 0 = True
    | b == 0 = True
algunoEs0Mezclita _ _ = False


-- e)
ambosSon0 :: Float -> Float -> Bool
ambosSon0 x y
    | (x == y) && (y == 0) = True
    | otherwise = False

ambosSon0PM :: Float -> Float -> Bool
ambosSon0PM 0 0 = True
ambosSon0PM _ _ = False



-- f)
mismoIntervalo :: Float -> Float -> Bool       -- En esta materia, vamos a usar el tipo de dato "Float" para representar números reales.
mismoIntervalo x y
    | (x <= 3) && (y <= 3)         = True
    | (3 < x) && (x <= 7) && (3 < y) && (y <= 7) = True
    | (7 < x) && (y < 7)           = True
    | otherwise = False


-- g)
sumaDistintos :: Int -> Int -> Int -> Int
sumaDistintos x y z
    | x /= y && y /= z && x /= z = x + y + z
    | x == y && y == z = 0                               -- O también podemos especificarlo como "undefined"
    | x == y = z
    | y == z = x
    | otherwise = y                                      -- "x == z = y"



-- h)
esMultiploDe :: Int -> Int -> Bool       -- Vamos a representar a los naturales con "Int"
esMultiploDe x y
    | x `mod` y == 0 = True
    | otherwise = False


-- i)
digitoUnidades :: Int -> Int
digitoUnidades x = (abs(x)) `mod` 10


-- j)

-- Forma 1:
{-
digitoDecenas :: Int -> Int
digitoDecenas y = (abs(y)) `mod` 100
-}


-- Forma 2:
digitoDecenas :: Int -> Int
digitoDecenas y
    | y < 10    = 0 
    | otherwise = div (ultimosDosDigitos - digitoUnidades ultimosDosDigitos) 10
    where ultimosDosDigitos = (abs(y)) `mod` 100 


-- Ejercicio 3

-- "RESUELTO" TAMBIÉN EN PAPEL.
estanRelacionados :: Int -> Int -> Bool
estanRelacionados a b
 | esMultiploDe a b = True
 | otherwise = False


-- Ejercicio 4
-- a)
prodInt :: (Float, Float) -> (Float, Float) -> Float
prodInt (a, b) (c, d) = a * c + b * d

-- b)
todoMenor :: (Float, Float) -> (Float, Float) -> Bool
todoMenor (o, p) (q, r)
 | o < q && p < r = True
 | otherwise = False


-- c)
distanciaPuntos :: (Float, Float) -> (Float, Float) -> Float        -- Recuerdo: dist (a1, a2) (b1, b2) = sqrt ((a1 - b1)² + (a2 - b2)²)
distanciaPuntos (a, b) (c, d) = sqrt ((a - c)**2 + (b - d)**2)


-- d)
sumaTerna :: (Int, Int, Int) -> Int
sumaTerna (a, b, c) = a + b + c

-- e)
sumarSoloMultiplos :: (Int, Int, Int) -> Int -> Int
sumarSoloMultiplos (a, b, c) z
    | esMultiploDe a z && esMultiploDe b z && esMultiploDe c z = a + b + c
    | esMultiploDe a z && esMultiploDe c z = a + c
    | esMultiploDe a z && esMultiploDe b z = a + b
    | esMultiploDe b z && esMultiploDe c z = b + c
    | esMultiploDe a z = a
    | esMultiploDe b z = b
    | esMultiploDe c z = c
    | otherwise = 0

sumarSoloMultiplosAux :: Int -> Int -> Int
sumarSoloMultiplosAux x y
    | esMultiploDe x y = x
    | otherwise = 0

sumarSoloMultiplos2 :: (Int, Int, Int) -> Int -> Int
sumarSoloMultiplos2 (x, y, z) a = sumarSoloMultiplosAux x a + sumarSoloMultiplosAux y a + sumarSoloMultiplosAux z a


sumarSoloMultiplosRecursion :: [Int] -> Int -> Int
sumarSoloMultiplosRecursion [] z = 0
sumarSoloMultiplosRecursion [x] z = sumarSoloMultiplosAux x z
sumarSoloMultiplosRecursion (x:xs) z = sumarSoloMultiplosAux x z + sumarSoloMultiplosRecursion xs z


-- f)
esPar :: Int -> Bool
esPar x
    | ((x `mod` 2) == 0) = True
    | otherwise          = False

posPrimerPar :: (Int, Int, Int) -> Int
posPrimerPar (x, y, z)
    | esPar x == True = 0
    | esPar y == True = 1
    | esPar z == True = 2
    | otherwise = 4


-- g)
crearPar :: a -> b -> (a, b)
crearPar a b = (a, b)

-- h)
invertir :: (a, b) -> (b, a)
invertir (a, b) = (b, a)



-- Ejercicio 5:
f2 :: Int -> Int
f2 n
 | n <= 7 = n*n    -- n^2
 | otherwise = 2*n - 1


g2 :: Int -> Int
g2 n
 | esPar n == True = div n 2
 | otherwise = 3*n + 1


todosMenores :: (Int, Int, Int) -> Bool
todosMenores (a, b, c)
    | (f2(a) > g2(a)) && (f2(b) > g2(b)) && (f2(c) > g2(c)) = True
    | otherwise = False


-- Ejercicio 6:
bisiesto :: Int -> Bool
bisiesto a
    | mod a 4 /= 0 = False
    | mod a 100 == 0 && mod a 400 /= 0 = False
    | otherwise = True



-- Ejercicio 7:
absolutoF :: Float -> Float          -- F de Float :u
absolutoF f = abs(f)

distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (a, b, c) (x, y, z) = absolutoF (a - x) + absolutoF (b - y) + absolutoF (c - z)



-- Ejercicio 8:
sumaUltimosDosDigitos :: Int -> Int
sumaUltimosDosDigitos x
    | x < 10    = digitoUnidades x
    | otherwise = digitoUnidades x + div (digitoDecenas x) 10


comparar :: Int -> Int -> Int
comparar a b
    | sumaUltimosDosDigitos a < sumaUltimosDosDigitos b = 1
    | sumaUltimosDosDigitos a > sumaUltimosDosDigitos b = -1
    | otherwise = 0