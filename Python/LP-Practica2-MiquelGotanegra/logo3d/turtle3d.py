from vpython import *
import math


class Turtle3D:

    def __init__(self):  # constructor
        scene.height = scene.width = 1000
        scene.autocenter = True

        self.trotu = sphere(pos=vector(0, 0, 0), radius=0.2, color=color.red)
        self.trail = True
        self.rgb = self.trotu.color

        self.alpha = 0.0
        self.beta = 0.0

        self.dir = vec(1, 0, 0)

        # descomentar per mostrar els eixos de coordenades
        #arrow(pos=vector(0, 0, 0), axis=vector(20, 0, 0), round=False, shaftwidth=self.trotu.radius*0.3, headwidth=0.3,color=color.red)
        #arrow(pos=vector(0, 0, 0), axis=vector(0, 20, 0), round=False, shaftwidth=self.trotu.radius*0.3, headwidth=0.3,color=color.green)
        #arrow(pos=vector(0, 0, 0), axis=vector(0, 0, 20), round=False, shaftwidth=self.trotu.radius*0.3, headwidth=0.3,color=color.blue)

    def forward(self, units):
        """la tortuga avança 'units' passos en la direccio a la que estigui mirant """

        ini = self.trotu.pos
        final = ini + self.dir*units
        v = final - ini

        if (self.trail):
            self.trotu.clone()
            cylinder(pos=self.trotu.pos, axis=v,
                     radius=self.trotu.radius, color=self.rgb)
        self.trotu.pos = final

    def backward(self, units):
        """la tortuga avança 'units' passos en la direccio contraria a la que estigui mirant"""
        self.forward(-units)

    def rot(self, a, b):
        """funcio que rota el vector de direccio dir respecte els angles a(horitzontal) i b (vertical)"""
        self.alpha += math.radians(a)
        self.beta += math.radians(b)

        x = math.cos(self.alpha) * math.cos(self.beta)
        z = math.sin(self.alpha) * math.cos(self.beta)
        y = math.sin(self.beta)

        self.dir = vec(x, y, z)

    def right(self, a):
        """gira la direccio en la que mira la tortuga 'a' graus cap a la dreta respecte l'eix vertical"""
        self.rot(a, 0)

    def left(self, a):
        """gira la direccio en la que mira la tortuga 'a' graus cap a l'esquerra respecte el eix veritcal"""
        self.rot(-a, 0)

    def up(self, b):
        """gira la direccio en la que mira la tortuga en 'b' graus cap a dalt respecte l'eix horitzontal"""
        self.rot(0, b)

    def down(self, b):
        """gira la direccio en la que mira la tortuga en 'b' graus cap a baix respecte l'eix horitzontal"""
        self.rot(0, -b)

    def color(self, r, g, b):
        """cambia el color de la tortuga i de l'estela per als proxims moviments a un color en format rgb"""
        self.trotu.color = vec(r, g, b)
        self.rgb = vec(r, g, b)

    def hide(self):
        """fa que a partir dels proxims moviments la tortuga no deixi cap estela"""
        self.trail = False

    def show(self):
        """fa que a partir dels proxims moviments la tortuga deixi una estela (es ja per defecte)"""
        self.trail = True

    def home(self):
        """retorna la tortuga a la posició inicial mirant cap el eix (1,0,0)"""

        # comentar si volem que al fer home() no s'ens faci reset al vector direccio
        self.alpha = 0.0
        self.beta = 0.0
        self.dir = vec(1, 0, 0)

        # la pintem perque no quedi un cilindre sense arrodonir quan la movem
        self.trotu.clone()

        self.trotu.pos = vec(0, 0, 0)
