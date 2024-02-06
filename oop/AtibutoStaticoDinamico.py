class MiClase:
#   Atributo estatico
    variable_clase = 'Variable clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

#   Podemos imprimir el atributo de una clase
print(MiClase.variable_clase)
#   objeto 1 y como accede a su propio atributo(instancia) y al de todos los objetos(clase)
objeto1 = MiClase('Variable del primer objeto')
print(objeto1.variable_instancia)
print(objeto1.variable_clase)
#   objeto 2
objeto2 = MiClase('Variable del segundo objeto')
print(objeto2.variable_instancia)
print(objeto2.variable_clase)

#   La siguiente sentencia define un nuevo atributo estatico sin tener que crearlo en la clase
MiClase.variable_clase2 = 'Valor variable clase 2'

#   Los dos objetos pueden acceder al nuevo atributo estatico sin estar definido en la propia clase
print(MiClase.variable_clase2)
print(objeto1.variable_clase2)
print(objeto2.variable_clase2)
