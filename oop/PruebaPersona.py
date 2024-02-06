# Puedes importar varias clases que tenga este fichero con *
from PersonaGetSet import Persona

# Cuando importas un archivo aparte de ejecutar la clase Persona tb ejecutas el codigo
# Por eso aparece en la terminal PersonaGetSet print(__name__)
print(__name__)

# __main__ es el fichero donde estas ejecutando en ese momento el archivo
if __name__ == '__main__':
    print('Creación objetos'.center(30, '-'))
    persona1 = Persona('Karla', 'Gomez', 30)
    persona1.mostrar_detalle()

    print('Eliminación objetos'.center(30, '-'))
    del persona1

