grammar logo3d;


root : func* EOF ;

func: 'PROC ' WORD '(' ( (WORD ',')* WORD | ) ')' ' IS' lines* 'END';

lines: assig
    |lectura
    |escriptura
    |condicional
    |wbucle
    |fbucle
    |procediment
    ;

assig: WORD ':=' expr;

procediment: WORD '(' ( (expr ',')* expr | ) ')';

lectura: '>>' WORD;

escriptura: '<<' expr;

condicional : 'IF' expr 'THEN' lines* ('ELSE' lines*)? 'END';

wbucle: 'WHILE' expr 'DO' lines* 'END';

fbucle: 'FOR' WORD 'FROM' var 'TO' var 'DO' lines* 'END';

expr : expr '*' expr   #Mul
    | expr '/' expr    #Div
    | expr '+' expr    #Sum
    | expr '-' expr    #Res
    | var              #NonOp
    | expr '==' expr   #Eq
    | expr '!=' expr    #nEq
    | expr '<' expr     #Lt
    | expr '>' expr     #Gt
    | expr '<=' expr    #Lte    
    | expr '>=' expr    #Gte
    ;


var :FLOAT #Float
    |INT #Int
    |WORD #Word
    ;



COMMENT : '//' ~[\r\n]* -> skip;
WORD : [a-zA-Z]+ ([0-9]+ | [a-zA-Z]+ |'_')* ;
INT: [0-9]+ ;
FLOAT : [0-9]+ '.' [0-9]* ;
WS : [ \n]+ -> skip ;