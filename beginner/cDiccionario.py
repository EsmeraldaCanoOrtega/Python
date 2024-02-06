# dict (key, value)
diccionario = {
    'IDE':'Integrated Development Environment',
    'OOP':'Object Oriented Programming',
    'DBMS':'Database Management System'
}
print(diccionario)
#largo
print(len(diccionario))
# acceder a un elemento (key)
print( diccionario['IDE'])
# otra forma de recuperar un elemento
print(diccionario.get('OOP'))
# reasignando el valor de un elemento
diccionario['IDE'] = 'integrated development environment'
print(diccionario)
# recorrer los elementos
for clave, valor in diccionario.items():
    print(clave, valor)

for clave in diccionario.keys():
    print(clave)

for valor in diccionario.values():
    print(valor)

# comprobar existencia de algún elemento
print('IDE' in diccionario)

# agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

# remover un elemento
diccionario.pop('DBMS')
print(diccionario)

# limpiar
diccionario.clear()
print(diccionario)

# eliminar el diccionario
del diccionario