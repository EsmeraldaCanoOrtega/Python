class AreaBaseAlt:
#   Metodo para calcular el area
    def calcularArea(self):
        self.area = self.base * self.altura
        print(f'El area rectangulo es: {self.area}')

#   Constructor sirve para instanciar un objeto y que atributos va a poseer
    def __init__(self):
        self.base = int(input('Proporciona la base: '))
        self.altura = int(input('Proporciona la altura: '))
        self.calcularArea()

#   Instanciamos el objeto 'objeto1'
objeto1 = AreaBaseAlt()