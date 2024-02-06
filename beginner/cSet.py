# Es un tipo de lista de Colecciones, pero con una serie de matices
# Los valores no se localizan por rango sino por valor
# Los valores deben ser unicos

planetas = {'Marte', 'Júpiter', 'Venus'}
print(planetas)
#largo como .length
print(len(planetas))
# Devuelve un booleano True or false si encuentra el siguente elemento
print('Marte' in planetas)
# agregar un elemento
planetas.add('Tierra')
print( planetas)
# no se pueden duplicar elementos, es decir aunque pongas de nuevo .add no va a hacer nada
planetas.add('Tierra')
print(planetas)
# eliminar elemento, devuelve un error si el elemento no ha sido encontrado
planetas.remove('Tierra')
print(planetas)
# eliminar elemento, posee una excepcion para que no devuelva un error si el elemento no ha sido encontrado
planetas.discard('Júpiters')
print(planetas)
# vaciar el elemento planeta de valores
planetas.clear()
print(planetas)
# eliminar el set
del planetas