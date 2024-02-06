#   📌ABC = Abstract Base Class  --> Importamos esta clase📌
from abc import ABC, abstractmethod

#   CLASE FIGURA
#   📌class FiguraGeometrica(ABC)📌
class FiguraGeometrica(ABC):
    def __init__(self, alto, ancho):
        self._alto = alto
        self._ancho = ancho

    #   📌Metodo que queramos obligar a que poseen este metodo sus hijas📌
    @abstractmethod
    def calcular_area(self):
        pass

    #   GET
    @property
    def get_alto(self):
        return self._alto

    #   SETTER
    @get_alto.setter
    def set_alto(self, alto):
        self._alto = alto

    #  GET
    @property
    def get_ancho(self):
        return self._ancho

    #   SETTER
    @get_ancho.setter
    def set_ancho(self, ancho):
        self._ancho = ancho

    #   TO STRING
    def __str__(self):
        return f'alto: {self._alto} ancho:{self._ancho}'


#   CLASE COLOR
class Color(object):
    def __init__(self, color):
        self._color = color

    #   GET
    @property
    def get_color(self):
        return self._color

    #   SETTER
    @get_color.setter
    def set_color(self, color):
        self._color = color

    #   TOSTRING
    def __str__(self):
        return f'color: {self._color}'


#   CLASE RECTANGULO HIJA DE FiguraGeometrica Y Color
class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, ancho, alto, color):
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)

    def calcular_area(self):
        return self._alto * self._ancho

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'


#   CLASE CUADRADO HIJA DE FiguraGeometrica Y Color
class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        return self._alto * self._ancho

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'


print('Creación Objeto cuadrado'.center(50, '-'))
cuadrado1 = Cuadrado(lado=5, color='rojo')
print(f'Cálculo área cuadrado: {cuadrado1.calcular_area()}')
print(cuadrado1)

print('Creación Objeto rectángulo'.center(50, '-'))
rectangulo1 = Rectangulo(ancho=9, alto=8, color='verde')
rectangulo1.ancho = 15
print(f'Cálculo área rectángulo: {rectangulo1.calcular_area()}')
print(rectangulo1)

# MRO - Method Resolution Order
#   📌 Los metodos que se llaman igual, por ejemplo str se realizará con el siguiente orden
#   Cuadrado, FiguraGeometrica,Abstracta(ABC), Color y finalmente la clase object .mro [<class 'MultiHerencia.Cuadrado'>, <class 'MultiHerencia.FiguraGeometrica'>, <class 'MultiHerencia.Color'>, <class 'object'>]
#   Este orden se debe a la siguiente sentencia --> class Cuadrado(FiguraGeometrica, Color):
#   class Cuadrado(Color, FiguraGeometrica):    --> Cuadrado, Color, FiguraGeometrica, Abstracta(ABC), object
print(Cuadrado.mro())
