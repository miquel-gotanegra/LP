absValue :: Int -> Int
absValue x 
    | x >= 0    =  x
    | otherwise = -x

power :: Int -> Int -> Int
power x p = x^p

isPrime :: Int -> Bool 
isPrime 0 = False
isPrime 1 = False
isPrime 2 = True
isPrime n = not $ findDivisor 2
   where 
		nsqrt = isqrt(n)
		findDivisor i
			| i > nsqrt		= False
			| otherwise	= mod n i == 0 || findDivisor (i+1)
		
		
isqrt :: Int -> Int
	--part entera de l'arrel quadrada
isqrt n = floor (sqrt ( fromIntegral n))

slowFib :: Int -> Int 
slowFib 0 = 0
slowFib 1 = 1
slowFib n = slowFib (n-1) + slowFib (n-2) 


quickFib :: Integer -> Integer
quickFib n
    | n == 0 = 0
    | n == 1 = 1
    | otherwise = sumaFib 0 1 n
    where 
    	sumaFib x y z
    		| z == 2	= x + y
    		| otherwise = sumaFib y (y+x) (z-1)
    		
factorial :: Int -> Int
{- patern matching, agafa la primera branca amb la que coincideix el resultat -}

--factorial 0 = 1             
--factorial n = n*factorial(n-1) 
{- guardes on cada una es compon de | (condicio) = implicacio ; s'agafa la primera que compleix la condicio-}

factorial n
	| n==0 = 1
	| otherwise = n*factorial(n-1)
        
