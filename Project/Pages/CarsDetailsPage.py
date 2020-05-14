from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Project.Extensions.WebDriverExtensions import WebDriverExtensions


class CarsDetailsPage:
    RESULTPAGE_BUY_NOW = (By.CLASS_NAME, "carDetailsBuyNow")

    def __init__(self, context):
        self.context = context

    def select_option_car(self):
        extensions = WebDriverExtensions()
        WebDriverWait(self.context, 30).until(
            EC.presence_of_element_located(self.RESULTPAGE_BUY_NOW))
        extensions.ExecuteJs(self.context, "VehicleController.selectCarRate()".format())
        print("eligió el auto")