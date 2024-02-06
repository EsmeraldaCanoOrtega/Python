# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4 * 3 * 2
# 5! = 5 * 4 * 6
# 5! = 5 * 24
# 5! = 120
def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)
def numerosDesc (numero = 0):
    if numero >= 1 :
        print(numero)
        return numerosDesc(numero - 1)

numerosDesc(0)
numero = 5
resultado = factorial(numero)
print(f'El factorial de {numero} es {resultado}')