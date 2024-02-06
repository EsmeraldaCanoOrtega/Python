#   CLASE PERSONA
class Persona:
#   def __init__(self, nombre, apellido, edad, *valores, **terminos):
#   *valores pasamos por parametros una tupla, **terminos un diccionario
    def __init__(self, nombre:str, edad):
        self.nombre = nombre
        self.edad = edad

#   __str__ realiza una sobrescritura, devuelve un string en vez una dirección de memoria al leer un objeto
    def __str__(self):
        return f'Persona[Nombre: {self.nombre}, Edad: {self.edad}]'
#        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')
#        persona1 = Persona('Juan', 'Perez', 28, '44553322', 2, 3, 5, m='manzana', p='pera')

#   CLASE EMPLEADO QUE HEREDA DE PERSONA
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def __str__(self):
        return f'Empleado[Sueldo: {self.sueldo}] {super().__str__()} '

persona1 = Persona('Juan', 28)
print(persona1)

# Este atributo aunque no pertenezca a la clase Persona se puede inicializarlo en el objeto
persona1.telefono = '55441122'
print(persona1.telefono)

empleado1 = Empleado('Karla', 30, 5000)
# Da un error porque este objeto no posee este atributo
#print(empleado1.telefono)
print(empleado1)