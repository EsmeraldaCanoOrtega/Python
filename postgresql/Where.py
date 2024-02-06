import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='root',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM hospitales WHERE codhos = %s AND reghos = %s'
# Las consultas deben recibir un string para que funcione
            codhos_user = input('Proporciona el valor codigo hospital: ')
            reghosuser ='Centro'
            cursor.execute(sentencia, (codhos_user,reghosuser))
#📌 metodo fetchone solo devuelve un registro
# en cambio fetchall devuelve todos los registros que coincidan con la consulta
            registros = cursor.fetchone()
            print(registros)
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()