a = int(input('Escribe un valor numérico: '))

#print(a % 2)
if a % 2 == 0:
    print(f'El valor de a {a} es número par')
else:
    print(f'El valor de a {a} es número impar')

print(f'El valor de a {a} es número par' if a % 2 == 0 else f'El valor de a {a} es número impar')

result = f'El valor de a {a} es número par' if a % 2 == 0 else f'El valor de a {a} es número impar'

print(result)