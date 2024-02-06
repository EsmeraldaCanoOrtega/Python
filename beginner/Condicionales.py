edad = int(input('Introduce tu edad: '))

'''veintes = edad >= 20 and edad < 30
print(veintes)
treintas = edad >= 30 and edad <40
print(treintas)
'''
# edad >= 20 and edad < 30 para quitar el and y la misma variable se compara dos veces
# se alterna como este caso los operadores 20 <= edad
if ( 20 <= edad < 30) or (30 <= edad <40):
    print('Dentro de rango (20\'s) o (30\'s)')
else:
    print("No está dentro de los 20's ni 30's")

''' if veintes:
       print('Dentro de los 20\'s')
    elif treintas:
        print('Dentro de los 30\'s')
    else:
        print('Fuera de rango')'''

result ='Dentro de rango (20\'s) o (30\'s)' if( 20 <= edad < 30) or (30 <= edad <40) else "No está dentro de los 20's ni 30's"
print(result)