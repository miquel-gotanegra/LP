data Queue a = Queue [a] [a]
 deriving (Show)

--crear una qua buida
create :: Queue a
create = (Queue [][])


push :: a -> Queue a -> Queue a

push a (Queue xs ys) = (Queue xs (a:ys)) 


{-
D’altra banda, l’operació d’avançar es fa treient el primer de la primera llista, si en té, i sinó,
 passant els de la segona llista cap a la primera (en l’ordre correcte) i agafant el primer tot deixant la resta.
 -}
pop :: Queue a -> Queue a -- ;D
pop (Queue [][]) = (Queue [][])
pop (Queue [] ys) = (Queue  (tail (reverse ys)) [] )
pop (Queue xs ys) = (Queue  (tail xs) ys)



top :: Queue a -> a -- ;D
--top (Queue [] []) = '0' ????????????
top (Queue [] ys) =  last ys
top (Queue xs ys) = head xs



empty :: Queue a -> Bool

empty (Queue [][]) = True
empty (Queue xs ys) = False



instance Eq a => Eq (Queue a)
 where (Queue xs ys) == (Queue as bs) =  xs ++ (reverse ys) == as ++ (reverse bs)