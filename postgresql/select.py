import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='root',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)
#📌1 manera mayor utilizada con el uso de with
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM hospitales'
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            print(registros)
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()

#📌2 manera sin el uso de with
'''cursor = conexion.cursor()
sentencia = 'SELECT * FROM hospitales'
cursor.execute(sentencia)
registros = cursor.fetchall()
print(registros)

📌 HAY CERRAR TANTO EL CURSOR COMO LA CONEXION sin el uso de WITH
cursor.close()
conexion.close()'''