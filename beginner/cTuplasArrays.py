# Definir una tupla () es como un array
# pero no se puede reasignar cada uno de sus elementos
frutas = ('Naranja', 'Plátano', 'Guayaba')

# navegación inversa
print(frutas[-1])

# acceder a un rango
print(frutas[0:1])# sin incluir el último índice

#recorrer elementos end modifica que en vez halla un salto de linea sino un espacio entre estos
for fruta in frutas:
    print(fruta, end=' ')

# cambiar valor tupla
# frutas[0] = 'Pera' NO SE PUEDE REASIGNAR
# Para cambiar el valor a una tupla hay que cambiarlo a lista
frutasLista = list(frutas)
frutasLista[0] = 'Pera'
frutas = tuple(frutasLista)

print('\n',frutas)

#eliminar la tupla
del frutas