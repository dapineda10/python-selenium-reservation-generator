import json

import psycopg2
import os


class bd:

    def OpenConnection(self):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'credentials.json')
        try:
            with open(filename) as credentials_file:
                credentials = json.load(credentials_file)
            # Como la conexión devuelve un diccionario podemos convertirlo fácilmente

            # Llamado de la función con **Kward ya que se recibe una lista de argumentos
            try:
                conexion = psycopg2.connect(**credentials)
                conexion.cursor()
                return conexion
            except Exception as e:
                print("Ocurrió un error al conectar a PostgreSQL: ", e)
        except:
            print("No fue posible realizar la conexión, revise la ruta del archivo credentials.json")
