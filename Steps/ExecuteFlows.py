from Pages.ResultPage import ResultPage
from Pages.PassengerPage import PassengerPage
from Pages.CarsDetailsPage import CarsDetailsPage
from Pages.ExtraPage import ExtraPage
from Pages.PayPage import PayPage
from db.DatabaseQueries import *
import logging


class ExecuteFlows:

    def __init__(self, context):
        self.context = context

    def execute_process(self, type_request, occupancy):
        """ Ejecuta los procesos dependiendo del type_request.

        :param type_request: 1,2,3,4,5,6,7,8,9,10,11
        :param occupancy:
        :return:
        """
        if type_request in ['1', '2', '3', '4']:
            # 1. domestic 1r1a1i, 2. domestic 1r1a1c, 3. international 1r1a1i, 4. international 1r1a1c
            while True:
                execution = self.execute_flows_flight(type_request, occupancy)
                if execution:
                    break
                # Si sólo pasó página de pasajeros debe repetir el flujo hasta que sean minimo 4 intentos
                elif execution is False and self.context.repetitions >= 4:
                    print("No fue posible insertar en base de datos")
                    logging.error('No fue posible insertar en base de datos la petición #' + type_request)
                    break

        elif type_request in ['5']:
            # 5. domestic_package BOG-MED 1r1a
            while True:
                execution = self.execute_flow_domestic_package(type_request, occupancy)
                if execution:
                    break
                # Si sólo pasó página de pasajeros debe repetir el flujo hasta que sean minimo 4 intentos
                elif execution is False and self.context.repetitions == 4:
                    print("No fue posible insertar en base de datos")
                    logging.error('No fue posible insertar en base de datos la petición #' + type_request)
                    break

        if type_request in ['6', '7']:
            # 6. hotel_international, 7. hotel_international
            while True:
                execution = self.execute_flow_hotel_domestic_international(type_request, occupancy)
                if execution:
                    break
                # Si sólo pasó página de pasajeros debe repetir el flujo hasta que sean minimo 4 intentos
                elif execution is False and self.context.repetitions == 4:
                    print("No fue posible insertar en base de datos")
                    logging.error('No fue posible insertar en base de datos la petición #' + type_request)
                    break

        elif type_request in ['8']:
            # 8. air_auto_international 1r2a1c
            while True:
                execution = self.execute_flow_flight_auto(type_request, occupancy)
                if execution:
                    break
                # Si sólo pasó página de pasajeros debe repetir el flujo hasta que sean minimo 4 intentos
                elif execution is False and self.context.repetitions == 4:
                    print("No fue posible insertar en base de datos")
                    logging.error('No fue posible insertar en base de datos la petición #' + type_request)
                    break

        elif type_request in ['9']:
            # 9. international_package 1r1a_2r2a1c
            while True:
                execution = self.execute_flow_air_auto_international(type_request, occupancy)
                if execution:
                    break
                # Si sólo pasó página de pasajeros debe repetir el flujo hasta que sean minimo 4 intentos
                elif execution is False and self.context.repetitions == 4:
                    print("No fue posible insertar en base de datos")
                    logging.error('No fue posible insertar en base de datos la petición #' + type_request)
                    break

        elif type_request in ['10']:
            # 10. autos_international 1r1a
            while True:
                execution = self.execute_flow_auto(type_request, occupancy)
                if execution:
                    break
                # Si sólo pasó página de pasajeros debe repetir el flujo hasta que sean minimo 4 intentos
                elif execution is False and self.context.repetitions == 4:
                    print("No fue posible insertar en base de datos")
                    logging.error('No fue posible insertar en base de datos la petición #' + type_request)
                    break

        elif type_request in ['11']:
            # 11. extras_domestic 1r1a
            while True:
                execution = self.execute_flow_extras(type_request, occupancy)
                if execution:
                    break
                # Si sólo pasó página de pasajeros debe repetir el flujo hasta que sean minimo 4 intentos
                elif execution is False and self.context.repetitions == 4:
                    print("No fue posible insertar en base de datos")
                    logging.error('No fue posible insertar en base de datos la petición #' + type_request)
                    break

    def search_results(self, type_request):
        """Busca los resultados dependiendo de el tipo de solicitud.

        :param type_request:La solicitud configurada en el MainExecution.
        :return:
        """
        global url
        checkin = datetime.datetime.now() + datetime.timedelta(days=int(30))
        initial_date = str(checkin.date().year) + '-' + str(checkin.date().month) + '-' + str(
            checkin.date().day)
        final_date = datetime.datetime.now() + datetime.timedelta(days=int(33))
        final_date = str(final_date.date().year) + '-' + str(final_date.date().month) + '-' + str(final_date.date().day)

        # 1- domestic_ow BOG - MDE 1r1a1i
        if type_request == '1':
            self.context.get(
                "https://testing.netactica.net/es-CO/Air/OW/BOG/MDE/{}/1/0/1/NA/NA/NA/NA/NA/false/false/autom#air".format(
                    initial_date))
            url = "https://testing.netactica.net/es-CO/Air/OW/BOG/MDE/{}/1/0/1/NA/NA/NA/NA/NA/false/false/autom#air".format(
                initial_date)
        # 2- domestic_rt BOG - MDE 1r1a1c
        elif type_request == '2':
            self.context.get(
                "https://testing.netactica.net/es-CO/Air/RT/BOG/MDE/{}/{}/1/1/0/NA/NA/NA/NA/NA/false/false/autom#air".format(
                    initial_date, final_date))
            url = "https://testing.netactica.net/es-CO/Air/RT/BOG/MDE/{}/{}/1/1/0/NA/NA/NA/NA/NA/false/false/autom#air".format(
                initial_date, final_date)
        # 3- international_rt BOG - MIA 1r1a1i
        elif type_request == '3':
            self.context.get(
                "https://testing.netactica.net/es-CO/Air/OW/BOG/MIA/{}/1/0/1/NA/NA/NA/NA/NA/false/false/autom#air".format(
                    initial_date))
            url = "https://testing.netactica.net/es-CO/Air/OW/BOG/MIA/{}/1/0/1/NA/NA/NA/NA/NA/false/false/autom#air".format(
                initial_date)
        # 4- international_ow BOG - MIA 1r1a1c
        elif type_request == '4':
            self.context.get(
                "https://testing.netactica.net/es-CO/Air/RT/BOG/MIA/{}/{}/1/1/0/NA/NA/NA/NA/NA/false/false/autom#air".format(
                    initial_date, final_date))
            url = "https://testing.netactica.net/es-CO/Air/RT/BOG/MIA/{}/{}/1/1/0/NA/NA/NA/NA/NA/false/false/autom#air".format(
                initial_date, final_date)
        # 5 - package BOG-MED 1r1a
        elif type_request == '5':
            self.context.get(
                "https://testing.netactica.net/es-CO/Package/BOG/MDE/{}/{}/1/0/0/{}/{}/1$0/false/false/NA/NA/NA/autom#air".format(
                    initial_date, final_date, initial_date, final_date))
            url = "https://testing.netactica.net/es-CO/Package/BOG/MDE/{}/{}/1/0/0/{}/{}/1$0/false/false/NA/NA/NA/autom#air".format(
                initial_date, final_date, initial_date, final_date)
        # 6 - hotel_domestic
        elif type_request == '6':
            self.context.get(
                "https://testing.netactica.net/es-CO/Hotel/BOG/{}/{}/1$0/NA/autom#hotel".format(
                    initial_date, final_date))
            url = "https://testing.netactica.net/es-CO/Hotel/BOG/{}/{}/1$0/NA/autom#hotel".format(
                initial_date, final_date)
        # 7 - hotel_international
        elif type_request == '7':
            self.context.get(
                "https://testing.netactica.net/es-CO/Hotel/MIA/{}/{}/1!2-6/NA/autom#hotel".format(
                    initial_date, final_date))
            url = "https://testing.netactica.net/es-CO/Hotel/MIA/{}/{}/1!2-6/NA/autom#hotel".format(
                initial_date, final_date)
        # 8 - air_auto_international
        elif type_request == '8':
            self.context.get(
                "https://testing.netactica.net/es-CO/AirCar//BOG/MIA/{}/{}/2/1/0/NA/NA/NA/NA/NA/false/false/autom#air".format(
                    initial_date, final_date))
            url = "https://testing.netactica.net/es-CO/AirCar//BOG/MIA/{}/{}/2/1/0/NA/NA/NA/NA/NA/false/false/autom#air".format(
                initial_date, final_date)
        # 9 - international_package 1r1a
        elif type_request == '9':
            self.context.get(
                "https://testing.netactica.net/es-CO/Package/BOG/MIA/{}/{}/3/1/0/{}/{}/1$0!2-5$0/false/false/NA/NA/NA/autom#air".format(
                    initial_date, final_date, initial_date, final_date))
            url = "https://testing.netactica.net/es-CO/Package/BOG/MIA/{}/{}/3/1/0/{}/{}/1$0!2-5$0/false/false/NA/NA/NA/autom#air".format(
                initial_date, final_date, initial_date, final_date)
        # 10 autos_international
        elif type_request == '10':
            self.context.get(
                "https://testing.netactica.net/es-CO/Car/MIA/{}/1000/MIA/{}/1000/NA/NA/NA/autom#car".format(
                    initial_date, final_date))
            url = "https://testing.netactica.net/es-CO/Car/MIA/{}/1000/MIA/{}/1000/NA/NA/NA/autom#car".format(
                initial_date, final_date)
        # 11 extras nacional
        elif type_request == '11':
            self.context.get(
                "https://testing.netactica.net/es-CO/Extras/BOG/NA/{}/{}/autom#extra".format(
                    initial_date, final_date))
            url = "https://testing.netactica.net/es-CO/Extras/BOG/NA/{}/{}/autom#extra".format(
                initial_date, final_date)
        print(url)

    def insert_in_database(self, type_request, occupancy):
        try:
            passenger_page = PassengerPage(self.context)
            database_queries = DatabaseQueries()
            passenger_page.send_form()
            pay_page = PayPage(self.context)
            itinerary = pay_page.get_itinerary_number()
            database_queries.InsertReservation(itinerary, type_request, occupancy)
            return True
        except:
            self.context.repetitions = self.context.repetitions + 1
            return False

    def skip_additional_services(self):
        self.skip_autos()
        self.skip_extras()

    def skip_autos(self):
        result_page = ResultPage(self.context)
        result_page.wait_autos()
        search_json = self.context.execute_script('return $searchData')
        cars = search_json['CarResults']
        if len(cars) != 0:
            # Cambiar el scritp
            self.context.execute_script('ContinueWithoutRentingCar()')
            print('Omite página de autos')

    def skip_extras(self):
        search_json = self.context.execute_script('return $searchData')

        extras = search_json['ExtraResults']
        if len(extras) != 0:
            self.context.execute_script('PostReservation(true)')
            print('Omite página de extras')
        else:
            print('No tiene página de extras')

    def execute_flows_flight(self, type_request, occupancy):
        passenger_page = PassengerPage(self.context)
        result_page = ResultPage(self.context)
        status = False

        while self.context.repetitions <= 4:
            print("Repite" + str(self.context.repetitions))
            self.search_results(type_request)
            result_status = result_page.select_flight(self.context.repetitions)
            if result_status:
                self.skip_additional_services()
                status = passenger_page.fill_passenger_information(occupancy)

            # Si status es verdadero, osea, que el mensaje de precios es correcto
            if status and result_status:
                status_insert = self.insert_in_database(type_request, occupancy)
                if status_insert:
                    return True
                elif status_insert is False:
                    return False
            else:
                if self.context.repetitions == 4:
                    print("No fue posible registrar pasajeros")
                    return False

    def execute_flow_air_auto_international(self, type_request, occupancy):
        result_page = ResultPage(self.context)
        passenger_page = PassengerPage(self.context)
        status = False
        hotel_status = False

        while self.context.repetitions <= 4:
            print("Repite" + str(self.context.repetitions))
            self.search_results(type_request)
            flight_status = result_page.select_flight(self.context.repetitions)
            if flight_status:
                hotel_status = result_page.select_hotel(self.context.repetitions)
                if hotel_status:
                    self.skip_additional_services()
                    status = passenger_page.fill_passenger_information(occupancy)

            # Si status es verdadero, osea, que el mensaje de precios es correcto
            if status and flight_status and hotel_status:
                status_insert = self.insert_in_database(type_request, occupancy)
                if status_insert:
                    return True
                elif status_insert is False:
                    return False
            else:
                if self.context.repetitions == 4:
                    print("No fue posible registrar pasajeros")
                    return False

    def execute_flow_auto(self, type_request, occupancy):
        result_page = ResultPage(self.context)
        passenger_page = PassengerPage(self.context)
        status_copy_driver = False
        status = False

        while self.context.repetitions <= 4:
            print("Repite" + str(self.context.repetitions))
            self.search_results(type_request)
            auto_status = result_page.select_auto(self.context.repetitions)
            if auto_status:
                result_page.rent_car()
                self.skip_extras()
                status = passenger_page.fill_driver_information()
                status_copy_driver = passenger_page.fill_driver()

            if status and status_copy_driver and auto_status:
                status_insert = self.insert_in_database(type_request, occupancy)
                if status_insert:
                    return True
                elif status_insert is False:
                    return False
            else:
                if self.context.repetitions == 4:
                    print("No fue posible registrar pasajeros")
                    return False

    def execute_flow_extras(self, type_request, occupancy):
        passenger_page = PassengerPage(self.context)
        result_page = ResultPage(self.context)
        extra_page = ExtraPage(self.context)
        status_copy_driver = False

        while self.context.repetitions <= 4:
            print("Repite" + str(self.context.repetitions))
            self.search_results(type_request)
            result_page.select_extra()
            extra_page.select_occupancy('1')
            result_page.buy_extra_now()
            result_page.buy_extra()
            status_extras = passenger_page.fill_extra_information()
            if status_extras:
                status_copy_driver = passenger_page.fill_driver()

            if status_extras and status_copy_driver:
                status_insert = self.insert_in_database(type_request, occupancy)
                if status_insert:
                    return True
                elif status_insert is False:
                    return False
            else:
                if self.context.repetitions == 4:
                    print("No fue posible registrar pasajeros")
                    return False

    def execute_flow_flight_auto(self, type_request, occupancy):
        result_page = ResultPage(self.context)
        passenger_page = PassengerPage(self.context)
        car_details_page = CarsDetailsPage(self.context)
        status_driver = False
        status = False

        while self.context.repetitions <= 4:
            print("Repite" + str(self.context.repetitions))
            self.search_results(type_request)

            flight_status = result_page.select_flight(self.context.repetitions)
            if flight_status:
                result_page.select_auto(self.context.repetitions)
                car_details_page.select_option_car()
                self.skip_extras()
                status = passenger_page.fill_passenger_information(occupancy)
                status_driver = passenger_page.fill_driver()

            if status and status_driver and flight_status:
                status_insert = self.insert_in_database(type_request, occupancy)
                if status_insert:
                    return True
                elif status_insert is False:
                    return False
            else:
                if self.context.repetitions == 4:
                    print("No fue posible registrar pasajeros")
                    return False

    def execute_flow_hotel_domestic_international(self, type_request, occupancy):
        result_page = ResultPage(self.context)
        passenger_page = PassengerPage(self.context)
        status_passenger = False

        while self.context.repetitions <= 4:
            print("Repite" + str(self.context.repetitions))
            self.search_results(type_request)

            hotel_status = result_page.select_hotel(self.context.repetitions)

            if hotel_status:
                self.skip_additional_services()
                status_passenger = passenger_page.fill_passenger_information(occupancy)

            if status_passenger and hotel_status:
                status_insert = self.insert_in_database(type_request, occupancy)
                if status_insert:
                    return True
                elif status_insert is False:
                    return False
            else:
                if self.context.repetitions == 4:
                    print("No fue posible registrar pasajeros")
                    return False

    def execute_flow_domestic_package(self, type_request, occupancy):
        result_page = ResultPage(self.context)
        passenger_page = PassengerPage(self.context)
        status = False
        hotel_status = False

        while self.context.repetitions <= 4:
            print("Repite" + str(self.context.repetitions))

            self.search_results(type_request)
            fligth_status = result_page.select_flight(self.context.repetitions)

            if fligth_status:
                hotel_status = result_page.select_hotel(self.context.repetitions)
                if hotel_status:
                    self.skip_additional_services()
                    status = passenger_page.fill_passenger_information(occupancy)

            # Si status es verdadero, osea, que el mensaje de precios es correcto
            if status and fligth_status and hotel_status:
                status_insert = self.insert_in_database(type_request, occupancy)
                if status_insert:
                    return True
                elif status_insert is False:
                    return False
            else:
                if self.context.repetitions == 4:
                    print("No fue posible registrar pasajeros")
                    return False
