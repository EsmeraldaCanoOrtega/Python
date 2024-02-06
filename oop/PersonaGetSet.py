class Persona:
    # __init__ Para crear un objeto
    def __init__(self, nombre, apellido, edad):
    #   .nombre es publico, se puede reasignarse y obtener cuando quieras
    #   ._nombre es privado, se puede reasignarse y obtener (señal al programador)
    #   .__nombre es privado, NO se puede reasignarse y obtener
        self._nombre = nombre
        self._apellido = apellido
        self.edad = edad

    # __del__ Para eliminar un objeto
    def __del__(self):
        print(f'Persona eliminada: {self._nombre} {self._apellido}')

# GET: @property es un indicativo o decorado para realizar el metodo get
    @property
    def nombre(self):
        print('Llamando método get nombre')
        return self._nombre

# SET: @nombre esta llamando al metodo get y esta obteniendo su valor
    @nombre.setter
    def nombre(self, nombre):
        print('Llamando método set nombre')
        self._nombre = nombre

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self._apellido} {self.edad}')

print(__name__)
if __name__ == '__main__':
    persona1 = Persona('Juan', 'Perez', 28)
    persona1.nombre = 'Juan Carlos'
    persona1.apellido = 'Lara'
    persona1.edad = 30
    persona1.mostrar_detalle()
