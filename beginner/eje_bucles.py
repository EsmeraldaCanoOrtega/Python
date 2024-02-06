# Ejercicio 1; iterar un rango de 0 a 10 e imprimir numeros divisibles entre 3.

for i in range(0,11):
    if i % 3 != 0:
        continue
    print(f'Valor: {i}')

# Ejercicio 2; crear un rango de numeros de 2 a 6, e imprimelos.

for i in range(2,7):
    if i % 2 != 0:
        continue
    print(f'Valor: {i}')

# Ejercicio 3; crear un rango de 3 a 10, pero con incremento 2 en 2, en lugar de un 1 en 1

for i in range(3,11,2):
    print(f'Valor: {i}')