from selenium.webdriver.support.ui import Select


class ExtraPage:
    EXTRAPAGE_SELECT_ADULTS = "ddl_Prod_0"

    def __init__(self, context):
        self.context = context

    def select_occupancy(self, adults):
        select = Select(self.context.find_element_by_id(self.EXTRAPAGE_SELECT_ADULTS))
        select.select_by_value(adults)
