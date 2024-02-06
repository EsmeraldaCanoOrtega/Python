from DispositivoEntrada import DispositivoEntrada
class Raton(DispositivoEntrada):
    contador_ratones = 0

    @classmethod
    def _generarSiguienteValor(cls):
        cls.contador_ratones +=1
        return cls.contador_ratones

    def __init__(self, tipoEntrada, marca):
        super().__init__(tipoEntrada, marca)
        self._Id = Raton._generarSiguienteValor()

    def __str__(self):
        return f'Ratón: Id: {self._Id}, {super().__str__()}'

    @property
    def Id(self):
        return self._Id

class Teclado(DispositivoEntrada):
    contador_teclados = 0

    @classmethod
    def _generarSiguienteValor(cls):
        cls.contador_teclados +=1
        return cls.contador_teclados
#   📌 Ojito con el orden de parametros en los constructores
    def __init__(self,  marca,tipoEntrada,):
        super().__init__(marca,tipoEntrada)
        self._Id = Teclado._generarSiguienteValor()

    def __str__(self):
        return f'Teclado: Id: {self._Id}, {super().__str__()}'

    @property
    def Id(self):
        return self._Id