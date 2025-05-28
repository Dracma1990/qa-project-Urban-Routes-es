import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriver, WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from data import message_for_driver

driver = webdriver.Chrome()


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code
    return None

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    request_taxi_button = (By.CSS_SELECTOR, ".button.round")
    comfort_rate_icon = (By.XPATH, "//div[@class='tcard-title' and text ()='Comfort']")
    phone_field_button = (By.CSS_SELECTOR, "np-button")
    phone_field = (By.ID, 'phone')
    next_button = (By.CSS_SELECTOR, "button.button.full")
    confirm_button = (By.XPATH, "//div[@class='button.button.full' and text ()='Confirmar']")
    payment_method_button = (By.CSS_SELECTOR, ".pp-button.filled")
    add_card_button = (By.CSS_SELECTOR, "pp-title")
    card_text = (By.CSS_SELECTOR, "input#number.card-input")
    card_code = (By.ID, "code")
    message_for_driver_button = (By.ID, "input-container")
    message_for_driver_text = (By.ID, "comment")
    reqs_button = (By.CSS_SELECTOR, "reqs-header")
    slider_button = (By.CSS_SELECTOR, "span.slider.round")
    plus_button = (By.CSS_SELECTOR, "counter-plus")
    final_blue_button (By.CSS_SELECTOR, "span.smart-button-main")



    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        #self.driver.find_element(*self.from_field).send_keys(from_address)
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.from_field)
        ).send_keys(from_address)

    def set_to(self, to_address):
        #self.driver.find_element(*self.to_field).send_keys(to_address)
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.to_field)
        ).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_request_taxi_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.request_taxi_button)
        )

    def click_on_request_taxi_button(self):
        self.get_request_taxi_button().click()

    def get_comfort_rate_icon(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.comfort_rate_icon)
        )

    def click_on_comfort_rate_icon(self):
        self.get_comfort_rate_icon().click()


    def get_phone_field_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.phone_field_button)
        )

    def click_on_phone_field_button(self):
        self.get_phone_field_button().click()

    def get_phone_field_text(self):
        return self.driver.find_element(*self.phone_field).get_attribute('value')

    def set_phone_field_text(self, phone_number):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.phone_field)
        ).send_keys(phone_number)

    def get_next_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.next_button)
        )

    def click_on_next_button(self):
        self.get_next_button().click()

    def get_confirm_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.confirm_button)
        )

    def click_on_confirm_button(self):
        self.get_confirm_button().click()

    def get_payment_method_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.payment_method_button)
        )

    def click_on_payment_method_button(self):
        self.get_payment_method_button().click()

    def get_add_card_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.add_card_button)
        )

    def click_on_add_card_button(self):
        self.get_add_card_button().click()

    def get_card_number_text(self):
        return self.driver.find_element(*self.card_text).get_attribute('value')

    def set_card_number_text(self, card_number):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.card_text)
        ).send_keys(data.card_number)

    def get_card_code(self):
        return self.driver.find_element(*self.card_code).get_attribute('value')

    def set_card_code(self, card_code):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.card_code)
        ).send_keys(data.card_code)

    def scroll_to_message_for_driver_button(self):
        driver.execute_script("arguments[0].scrollIntoView();", message_for_driver

    def get_message_for_driver_button(self):
            return WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.message_for_driver_button)
            )

    def click_on_message_for_driver_button(self):
            self.get_message_for_driver_button().click()

    def get_message_for_driver_text(self):
        return self.driver.find_element(*self.message_for_driver_button).get_attribute('value')

    def set_message_for_driver_text(self, card_number):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.message_for_driver_button)
        ).send_keys(data.message_for_driver)

    def scroll_to_reqs_button(self):
        driver.execute_script("arguments[0].scrollIntoView(); ", reqs_button

    def get_reqs_button(self):
            return WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.reqs_button)
            )

    def click_on_reqs_button(self):
            self.reqs_button.click()

    def get_slider_button(self):
            return WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.slider_button)
            )

    def click_on_slider_button(self):
            self.slider_button.click()

    def get_plus_button(self):
            return WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.plus_button)
            )

    def click_on_plus_button(self):
            self.plus_button.click()

    def get_final_blue_button(self):
            return WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.final_blue_button)
            )

    def click_on_final_blue_button(self):
            self.final_blue_button.click()


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

        cls.driver = webdriver.Chrome(service=Service(), options=options)

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
        assert routes_page.get_comfort_rate_icon().text in "Comfort"

    def test_set_phone_field_text(self):
        self.test_set_route()
        self.test_select_comfort_rate()
        routes_page = UrbanRoutesPage(self.driver)
        phone_number = data.phone_number
        routes_page.set_phone_field_text(phone_number)
        assert routes_page.get_phone_field_text() == phone_number

    def test_set_credit_card_text(self):
        self.test_set_route()
        self.test_select_comfort_rate()
        self.test_set_phone_field_text()
        routes_page = UrbanRoutesPage(self.driver)
        card_number = data.card_number
        routes_page.set_card_number_text(card_number)
        assert routes_page.get_card_number_text() == card_number

    def test_message_for_driver(self):
        self.test_set_route()
        self.test_select_comfort_rate()
        self.test_set_phone_field_text()
        self.test_set_credit_card_text()
        routes_page = UrbanRoutesPage(self.driver)
        message_for_driver = data.message_for_driver
        routes_page.set_message_for_driver_text(message_for_driver)
        assert routes_page.get_message_for_driver_text() == message_for_driver

    def test_request_blanket_and_tissues(self):
        self.test_set_route()
        self.test_select_comfort_rate()
        self.test_set_phone_field_text()
        self.test_set_credit_card_text()
        self.test_message_for_driver()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_slider_button()
        assert routes_page.get_slider_button().click

    def test_request_2_ice_creams(self):
        self.test_set_route()
        self.test_select_comfort_rate()
        self.test_set_phone_field_text()
        self.test_set_credit_card_text()
        self.test_message_for_driver()
        self.test_request_blanket_and_tissues()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_plus_button()
        routes_page.click_on_plus_button()
        assert routes_page.get_slider_button().click

    def test_get_reservation_popup_window(self):
        self.test_set_route()
        self.test_select_comfort_rate()
        self.test_set_phone_field_text()
        self.test_set_credit_card_text()
        self.test_message_for_driver()
        self.test_request_blanket_and_tissues()
        self.test_request_2_ice_creams()
        assert routes_page.get_final_blue_button().click


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
