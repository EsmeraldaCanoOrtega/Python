# un * es para recibir una tupla
def sumarxnumeros (*numeros):
    total= 0
    for numero in numeros:
        total+=numero
    return total
# dos ** es para recibir por parametros un diccionario
def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')
# En la llamada de la funcion ajustas en el parametro si es un lista,String,tuple
def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)


nombres = ['Juan', 'Karla', 'Guillermo']
desplegarNombres(nombres)
desplegarNombres('Carlos')
desplegarNombres((8, 9))
desplegarNombres([10, 11])

resultado= sumarxnumeros(5, 5, 5, 5)
print(f'El resultado ha sido {resultado}')


listarTerminos(IDE='Integrated Developement Environment', PK='Primary Key')
listarTerminos(DBMS='Database Management System')