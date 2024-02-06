class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, otro):
        return f'{self.nombre} {otro.nombre}'

    def __sub__(self, otro):
        return self.edad - otro.edad


persona1 = Persona('Juan', 28)
persona2 = Persona('Carlos', 20)
print(persona1 + persona2)
print(persona1 - persona2)

'''Nombre de los metodos (más comunes) para operaciones de dos objetos de la clase.
__add__(self, other): Permite la sobrecarga del operador de adición +

__sub__(self, other): sustracción -

__mul__(self, other):  multiplicación *

__truediv__(self, other): división /

__floordiv__(self, other): división entera //

__mod__(self, other):  módulo % (resto de una division)

__pow__(self, other): potencia **

__lt__(self, other): menor que <

__le__(self, other):  menor o igual que <=

__eq__(self, other): igualdad ==

__ne__(self, other): desigualdad !=

__gt__(self, other): mayor que >

__ge__(self, other): mayor o igual que >=
'''