# Dada la siguiente tupla
numeros = (13, 1, 8, 3, 2, 5, 8)
# crear una lista con valores menos a 5
numsmenores5 = []
for numero in numeros:
    if numero <5:
        numsmenores5.append(numero)
print(numsmenores5)