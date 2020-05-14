import datetime

from Project.db.bd import bd


class DatabaseQueries:

    def InsertReservation(self, itinerary, type_reservation, occupancy):
        """Inserta en bd los itinerarios creados.

        :param occupancy:
        :param itinerary:
        :param type_reservation:
        :return:
        """
        conexion = bd()
        conection = conexion.OpenConnection()

        try:
            with conection.cursor() as cursor:
                consulta = "INSERT INTO reservation(code, date_creation, code_request, occupancy) VALUES (%s, %s, %s, %s);"

                print('Se insertó el registro en bd con código de itinerario_' + itinerary)

                cursor.execute(consulta,
                               (itinerary, datetime.datetime.now(), type_reservation, occupancy))
                conection.commit()

        except Exception as e:
            print("Ocurrió un error al insertar: ", e)
        finally:
            conection.close()
