# GEI-LP (edició 2020-2021 Q2): Logo3D 🐢

Implementacio d'un intèrpret d'un llenguatge de programació anomenat Logo3D per permetre pintar amb una tortuga en 3D.

## Instalación 🔧

Per instalar les llibreries necessaries per executar el programa fem servir la comanda: 

```
$ pip install -r requirements.txt
```

## Compilacio 🖥

Abans de poder utilitzar l'interpret l'haurem de compilar perquè generi els arxius que fara servir el main.

Ho fem amb la següent comanda:

```
$ antlr4 -Dlanguage=Python3 -no-listener -visitor logo3d.g
```

## Execució 🚀

Per executar el programa fem servir:
```
$ python3 logo3d.py input_file.l3d
```

Per defecte s'executa el programa partint del **main**, si volem que es començi desde qualsevol altre dels procediments haurem de utilitzar:
```
$ python3 logo3d.py input_file.l3d procediment param1 param2..
```
On el procedmient pot ser tant de la input file com una de les funcions de Turtle3D, seguida de els seus paràmetres.


Esta inclós a la carpeta l'arxiu *test-01.l3d*, un exemple de input_file


## Autor ✒️



* **Miquel Gotanegra Estañol** 
