#  👇CLASE COMPLEJAS HEREDAN DE DOS CLASES ABAJO DEL TODO👇
#   CLASE FIGURA
class FiguraGeometrica(object):
    def __init__(self,alto,ancho):
        self._alto= alto
        self._ancho= ancho
#   GET
    @property
    def get_alto (self):
        return self._alto
#   SETTER
    @get_alto.setter
    def set_alto (self,alto):
        self._alto=alto
#  GET
    @property
    def get_ancho(self):
        return self._ancho
#   SETTER
    @get_ancho.setter
    def set_ancho(self,ancho):
        self._ancho= ancho

#   TO STRING
    def __str__(self):
        return f'alto: {self._alto} ancho:{self._ancho}'

#   CLASE COLOR
class Color(object):
    def __init__(self,color):
        self._color=color
#   GET
    @property
    def get_color (self):
        return self._color
#   SETTER
    @get_color.setter
    def set_color(self,color):
        self._color=color
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
    def __init__(self, lado,color):
        # super().__init__(lado) --> 'Si solo heredara de una clase'
#   📌Aqui inicializa los valores alto y ancho aunque le hayamos llamado 'lado, lado'📌
#   📌lo realiza por posición de los atributos que inicializamos📌
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        return self._alto * self._ancho

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'