grammar Expr;
root : expr EOF ;
expr : expr MES expr
    | NUM
    ;
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