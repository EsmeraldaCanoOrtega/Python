"""1.- funcion que devuelve un string a nuestra terminal
print("Esta cadena se esta ejecutando porque tenemos el ejecutable en nuestra "
      "libreria que esta /venv/Scripts/python.exe")"""

num_1 = 20
# Pide por terminal al usuario input() y nos devuelve un valor de tipo String o cadena de caracteres
# lo casteamos al tipo de dato float() porque si son enteros al dividir arroja una excepción
num_2 = float(input('Introduce un numero: '))
result = num_1 / num_2

# Las tres maneras de visualizar cadenas, variables y como concatenarlas
print("El resultado de",num_1,"entre",num_2,"es",result)
print("El resultado de",num_1,"entre",num_2,"es",(num_1/num_2))
# redondear o truncar solo dos decimales var:.2f
print(f'El resultado de {num_1} entre {num_2} es {result:.2f}')

# Esta es la direccion de memoria(hexadecimal) de la variable result con la funcion id()
print(id(result))

# 3.- En este caso, "telephono: int", es una pista del dato que va a recibir
#     pero aun asi no lo estamos typando
#     por ejemplo si le asignamos el valor False, print(type(telephono))
#     nos indicará que la variable telephono es de tipo booleano
telephono: str
telephono: int = False
print(telephono)
print(type(telephono))

# 4.- Concatenar variables

firstName = "Esmeralda"
surname = "Caño Ortega"
name = firstName + " " + surname
print(firstName,surname)
print(firstName+" "+surname)

# 5.- Condicionales true or false
es_mayor = 3>0
if es_mayor:
      print("Si es mayor")
else:
      print("No es mayor")
# Operador ternario
print("Si es mayor" if es_mayor else "No no es mayor")