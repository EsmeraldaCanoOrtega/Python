from RatonTeclado import Raton, Teclado
from Monitor import Monitor


class Computadora():
    contador_computadoras = 0

    @classmethod
    def _generarSiguienteValor(cls):
        cls.contador_computadoras += 1
        return cls.contador_computadoras

    def __init__(self, nombre, monitor, teclado, raton):
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton
        self._id = Computadora._generarSiguienteValor()

    def __str__(self):
        return f'{self._nombre}: {self._id}' \
               f'\n\t{self._monitor}' \
               f'\n\t{self._teclado}' \
               f'\n\t{self._raton}'


if __name__ == '__main__':
    teclado1 = Teclado('HP', 'USB')
    raton1 = Raton('HP', 'USB')
    monitor1 = Monitor('HP', 15)
    computadora1 = Computadora('HP', monitor1, teclado1, raton1)
    print(computadora1)
    teclado2 = Teclado('Acer', 'Bluetooth')
    raton2 = Raton('Acer', 'Bluetooth')
    monitor2 = Monitor('Acer', 27)
    computadora2 = Computadora('Acer', monitor2, teclado2, raton2)
    print(computadora2)
