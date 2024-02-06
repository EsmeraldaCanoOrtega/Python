class Monitor():
    contador_monitores =0

    @classmethod
    def _generarSiguienteValor(cls):
        cls.contador_monitores +=1
        return cls.contador_monitores
    def __init__(self,marca,tamanno):
        self._id = Monitor._generarSiguienteValor()
        self._marca = marca
        self._tamanno = tamanno

    def __str__(self):
        return f'Monitor: Id: {self._id}, marca: {self._marca}, tamaño: {self._tamanno}'
    
    @property
    def id(self):
        return self._id
    @property
    def tamanno(self):
        return self._tamanno
    @tamanno.setter
    def tamanno(self,tamanno):
        self._tamanno =tamanno
    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca
