from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class PayPage():
    def __init__(self, context):
        self.context = context

    PAY_ITINERARY_DOMESTIC = (By.ID,
                              "ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_ctl06_lblItineraryNumber")

    PAY_ITINERARY_INTERNATIONAL = (By.ID,
                                   "ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_ctl05_lblItineraryNumber")

    PAY_ITINERARY_ALTERNATIVE = (By.ID,
                                 "ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_lblItineraryNumber")

    PAY_ITINERARY_ALTERNATIVE_2 = (By.ID,
                                   "ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_ctl04_lblItineraryNumber")

    def get_itinerary_number(self):
        try:
            itinerary = WebDriverWait(self.context, 30).until(
                EC.visibility_of_element_located(self.PAY_ITINERARY_DOMESTIC)).text
        except:
            try:
                itinerary = WebDriverWait(self.context, 10).until(
                    EC.visibility_of_element_located(self.PAY_ITINERARY_ALTERNATIVE)).text
            except:
                try:
                    itinerary = WebDriverWait(self.context, 10).until(
                        EC.visibility_of_element_located(self.PAY_ITINERARY_ALTERNATIVE_2)).text
                except:
                    itinerary = WebDriverWait(self.context, 10).until(
                        EC.visibility_of_element_located(self.PAY_ITINERARY_INTERNATIONAL)).text

        return itinerary
