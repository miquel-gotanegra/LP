grammar E4;


root : func* EOF ;

func : write
	|assig
	;

assig: WORD EQ expr;

expr : expr MES expr	
    | NUM				
    | WORD				
    ;

write: WRITE WORD
	;


EQ : ' := ' ;
WRITE : 'write';
WORD : [a-zA-Z\u0080-\u00FF]+ ;
NUM : [0-9]+ ;
MES : '+' ;
WS : [ \n]+ -> skip ;

/*
grammar Expr;
root : expr EOF ;
expr : <assoc=right> expr EXP expr
    |expr MUL expr
    |expr DIV expr
    |expr MES expr
    |expr MENYS expr
    | NUM
    ;
NUM : [0-9]+ ;
MES : '+' ;
MENYS : '-' ;
MUL : '*' ;
DIV : '/' ;
EXP : '^' ;
WS : [ \n]+ -> skip ;

#La recursivitat va d'esquerra a dreta
#la multiplicacio te prioritat sobre la suma
# expr : expr '*' expr
#    | expr '+' expr
#    | INT
# ;

#si volem que la associativitat sigui de dreta a esquerra
#expr : <assoc=right> expr '^' expr
#    | INT
#    ;


*/