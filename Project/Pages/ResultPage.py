import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Project.Extensions.WebDriverExtensions import WebDriverExtensions
import logging


class ResultPage:
    RESULTPAGE_FLIGHT_OPTION = (By.CLASS_NAME, "flight")
    RESULTPAGE_HOTEL_OPTION = (By.CLASS_NAME, "hotelOption ")
    RESULTPAGE_CAR_OPTION = (By.CLASS_NAME, "divCarHeading ")
    RESULTPAGE_AIRLINE_FILTERS = (By.ID, "divAirFilters")
    RESULTPAGE_AVIANCA_CHECKBOX = (By.XPATH, "//input[@value='AV']")
    RESULTPAGE_CAR_CONTENT = (By.CLASS_NAME, "divCarContent")
    RESULTPAGE_HOTEL_IMAGE = (By.CLASS_NAME, "hotel-image")
    RESULTPAGE_BUY_EXTRA = (By.ID, "btnBuyNow_1")
    RESULTPAGE_NOTIFY = (By.ID, "divLoading")

    def __init__(self, context):
        self.context = context

    def select_flight(self, flight):
        try:
            extensions = WebDriverExtensions()
            WebDriverWait(self.context, 50).until(
                EC.visibility_of_all_elements_located(self.RESULTPAGE_FLIGHT_OPTION))
            extensions.ExecuteJs(self.context, "selectAir('Air_{}')".format(str(flight)))
            return True
        except:
            self.context.repetitions = self.context.repetitions + 1
            logging.error("No hay vuelos en la página de resultados, el código de flujo es:" + self.context.code_flow)
            return False

    def select_hotel(self, hotel):
        try:
            extensions = WebDriverExtensions()
            WebDriverWait(self.context, 50).until(
                EC.visibility_of_all_elements_located(self.RESULTPAGE_HOTEL_OPTION))
            extensions.ExecuteJs(self.context, "selectHotel('Hot_{}');".format(str(hotel)))
            return True
        except:
            self.context.repetitions = self.context.repetitions + 1
            logging.error("No hay hoteles en la página de resultados, el código de flujo es:" + self.context.code_flow)
            return False

    def select_auto(self, car):
        try:
            extensions = WebDriverExtensions()
            WebDriverWait(self.context, 50).until(
                EC.visibility_of_all_elements_located(self.RESULTPAGE_CAR_OPTION))
            extensions.ExecuteJs(self.context,
                                 "VehicleController.selectCarOption('Car_{}', 1, 503752, '/');".format(str(car)))
            return True
        except:
            self.context.repetitions = self.context.repetitions + 1
            logging.error("No hay autos disponibles en la página de resultados, el código de flujo es:" + self.context.code_flow)
            return False

    def select_extra(self):
        if self.IsAvailabilityMessageInPage() is False:
            WebDriverWait(self.context, 50).until(
                EC.visibility_of_all_elements_located(self.RESULTPAGE_HOTEL_IMAGE))[0].click()

    def buy_extra_now(self):
        WebDriverWait(self.context, 50).until(
            EC.visibility_of_all_elements_located(self.RESULTPAGE_BUY_EXTRA))[0].click()

    def wait_autos(self):
        try:
            WebDriverWait(self.context, 50).until(
                EC.visibility_of_all_elements_located(self.RESULTPAGE_CAR_CONTENT))
        except:
            print('No tiene página de autos')

    def wait_extras(self):
        try:
            WebDriverWait(self.context, 50).until(
                EC.visibility_of_all_elements_located(self.RESULTPAGE_CAR_CONTENT))
        except:
            print('No tiene página de extras')

    def rent_car(self):
        extensions = WebDriverExtensions()
        WebDriverWait(self.context, 50).until(
            EC.visibility_of_all_elements_located(self.RESULTPAGE_CAR_CONTENT))
        extensions.ExecuteJs(self.context, "VehicleController.selectCarRate()".format())

    def buy_extra(self):
        extensions = WebDriverExtensions()
        try:
            WebDriverWait(self.context, 50).until(
                EC.visibility_of_all_elements_located(self.RESULTPAGE_HOTEL_IMAGE))
            extensions.ExecuteJs(self.context, "PostReservation(true)".format())
        except:
            pass

    def IsAvailabilityMessageInPage(self):
        """Valida que haya desaparecido el mensaje de comprobación de precios en página de pasajeros
        :return:
        """
        while True:
            element = WebDriverWait(self.context, 15).until(
                EC.presence_of_element_located(self.RESULTPAGE_NOTIFY))
            time.sleep(2)
            if not element.is_displayed():
                return False
