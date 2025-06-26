import data
import Selectors
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriver, WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from UrbanRoutesPage import UrbanRoutesPage

from data import message_for_driver

class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

        cls.driver = webdriver.Chrome(service=Service(), options=options)
        cls.driver.timeouts.implicit_wait(5)
        #cls.routes_page = UrbanRoutesPage(cls.driver)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_select_comfort_rate(self):
        self.test_set_route()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_request_taxi_button()
        routes_page.click_on_comfort_rate_icon()
        assert routes_page.get_comfort_rate_icon() == "Comfort"

    def test_set_phone_number(self):
        self.test_select_comfort_rate()
        routes_page = UrbanRoutesPage(self.driver)
        assert  routes_page.check_phone_field_button_enable() == True
        routes_page.click_on_phone_field_button()
        phone_number = data.phone_number
        routes_page.set_phone_field_text(phone_number)
        assert routes_page.get_phone_field_text() == phone_number

    def test_set_credit_card_text(self):
        self.test_set_phone_number()
        routes_page = UrbanRoutesPage(self.driver)
        card_number = data.card_number
        routes_page.set_card_number_text(card_number)
        assert routes_page.get_card_number_text() == card_number

    def test_message_for_driver(self):
        self.test_set_route()
        self.test_select_comfort_rate()
        self.test_set_phone_number()
        self.test_set_credit_card_text()
        routes_page = UrbanRoutesPage(self.driver)
        msj_for_driver = data.message_for_driver
        routes_page.set_message_for_driver_text(msj_for_driver)
        assert routes_page.get_message_for_driver_text() == msj_for_driver

    def test_request_blanket_and_tissues(self):
        self.test_set_route()
        self.test_select_comfort_rate()
        self.test_set_phone_number()
        self.test_set_credit_card_text()
        self.test_message_for_driver()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_slider_button()
        assert routes_page.get_blanket_selected() == True

    def test_request_2_ice_creams(self):
        self.test_set_route()
        self.test_select_comfort_rate()
        self.test_set_phone_number()
        self.test_set_credit_card_text()
        self.test_message_for_driver()
        self.test_request_blanket_and_tissues()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_plus_button()
        routes_page.click_on_plus_button()
        assert routes_page.get_ice_cream_count() == "2"

    def test_get_reservation_popup_window(self):
        self.test_set_route()
        self.test_select_comfort_rate()
        self.test_set_phone_number()
        self.test_set_credit_card_text()
        self.test_message_for_driver()
        self.test_request_blanket_and_tissues()
        self.test_request_2_ice_creams()
        routes_page = UrbanRoutesPage(self.driver)
        assert routes_page.get_car_modal_title() == "Buscar automóvil"

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

        cls.driver = webdriver.Chrome(service=Service(), options=options)