{-# LANGUAGE RecordWildCards #-}    -- per utilitzar fields

import Data.Char (isUpper)          -- ens diu si un Char es mayuscula o no

import Data.List (nub, isInfixOf)   {- 	nub [..] borra els duplicats de la llista
										isInfixOf [l1] [l2] retorna si l1 esta continguda a l2 o no
									-}

import Data.List.Split (splitOn)    -- splitOn "xy" "axybxyc" --> ["a","b","c"]
import Data.String.Utils (strip)    -- strip " a b " -> "a b" esborra els espais al principi o al final (no els del mitg)

import Data.Maybe (mapMaybe, fromMaybe) {-mapMaybe :: (a -> Maybe b) -> [a] -> [b]
											si la funcio retorna nothing, no s'afegeix a la llista
											si retorna Just b, b s'afegeix a la llista
										
										  fromMaybe :: a -> Maybe a -> a 
										  	si Maybe a es Nothing, retorna el valor per defecte (primer valor)
											si Maybe a es (Just a) retorna a
										-} 


type Programa = [ Regla ]

data Regla = Regla { _cap::Atom, _cos::[ Atom ] }
	deriving (Eq,Show)

data Atom = Atom { _nomPredicat::String, _termes::[ Term ] }
    deriving (Eq, Show)

data Term = Var String | Sym String
   deriving (Eq, Show)

type Sustitucio = [ (Term, Term) ]     -- [(variable, constant), (variable, constant), ...]

type BaseConeixement = [ Atom ]


-- %%%%%%%%% PARSE INPUT %%%%%%%%%


--transforma una llista de strings en una de termes
stringListToTerms:: [String] -> [Term] 
stringListToTerms [] = []
stringListToTerms a = map termify a
		where termify x
			| isUpper(head x) = Var x
			| otherwise = Sym x
			
atomize::String -> Atom --crea un atom en _cap es el primer element de s i cos la resta
atomize s = do
	let w = (words s)
	let predicat = (head w)
	let terms = stringListToTerms (tail w)
	 
	(Atom predicat terms)

-- progenitor X Z & ancestre Z Y => ancestre X Y
-- crea una regla amb els elements del string
reglify :: String -> Regla
reglify s = do
	let w = splitOn " => " s
	if( (length w) > 1) then do
		let ant = splitOn " & " (head w)
		let con = atomize(last w)

		(Regla con (map atomize ant))

	else
		(Regla (atomize (w!!0)) [])

stringsToPrograma :: [String] -> Programa
stringsToPrograma [""] = []
stringsToPrograma s = map reglify s

-- %%%%%%%%% UNIFICACIO %%%%%%%%%

sustitucioBuida :: Sustitucio
sustitucioBuida = []

sus:: Atom -> (Term,Term) -> Atom --funcio auxiliar de sustitueix
sus a (var,sym) = do
	let terms = _termes a
	let newTerms = [ if (x == var) then sym else x | x <- terms] -- per a cada terme de a, si coincideix am la sustitucio sustituim 
	(Atom (_nomPredicat a) newTerms) 

sustitueix :: Atom -> Sustitucio -> Atom
sustitueix atom [] = atom --aqui si poso sustitucioBuida en comptes de [] hem dona warning -Woverlapping-patterns
sustitueix atom (s:sx) = do -- si la llista no es buida
	let a = sus atom s -- fem la sustitucio del primer element de la llista i ho coloquem a "a"
	(sustitueix a sx) -- cridem recursivament a la funcio amb la resta d'elements de la llista i el atom tractat amb el primer

-- retorna si alguna variable te assignada dos constants diferents, suposant que no hi ha dos elements iguals a la llista
noRepes :: Sustitucio -> Bool 
noRepes [] = True
noRepes ((a,_):sx) = not (elem a (map fst sx)) && noRepes sx

-- retorna cert si es una parella de Symbols i fals si es (Var,Sym)
var:: (Term,Term) -> Bool
var (Sym _ ,Sym _) = False
var (Var _ ,_) = True

--retorna cert si els dos termes son iguals
iguals :: (Term,Term) -> Bool
iguals (a,b) = if (a==b) then True else False

-- si els atoms es poden unificar retorna Just Sustitucio, si no retorna Nothing
unifica :: Atom -> Atom -> Maybe Sustitucio
unifica atom1 atom2 = do
	if ((_nomPredicat atom1) /= (_nomPredicat atom2)) then Nothing
	else do
		let t1 = _termes atom1
		let t2 = _termes atom2
		let parelles = nub (zip t1 t2)

		let constants = filter (not.var) parelles
		let variables = filter var parelles

		if( length t1 == length t2 && and(map iguals constants) && noRepes variables ) then Just variables 
		else Nothing

--funcio auxiliar de avaluaAtom que ens torna una [Substitucio] on hi ha una sustitucio de les possibles i les sustitucions consecuents
eval:: BaseConeixement -> (Sustitucio,Atom) -> [Sustitucio]
eval kb (s,a) = do 
	[s++x | x<-(mapMaybe (unifica a) kb)] --afegim la sustitucio que ja hem fet al atom a la llista 
	

avaluaAtom :: BaseConeixement -> Atom -> [ Sustitucio ] -> [Sustitucio]
avaluaAtom kb atom [] = mapMaybe (unifica atom) kb
avaluaAtom kb atom llista = do
	let atomList = map (sustitueix atom) llista -- una llista del atom amb cada una de les sustitucins
	let aux = zip llista atomList
	concat (map(eval kb) aux)

-- %%%%%%%%% EVALUAR REGLES %%%%%%%%%

--funcio auxiliar de avaluaRegla que combina (quan sigui possible) les sustitucions de cada un dels antecedents
avReg:: BaseConeixement -> [Atom] -> [ Sustitucio ] -> [Sustitucio]
avReg kb [a] sus = avaluaAtom kb a sus
avReg kb (a:as) sus = do
	let newSus = avaluaAtom kb a sus
	avReg kb as newSus   


avaluaRegla :: BaseConeixement -> Regla -> BaseConeixement
avaluaRegla kb r = 
	if (_cos r == []) 
		then [_cap r]
	else do
		let susList = avReg kb (_cos r) []
		nub (map (sustitueix (_cap r)) susList)

-- %%%%%%%%% GENERAR KB %%%%%%%%%

consequencia :: Programa -> BaseConeixement -> BaseConeixement
consequencia pr kb = do
	let newKb = concat(map (avaluaRegla kb) pr)
	if kb == newKb 
		then newKb
	else consequencia pr newKb

-- %%%%%%%%%   OUTPUT 	%%%%%%%%%

data Sol = B Bool | Sus [Sustitucio]


check :: Programa -> Regla -> Sol
check pr q = do
	let kb = consequencia (pr ++ [q]) []
	let r = [x | x <- kb, (_nomPredicat x == "query")]
	if( _termes (_cap q) == [] ) 
		then 
		if(length r /= 0) 
			then B True
		else B False

	else do 
		let sol = avaluaAtom r (_cap q) []
		Sus sol

nameT::Term -> String 
nameT (Var s) = s 
nameT (Sym s) = s 


showS:: Sustitucio -> String
showS [] = ";"
showS ((Var a,Sym b):sx) = 

	" " ++ a ++ " = " ++ b ++  showS sx

showC:: Sol -> String
showC (B b) = show b 
showC (Sus []) = ""
showC (Sus (s:sx)) = do
	showS s ++ showC (Sus sx)



-- %%%%%%%%% 	MAIN 	%%%%%%%%%
main = do 
	x <- getContents
	
	let t = splitOn "end.\n" x --separa el programa de les querys

	let aux_prog = splitOn ".\n" (t !! 0) -- separa els atoms
	let aux_preg = splitOn ".\n" (t !! 1) -- separa els atoms

	let prog = [x| x<- aux_prog, x/="" ]
	let preg = [x| x<- aux_preg, x/="" ]
	
	let pr = stringsToPrograma prog
	let pg = stringsToPrograma preg

	let aux = map (check pr) pg

	let res = map (strip.showC) aux

	mapM_ putStrLn res


	
