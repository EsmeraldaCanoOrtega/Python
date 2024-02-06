# Bucle while: ("Recordemos que debe ser una condición cierta para que continue el bucle")
contador = 0

while contador < 3:
    print(contador)
    contador += 1 #contador = contador + 1
else:
    print(f'Fin ciclo while el contador es {contador}')

# Bucle for-each: (Recorre cada caracter o elemento de la lista, en este caso un Array)
word = 'Hello there'

for letter in word:
    print(letter)
else:
    print(word)

# For i: cifra inicial, cifra final -1, cantidad que suma por bucle finalizado
for i in range(0,-11,-2):
    print(f'Valor: {i}')

# - Break, rompe el bucle y no realiza el else
for letra in 'Holanda':
    if letra == 'a':
        print(f'Letra encontrada: {letra}')
        break
else:
    print('Fin ciclo for')

# - Continue realiza el siguiente el elemento del bucle
#   pero no realiza las siguientes lineas de codigo

for i in range(6):
    if i % 2 != 0:
        continue
    print(f'Valor: {i}')