import psycopg2

def abrirconexion():
            conexion  = psycopg2.connect(
            host      = 'localhost',
            database  = 'ejemplo1',
            user      = 'postgres',
            password  = '1234',
            )
            return conexion


