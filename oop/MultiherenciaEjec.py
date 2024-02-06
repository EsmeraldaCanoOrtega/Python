from MultiHerencia import Cuadrado,Rectangulo
print('Creación Objeto cuadrado'.center(50,'-'))
cuadrado1 = Cuadrado(lado=5, color='rojo')
print(f'Cálculo área cuadrado: {cuadrado1.calcular_area()}')
print(cuadrado1)

print('Creación Objeto rectángulo'.center(50,'-'))
rectangulo1 = Rectangulo(ancho=9, alto=8, color='verde')
rectangulo1.ancho = 15
print(f'Cálculo área rectángulo: {rectangulo1.calcular_area()}')
print(rectangulo1)

# MRO - Method Resolution Order
#   📌 Los metodos que se llaman igual, por ejemplo str se realizará con el siguiente orden
#   Cuadrado, FiguraGeometrica, Color y finalmente la clase object .mro [<class 'MultiHerencia.Cuadrado'>, <class 'MultiHerencia.FiguraGeometrica'>, <class 'MultiHerencia.Color'>, <class 'object'>]
#   Este orden se debe a la siguiente sentencia --> class Cuadrado(FiguraGeometrica, Color):
#   class Cuadrado(Color, FiguraGeometrica):    --> Cuadrado, Color, FiguraGeometrica, object
print(Cuadrado.mro())