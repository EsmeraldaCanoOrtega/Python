from Computadora import Computadora
from Monitor import Monitor
from RatonTeclado import Teclado, Raton


class Orden:
    contador_ordenes = 0

    @classmethod
    def _generarSiguieneValor(cls):
        cls.contador_ordenes += 1
        return cls.contador_ordenes

    def __init__(self, computadora):
        self._id = Orden._generarSiguieneValor()
        self._computadora = list(computadora)

    def agregarComputadora(self, computadora):
        self._computadora.append(computadora)

    def __str__(self):
        strComputadoras = ''
        for computadora in self._computadora:
            strComputadoras = strComputadoras + '\n\t' + computadora.__str__()
        return f'Orden: {self._id};{strComputadoras}'



