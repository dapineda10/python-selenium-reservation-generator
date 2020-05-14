import logging
import time
from datetime import date
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Project.Extensions.WebDriverExtensions import WebDriverExtensions
from Project.Mockaroo.MockarooRequest import MockarooRequest


class PassengerPage:
    PASSENGER_TITLE = "Travelers_{index}__Title"
    PASSENGER_NAME = "Travelers_{index}__FirstName"
    PASSENGER_LAST_NAME = "Travelers_{index}__LastName"
    PASSENGER_DOCUMENT_TYPE = "Travelers_{index}__DocumentType"
    PASSENGER_DOCUMENT = "Travelers_{index}__DucumentNumber"
    PASSENGER_DOB_D = "Travelers[{index}].DOB_d"
    PASSENGER_DOB_M = "Travelers[{index}].DOB_m"
    PASSENGER_DOB_Y = "Travelers[{index}].DOB_y"
    PASSENGER_EMAIL = (By.ID, "ContactEmail")
    PASSENGER_PHONE = (By.ID, "ContactPhone")
    PASSENGER_CHECKBOX = (By.ID, "chkTermsAndConditions")
    PASSENGER_SUBMIT = "submitButtonId"
    PASSENGER_AVAILABILITY_MESSAGE = (By.ID, "message")
    PASSENGER_TOTAL_PRICE_TEXT = (By.XPATH, '//*[@id="packSummary"]/div[1]/div[5]/div[2]/span/span[2]')
    PASSENGER_TOTALIZER_TEXT = (By.CLASS_NAME, 'nts-totalizer')
    PASSENGER_CURRENCY_PRICE_TEXT = (By.CLASS_NAME, 'currencyText')
    PASSENGER_CURRENCY_CODE_TEXT = (By.CLASS_NAME, 'currencyCode')
    DRIVER_TITLE = (By.ID, "Driver_Title")
    DRIVER_NAME = (By.ID, "Driver_FirstName")
    DRIVER_LAST_NAME = (By.ID, "Driver_LastName")
    DRIVER_DOCUMENT_TYPE = (By.ID, "Driver_DocumentType")
    DRIVER_DOCUMENT = (By.ID, "Driver_DucumentNumber")
    DRIVER_DOB_D = (By.ID, "Driver.DOB_d")
    DRIVER_DOB_M = (By.ID, "Driver.DOB_m")
    DRIVER_DOB_Y = (By.ID, "Driver.DOB_y")
    EXTRA_TITLE = (By.ID, "ExtraReservationItems_0__Travelers_0__Title")
    EXTRA_NAME = (By.ID, "ExtraReservationItems_0__Travelers_0__FirstName")
    EXTRA_LAST_NAME = (By.ID, "ExtraReservationItems_0__Travelers_0__LastName")
    EXTRA_DOCUMENT_TYPE = (By.ID, "ExtraReservationItems_0__Travelers_0__DocumentType")
    EXTRA_DOCUMENT = (By.ID, "ExtraReservationItems_0__Travelers_0__DucumentNumber")
    EXTRA_DOB_D = (By.ID, "ExtraReservationItems[0].Travelers[0].DOB_d")
    EXTRA_DOB_M = (By.ID, "ExtraReservationItems[0].Travelers[0].DOB_m")
    EXTRA_DOB_Y = (By.ID, "ExtraReservationItems[0].Travelers[0].DOB_y")

    def __init__(self, context):
        self.context = context
        self.mockaroo = MockarooRequest()

    def fill_driver_information(self):
        data = self.mockaroo.GetNetNFFPassengersData()

        if self.IsAvailabilityMessageInPage() is False:
            self.FillFormPerDriver()
            self.FillEmail(data['Email'])
            self.FillPhone(data['Phone'])
            self.ClickCheckBox()
            return True
        else:
            self.context.repetitions = self.context.repetitions + 1
            return False

    def fill_extra_information(self):
        data = self.mockaroo.GetNetNFFPassengersData()
        try:
            if self.IsAvailabilityMessageInPage() is False:
                self.FillFormExtra()
                self.FillEmail(data['Email'])
                self.FillPhone(data['Phone'])
                self.ClickCheckBox()
                return True
            else:
                self.context.repetitions = self.context.repetitions + 1
                return False
        except:
            self.context.repetitions = self.context.repetitions + 1
            logging.error("No fue posible registrar información extra, el código de flujo es:" + self.context.code_flow)
            return False

    def fill_passenger_information(self, occupancy):
        """Registra los pasajeros en el formulario dependiendo del occupancy.
        :return:
        """
        try:
            data = self.mockaroo.GetNetNFFPassengersData()

            if occupancy == '1r1a' and self.IsAvailabilityMessageInPage() is False:
                self.FillPassenger1r1a()
                self.FillEmail(data['Email'])
                self.FillPhone(data['Phone'])

                self.ClickCheckBox()
                return True
            elif occupancy == '1r1a1i' and self.IsAvailabilityMessageInPage() is False:
                self.FillPassenger1r1a1i()
                self.FillEmail(data['Email'])
                self.FillPhone(data['Phone'])
                self.ClickCheckBox()
                return True
            elif occupancy == '1r1a1c' and self.IsAvailabilityMessageInPage() is False:
                self.FillPassenger1r1a1c()
                self.FillEmail(data['Email'])
                self.FillPhone(data['Phone'])
                self.ClickCheckBox()
                return True
            elif occupancy == '1r2a2c' and self.IsAvailabilityMessageInPage() is False:
                self.FillPassenger1r2a2c()
                self.FillEmail(data['Email'])
                self.FillPhone(data['Phone'])
                self.ClickCheckBox()
                return True
            elif occupancy == '1r2a1c' and self.IsAvailabilityMessageInPage() is False:
                self.FillPassenger1r2a1c()
                self.FillEmail(data['Email'])
                self.FillPhone(data['Phone'])
                self.ClickCheckBox()
                return True
            elif occupancy == '1r2a_2r2a' and self.IsAvailabilityMessageInPage() is False:
                self.FillPassenger1r2a2r2a()
                self.FillEmail(data['Email'])
                self.FillPhone(data['Phone'])
                self.ClickCheckBox()
                return True
            elif occupancy == '1r3a_2r4a' and self.IsAvailabilityMessageInPage() is False:
                self.FillPassenger1r3a2r4a()
                self.FillEmail(data['Email'])
                self.FillPhone(data['Phone'])
                self.ClickCheckBox()
                return True
            elif occupancy == '1r2a1i_2r2a1c' and self.IsAvailabilityMessageInPage() is False:
                self.FillPassenger1r2a1i2r2a1c()
                self.FillEmail(data['Email'])
                self.FillPhone(data['Phone'])
                self.ClickCheckBox()
                return True
            elif occupancy == '1r1a_2r2a1c_1' and self.IsAvailabilityMessageInPage() is False:
                self.FillPassenger1r1a2r2a1c1()
                self.FillEmail(data['Email'])
                self.FillPhone(data['Phone'])
                self.ClickCheckBox()
                return True
            elif occupancy == '1r1a_2r2a1c_2' and self.IsAvailabilityMessageInPage() is False:
                self.FillPassenger1r1a2r2a1c2()
                self.FillEmail(data['Email'])
                self.FillPhone(data['Phone'])
                self.ClickCheckBox()
                return True
            else:
                self.context.repetitions = self.context.repetitions + 1
                return False
        except:
            self.context.repetitions = self.context.repetitions + 1
            logging.error("No fue posible registrar pasajeros, el código de flujo es:" + self.context.code_flow)
            return False

    def FillPassenger1r1a(self):
        self.FillFormPerPassenger('primary_adult', 0)

    def FillPassenger1r2a2c(self):
        self.FillFormPerPassenger('primary_adult', 0)
        self.FillFormPerPassenger('secondary_adult', 1)
        self.FillFormPerPassenger('child', 2)
        self.FillFormPerPassenger('child', 3)

    def FillPassenger1r1a1i(self):
        self.FillFormPerPassenger('primary_adult', 0)
        self.FillFormPerPassenger('infant-flight', 1)

    def FillPassenger1r1a1c(self):
        self.FillFormPerPassenger('primary_adult', 0)
        self.FillFormPerPassenger('child-flight', 1)

    def FillPassenger1r2a1c(self):
        self.FillFormPerPassenger('primary_adult', 0)
        self.FillFormPerPassenger('secondary_adult', 1)
        self.FillFormPerPassenger('child-flight', 2)

    def FillPassenger1r2a2r2a(self):
        self.FillFormPerPassenger('primary_adult', 0)
        self.FillFormPerPassenger('secondary_adult', 1)
        self.FillFormPerPassenger('primary_adult', 2)
        self.FillFormPerPassenger('secondary_adult', 3)

    def FillPassenger1r3a2r4a(self):
        self.FillFormPerPassenger('primary_adult', 0)
        self.FillFormPerPassenger('secondary_adult', 1)
        self.FillFormPerPassenger('secondary_adult', 2)
        self.FillFormPerPassenger('primary_adult', 3)
        self.FillFormPerPassenger('secondary_adult', 4)
        self.FillFormPerPassenger('secondary_adult', 5)
        self.FillFormPerPassenger('secondary_adult', 6)

    def FillPassenger1r2a1i2r2a1c(self):
        self.FillFormPerPassenger('primary_adult', 0)
        self.FillFormPerPassenger('secondary_adult', 1)
        self.FillFormPerPassenger('child', 2)
        self.FillFormPerPassenger('primary_adult', 3)
        self.FillFormPerPassenger('secondary_adult', 4)
        self.FillFormPerPassenger('child', 5)

    def FillPassenger1r1a2r2a1c1(self):
        self.FillFormPerPassenger('primary_adult', 0)
        self.FillFormPerPassenger('primary_adult', 1)
        self.FillFormPerPassenger('secondary_adult_hotel', 2)
        self.FillFormPerPassenger('child', 3)

    def FillPassenger1r1a2r2a1c2(self):
        self.FillFormPerPassenger('primary_adult', 0)
        self.FillFormPerPassenger('primary_adult', 1)
        self.FillFormPerPassenger('secondary_adult', 2)
        self.FillFormPerPassenger('child-flight', 3)

    def FillFormExtra(self):
        data = self.mockaroo.GetNetNFFPassengersData()
        self.FillTitleExtra(data['Title'])
        self.FillNameExtra(data['FirstName'])
        self.FillLastNameExtra(data['LastName'])
        self.FillDocumentTypeExtra(data['BillingDocumentTypeNamePlaceToPay'])
        self.FillIDocumentNumberExtra(self.mockaroo.GetDocumentPassenger())
        mockaroo_date = data['ChildAge1'].split(" ")[0]
        date_object = date.fromisoformat(mockaroo_date)
        self.FillBirthDayExtra(date_object.day)
        self.FillBirthDayMonthExtra(date_object.month)
        self.FillBirthDayYearExtra(date_object.year)

    def FillFormPerDriver(self):
        """Registra pasajeros según el tipo.
         """
        data = self.mockaroo.GetNetNFFPassengersData()
        self.FillTitleDriver(data['Title'])
        self.FillNameDriver(data['FirstName'])
        self.FillLastNameDriver(data['LastName'])
        self.FillDocumentTypeDriver(data['BillingDocumentTypeNamePlaceToPay'])
        self.FillIDocumentNumberDriver(self.mockaroo.GetDocumentPassenger())
        mockaroo_date = data['ChildAge1'].split(" ")[0]
        date_object = date.fromisoformat(mockaroo_date)
        self.FillBirthDayDriver(date_object.day)
        self.FillBirthDayMonthDriver(date_object.month)
        self.FillBirthDayYearDriver(date_object.year)

    def FillFormPerPassenger(self, type_passenger, passenger_number):
        """Registra pasajeros según el tipo.
            Los tipos de pasajeros(type_passenger) son: primary_adult, secondary_adult y child passenger_number
            número de pasajero(passenger_number) = Debe iniciar con el indice 0

         """
        print('Ingresa a llenar pasajeros')
        data = self.mockaroo.GetNetNFFPassengersData()
        self.FillTitle(data['Title'], passenger_number)
        self.FillName(data['FirstName'], passenger_number)
        self.FillLastName(data['LastName'], passenger_number)

        # Si es un primary_adult debe llenar algunos datos adicionales
        if type_passenger == 'primary_adult':
            print('Va a llenar adulto')
            self.FillDocumentType(data['BillingDocumentTypeNamePlaceToPay'], passenger_number)
            self.FillIDocumentNumber(self.mockaroo.GetDocumentPassenger(), passenger_number)
            mockaroo_date = data['ChildAge1'].split(" ")[0]
            date_object = date.fromisoformat(mockaroo_date)
            self.FillBirthDay(date_object.day, passenger_number)
            self.FillBirthDayMonth(date_object.month, passenger_number)
            self.FillBirthDayYear(date_object.year, passenger_number)

        # Si es un primary_adult debe llenar algunos datos adicionales
        if type_passenger == 'secondary_adult':
            self.FillDocumentType(data['BillingDocumentTypeNamePlaceToPay'], passenger_number)
            self.FillIDocumentNumber(self.mockaroo.GetDocumentPassenger(), passenger_number)
            mockaroo_date = data['ChildAge1'].split(" ")[0]
            date_object = date.fromisoformat(mockaroo_date)
            self.FillBirthDay(date_object.day, passenger_number)
            self.FillBirthDayMonth(date_object.month, passenger_number)
            self.FillBirthDayYear(date_object.year, passenger_number)

        # Si es un child debe registrar las edades correctas
        if type_passenger == 'child':
            mockaroo_date = data['ChildAge1'].split(" ")[0]
            date_object = date.fromisoformat(mockaroo_date)
            self.FillBirthDay(date_object.day, passenger_number)
            self.FillBirthDayMonth(date_object.month, passenger_number)
            self.FillBirthDayYear(date_object.year, passenger_number)

        if type_passenger == 'infant':
            mockaroo_date = data['ChildAge1'].split(" ")[0]
            date_object = date.fromisoformat(mockaroo_date)
            self.FillBirthDay(date_object.day, passenger_number)
            self.FillBirthDayMonth(date_object.month, passenger_number)
            self.FillBirthDayYear(date_object.year, passenger_number)

        # Si es un child debe registrar las edades correctas
        if type_passenger == 'child-flight':
            mockaroo_date = data['ChildAge1'].split(" ")[0]
            date_object = date.fromisoformat(mockaroo_date)
            self.FillDocumentType(data['BillingDocumentTypeNamePlaceToPay'], passenger_number)
            self.FillIDocumentNumber(self.mockaroo.GetDocumentPassenger(), passenger_number)
            self.FillBirthDay(date_object.day, passenger_number)
            self.FillBirthDayMonth(date_object.month, passenger_number)
            self.FillBirthDayYear(date_object.year, passenger_number)

        if type_passenger == 'infant-flight':
            mockaroo_date = data['ChildAge1'].split(" ")[0]
            date_object = date.fromisoformat(mockaroo_date)
            self.FillDocumentType(data['BillingDocumentTypeNamePlaceToPay'], passenger_number)
            self.FillIDocumentNumber(self.mockaroo.GetDocumentPassenger(), passenger_number)
            self.FillBirthDay(date_object.day, passenger_number)
            self.FillBirthDayMonth(date_object.month, passenger_number)
            self.FillBirthDayYear(date_object.year, passenger_number)

    def MakeOccupancy(self, rooms, adults_room_one, children_room_one, adults_room_two, children_room_two):
        """retorna un occupancy dependiendo de los adultos y niños que le lleguen.

        :param rooms: la cantidad de habitaciones
        :param adults_room_one: Cantidad de adultos en la habitación 1
        :param children_room_one: Cantidad de adultos en la habitación 1
        :param adults_room_two: Cantidad de adultos en la habitación 2
        :param children_room_two: Cantidad de adultos en la habitación 2
        :return: occupancy
        """
        if rooms == 1:
            if adults_room_one == 1 and children_room_one == 0:
                return '1r1a'
            elif adults_room_one == 2 and children_room_one == 2:
                return '1r2a2c'
            elif adults_room_one == 2 and children_room_one == 1:
                return '1r2a1c'
        if rooms == 2:
            if adults_room_one == 2 and children_room_one == 0 and adults_room_two == 2 and children_room_two == 0:
                return '1r2a_2r2a'
            elif adults_room_one == 3 and children_room_one == 0 and adults_room_two == 4 and children_room_two == 0:
                return '1r3a_2r4a'
            elif adults_room_one == 1 and children_room_one == 0 and adults_room_two == 2 and children_room_two == 1:
                return '1r1a_2r2a1c'
            elif adults_room_one == 2 and children_room_one == 1 and adults_room_two == 2 and children_room_two == 1:
                return '1r2a1i_2r2a1c'

    def IsAvailabilityMessageInPage(self):
        """Valida que haya desaparecido el mensaje de comprobación de precios en página de pasajeros
        :return:
        """
        count = 0
        while True:
            time.sleep(2)
            element = WebDriverWait(self.context, 15).until(
                EC.presence_of_element_located(self.PASSENGER_AVAILABILITY_MESSAGE))
            count = count + 1
            if not element.is_displayed():
                return False
            elif count == 5:
                return True

    def FillTitle(self, title, index):
        by = (By.ID, self.PASSENGER_TITLE.replace("{index}", str(index)))
        WebDriverWait(self.context, 20).until(
            EC.visibility_of_element_located(by)).send_keys(title)

    def FillName(self, name, index):
        by = (By.ID, self.PASSENGER_NAME.replace("{index}", str(index)))
        WebDriverWait(self.context, 20).until(
            EC.visibility_of_element_located(by)).send_keys(name)

    def FillLastName(self, last_name, index):
        by = (By.ID, self.PASSENGER_LAST_NAME.replace("{index}", str(index)))
        WebDriverWait(self.context, 20).until(
            EC.visibility_of_element_located(by)).send_keys(last_name)

    def FillIDocumentNumber(self, document, index):
        try:
            by = (By.ID, self.PASSENGER_DOCUMENT.replace("{index}", str(index)))
            WebDriverWait(self.context, 20).until(
                EC.visibility_of_element_located(by)).send_keys(document)
        except:
            pass

    def FillDocumentType(self, type_document, index):
        by = (By.ID, self.PASSENGER_DOCUMENT_TYPE.replace("{index}", str(index)))
        WebDriverWait(self.context, 20).until(
            EC.visibility_of_element_located(by)).send_keys(type_document)

    def FillBirthDay(self, day, index):
        by = (By.ID, self.PASSENGER_DOB_D.replace("{index}", str(index)))
        WebDriverWait(self.context, 20).until(
            EC.visibility_of_element_located(by)).send_keys(day)

    def FillBirthDayMonth(self, month, index):
        by = (By.ID, self.PASSENGER_DOB_M.replace("{index}", str(index)))
        WebDriverWait(self.context, 20).until(
            EC.visibility_of_element_located(by)).send_keys(month)

    def FillBirthDayYear(self, year, index):
        by = (By.ID, self.PASSENGER_DOB_Y.replace("{index}", str(index)))
        WebDriverWait(self.context, 20).until(
            EC.visibility_of_element_located(by)).send_keys(year)

    def FillTitleDriver(self, title):
        WebDriverWait(self.context, 20).until(
            EC.visibility_of_element_located(self.DRIVER_TITLE)).send_keys(title)

    def FillNameDriver(self, name):
        WebDriverWait(self.context, 20).until(
            EC.visibility_of_element_located(self.DRIVER_NAME)).send_keys(name)

    def FillLastNameDriver(self, last_name):
        WebDriverWait(self.context, 20).until(
            EC.visibility_of_element_located(self.DRIVER_LAST_NAME)).send_keys(last_name)

    def FillIDocumentNumberDriver(self, document):
        try:
            WebDriverWait(self.context, 20).until(
                EC.visibility_of_element_located(self.DRIVER_DOCUMENT)).send_keys(document)
        except:
            pass

    def FillDocumentTypeDriver(self, type_document):
        WebDriverWait(self.context, 20).until(
            EC.visibility_of_element_located(self.DRIVER_DOCUMENT_TYPE)).send_keys(type_document)

    def FillBirthDayDriver(self, day):
        WebDriverWait(self.context, 20).until(
            EC.visibility_of_element_located(self.DRIVER_DOB_D)).send_keys(day)

    def FillBirthDayMonthDriver(self, month):
        WebDriverWait(self.context, 20).until(
            EC.visibility_of_element_located(self.DRIVER_DOB_M)).send_keys(month)

    def FillBirthDayYearDriver(self, year):
        WebDriverWait(self.context, 20).until(
            EC.visibility_of_element_located(self.DRIVER_DOB_Y)).send_keys(year)

    def FillTitleExtra(self, title):
        try:
            element = WebDriverWait(self.context, 20).until(
                EC.visibility_of_element_located(self.EXTRA_TITLE))
            element.send_keys(title)
        except Exception as e:
            print(e)

    def FillNameExtra(self, name):
        WebDriverWait(self.context, 20).until(
            EC.visibility_of_element_located(self.EXTRA_NAME)).send_keys(name)

    def FillLastNameExtra(self, last_name):
        WebDriverWait(self.context, 20).until(
            EC.visibility_of_element_located(self.EXTRA_LAST_NAME)).send_keys(last_name)

    def FillIDocumentNumberExtra(self, document):
        try:
            WebDriverWait(self.context, 20).until(
                EC.visibility_of_element_located(self.EXTRA_DOCUMENT)).send_keys(document)
        except:
            pass

    def FillDocumentTypeExtra(self, type_document):
        WebDriverWait(self.context, 20).until(
            EC.visibility_of_element_located(self.EXTRA_DOCUMENT_TYPE)).send_keys(type_document)

    def FillBirthDayExtra(self, day):
        WebDriverWait(self.context, 20).until(
            EC.visibility_of_element_located(self.EXTRA_DOB_D)).send_keys(day)

    def FillBirthDayMonthExtra(self, month):
        WebDriverWait(self.context, 20).until(
            EC.visibility_of_element_located(self.EXTRA_DOB_M)).send_keys(month)

    def FillBirthDayYearExtra(self, year):
        WebDriverWait(self.context, 20).until(
            EC.visibility_of_element_located(self.EXTRA_DOB_Y)).send_keys(year)

    def FillEmail(self, email):
        WebDriverWait(self.context, 20).until(
            EC.visibility_of_element_located(self.PASSENGER_EMAIL)).send_keys(email)

    def FillPhone(self, phone):
        WebDriverWait(self.context, 20).until(
            EC.visibility_of_element_located(self.PASSENGER_PHONE)).send_keys(phone)

    def ClickCheckBox(self):
        WebDriverWait(self.context, 20).until(
            EC.visibility_of_element_located(self.PASSENGER_CHECKBOX)).click()

    def SendForm(self):
        self.context.find_element_by_id(self.PASSENGER_SUBMIT).click()

    def GetTotalPrice(self):
        price = self.ReplaceCharactersPrice(WebDriverWait(self.context, 40).until(
            EC.visibility_of_all_elements_located(self.PASSENGER_TOTALIZER_TEXT))[0].text)
        return price

    def GetCurrency(self):
        currency = WebDriverWait(self.context, 20).until(
            EC.visibility_of_element_located(self.PASSENGER_CURRENCY_CODE_TEXT)).text.split(' ')[0]
        self.MoveToElement(WebDriverWait(self.context, 20).until(
            EC.visibility_of_element_located(self.PASSENGER_CURRENCY_CODE_TEXT)))
        return currency

    def ReplaceCharactersPrice(self, price):
        return price.replace("$", "").replace(" ", "").replace("COP", "").replace("USD", "")

    def MoveToElement(self, target):
        actions = ActionChains(self.context)
        actions.move_to_element(target)
        actions.perform()

    def send_form(self):
        self.context.find_element_by_id(self.PASSENGER_SUBMIT).click()

    def fill_driver(self):
        try:
            extensions = WebDriverExtensions()
            extensions.ExecuteJs(self.context, "copyFirstPassengerToDriver()".format())
            return True
        except:
            self.context.repetitions = self.context.repetitions + 1
            logging.error("No fue posible copiar información del conductor, el código de flujo es:" + self.context.code_flow)
            return False
