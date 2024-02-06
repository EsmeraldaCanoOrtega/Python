try:
    # 📌with: garantiza que el archivo se cerrará automáticamente cuando se termine de usar
    # Esto crea un archivo y lanza un error si el archivo ya existe
    with open('prueba.txt', 'x', encoding='utf8') as archivo:
        # .write Reescribe todo lo que hubiera con anterioridad
        archivo.write('hola que ase\n')
        archivo.write('Adios')

except FileExistsError:
    # 📌Recuerda se utiliza ruta relativa o especifica
    #  archivo = open('c:\\Cursos\\Python\\Archivos\\Leccion01\\prueba.txt', 'r', encoding='utf8')
    with open('prueba.txt', 'r+', encoding='utf8') as archivo:

        # leer algunos caracteres
        # print(archivo.read(5))

        # leer linea completas (/n)
        # print(archivo.readlines())

        # print(type(archivo.read())) --> String
        # print(type(archivo.readlines()))  --> List
        # archivo.readlines()[-1] --> accediendo a la ultima linea de la lista

        # #iterar el archivo
        for linea in archivo:
            # el archivo es dinamico se acta
            print(linea)
            if linea == 'Adios':
                with open('prueba.txt', 'a', encoding='utf8') as archivo:
                    archivo.write('\nHasta addddddddddddhora')

        # 📌Una vez que lee caracteres o lineas no puede volver a leerlas

finally:
    print('Fin del archivo')