from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Extensions.WebDriverExtensions import WebDriverExtensions


class CarsDetailsPage:
    RESULTPAGE_BUY_NOW = (By.CLASS_NAME, "carDetailsBuyNow")

    def __init__(self, context):
        self.context = context

    def select_option_car(self):
        extensions = WebDriverExtensions()
        WebDriverWait(self.context, 50).until(
            EC.visibility_of_all_elements_located(self.RESULTPAGE_BUY_NOW))
        extensions.ExecuteJs(self.context, "VehicleController.selectCarRate()".format())