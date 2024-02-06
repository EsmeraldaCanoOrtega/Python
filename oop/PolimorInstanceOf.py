class Empleado:

    def __init__(self, nombre, sueldo):
        self._nombre = nombre
        self._sueldo = sueldo

    def __str__(self):
        return f'Empleado: [Nombre: {self._nombre}, Sueldo: {self._sueldo}]'

    def mostrar_detalles(self):
        return self.__str__()
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,nombre):
        self._nombre=nombre
    @property
    def sueldo(self):
        return self._sueldo
    @sueldo.setter
    def sueldo(self,sueldo):
        self._sueldo=sueldo

class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self._departamento = departamento

    def __str__(self):
        return f'Gerente [Departamento: {self._departamento}] {super().__str__()}'
    @property
    def departamento(self):
        return self._departamento

#   📌Metodo aparte de las clases que nos indica el tipo del objeto y mostrar_detalles nos devuelve un string
def imprimir_detalles(objeto):
    print(type(objeto))
    print(objeto.mostrar_detalles())
#   📌Comprueba si este objeto es de tipo Gerente para evitar que nos de error al realizar un get de un atrubito no definido
#   Esto en Java solo lo podias poner en la clase padre en este caso Empleado
    if isinstance(objeto, Gerente):
        print(objeto.departamento)


empleado = Empleado('Juan', 5000)
imprimir_detalles(empleado)

gerente = Gerente('Karla', 6000, 'Sistemas')
imprimir_detalles(gerente)
