# 📌Esta clase sirve para lanzar(raise) excepciones porque hereda de Exception tb con baseException
class NumerosIdenticosException(Exception):

    def __init__(self, mensaje):
        self.message = mensaje

resultado = None
try:
    a = int(input('Primer número: '))
    b = int(input('Segundo número: '))
    if a == b:
    # 📌raise ValueError('error de valor')   --> lanzar un mensaje sin necesidad de crear una clase
        raise NumerosIdenticosException('números indénticos')
    resultado = a/b
# 📌Hay que ordenar las excepciones segun por ambiguedad, es decir la ultima la clase padre Exception
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrió un error: {e} , {type(e)}')
except TypeError as e:
    #📌 Se puede escribir código  en las excepciones para tratarlo de diferente manera
    # o invocar otras excepciones dentro de la excepción
    print(f'TypeError - Ocurrió un error: {e} , {type(e)}')
except Exception as e:
    print(f'Exception - Ocurrió un error: {e} , {type(e)}')
else:
    print('No se arrojó ninguna excepción')
# 📌finally Se va a ejecutar tanto que salga una excepción o no(else)
finally:
    print('Ejecución del bloque finally')

print(f'Resultado: {resultado}')
print('Continuamos...')