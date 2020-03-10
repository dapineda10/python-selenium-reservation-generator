import json

import psycopg2


class bd:

    def OpenConnection(self):
        with open(r"C:\Users\usuario\PycharmProjects\Headless\db\credentials.json") as credentials_file:
            credentials = json.load(credentials_file)
        # Como la conexión devuelve un diccionario podemos convertirlo fácilmente

        # Llamado de la función con **Kward ya que se recibe una lista de argumentos
        try:
            conexion = psycopg2.connect(**credentials)
            conexion.cursor()
            return conexion
        except Exception as e:
            print("Ocurrió un error al conectar a PostgreSQL: ", e)
