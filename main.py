import data
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import UrbanRoutesLocators
from selenium.common.exceptions import TimeoutException


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
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


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    def __init__(self, driver):
        self.COMFORT_CARD = UrbanRoutesLocators.COMFORT_CARD
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def get_supportive_class(self):
        class_element = self.driver.find_element(*self.COMFORT_CARD).get_attribute("class")
        return class_element

    def setup_method(self):
        self.routes_page = UrbanRoutesPage(self.driver)

    def get_blanket_selected(self):
        checkbox = self.driver.find_element(*UrbanRoutesLocators.EXTRA_ITEMS_BLANKET_CHECKBOX)
        return checkbox.get_attribute("checked")

    def get_ice_cream_count(self):
        count_element = self.driver.find_element(*UrbanRoutesLocators.ICE_CREAM_COUNT)
        return count_element.text

    def get_car_modal_title(self):
        title_element = self.driver.find_element(*UrbanRoutesLocators.CAR_MODAL_TITLE)
        return title_element.text

    def get_car_details_title(self):
        element = self.driver.find_element(*UrbanRoutesLocators.CAR_DETAILS_TITLE)
        return element.text


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=options)

    # Prueba 1: Agregar dirección
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(UrbanRoutesPage.from_field))
        wait.until(EC.presence_of_element_located(UrbanRoutesPage.to_field))

        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        assert routes_page.get_from() == address_from  # get_from() y get_to(), Estos ya los tienes, pero para todas las 8 pruebas nos haría falta crear aserciones...
        assert routes_page.get_to() == address_to

    # Prueba 2: Seleccionar tarifa "Comfort"
    def test_select_comfort_tariff(self):
        wait = WebDriverWait(self.driver, 10)
        routes_page = UrbanRoutesPage(self.driver)

        wait.until(EC.presence_of_element_located(UrbanRoutesLocators.FLASH_MODE_ACTIVE))

        taxi_icon = wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.TAXI_ICON))
        taxi_icon.click()

        call_taxi_btn = wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.CALL_TAXI_BUTTON))
        call_taxi_btn.click()

        comfort_card = wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.COMFORT_CARD))
        comfort_card.click()
        assert "active" in routes_page.get_supportive_class()

    # Prueba 3: Añadir número de teléfono
    def test_set_phone_number(self):
        wait = WebDriverWait(self.driver, 10)
        routes_page = UrbanRoutesPage(self.driver)

        toggle = wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.PHONE_TRIGGER))
        try:
            toggle.click()
        except:
            self.driver.execute_script("arguments[0].click();", toggle)

        toggle = wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.PHONE_TRIGGER))
        try:
            toggle.click()
        except:
            self.driver.execute_script("arguments[0].click();", toggle)

        phone_inputs = wait.until(
            lambda d: [
                          inp for inp in d.find_elements(*UrbanRoutesLocators.PHONE_INPUT_TAG)
                          if inp.is_displayed() and inp.is_enabled()
                      ] or False
        )
        phone_input = phone_inputs[0]

        phone_input.clear()
        phone_input.send_keys(data.phone_number)
        assert phone_input.get_attribute("value") == data.phone_number

        next_btn = wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.NEXT_BUTTON))
        next_btn.click()

        code_input = wait.until(EC.visibility_of_element_located(UrbanRoutesLocators.CODE_INPUT))
        test_code = retrieve_phone_code(self.driver)

        code_input.clear()
        code_input.send_keys(test_code)
        assert code_input.get_attribute("value") == test_code

        confirm_btn = wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.CONFIRM_BUTTON))
        confirm_btn.click()

    # Prueba 4: Agregar una tarjeta de crédito
    def test_add_credit_card(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.invisibility_of_element_located(UrbanRoutesLocators.OVERLAY))

        pay_button = wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.PAY_BUTTON))
        self.driver.execute_script("arguments[0].click();", pay_button)

        add_card_option = wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.ADD_CARD_OPTION))
        try:
            add_card_option.click()
        except:
            self.driver.execute_script("arguments[0].click();", add_card_option)

        number_input = wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.CARD_NUMBER_INPUT))
        number_input.click()
        number_input.clear()
        number_input.send_keys(data.card_number)

        code_input = self.driver.find_element(*UrbanRoutesLocators.CARD_CODE_INPUT)
        code_input.click()
        code_input.clear()
        code_input.send_keys(data.card_code)

        self.driver.execute_script("arguments[0].blur();", code_input)

        add_btn = wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.ADD_BUTTON))
        add_btn.click()

        try:
            close_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(UrbanRoutesLocators.CLOSE_BUTTON)
            )
            close_btn.click()
        except TimeoutException:
            pass

        assert number_input.get_attribute("value") == data.card_number

    # Prueba 5: Escribir un mensaje para el conductor
    def test_write_message_for_driver(self):
        wait = WebDriverWait(self.driver, 10)
        message_input = wait.until(EC.presence_of_element_located(UrbanRoutesLocators.MESSAGE_INPUT))
        message_input.clear()
        message_input.send_keys(data.message_for_driver)
        assert message_input.get_attribute("value") == data.message_for_driver

    # Prueba 6: Pedir manta y pañuelos
    def test_request_blanket_and_tissues(self):
        wait = WebDriverWait(self.driver, 10)
        routes_page = UrbanRoutesPage(self.driver)
        switch = wait.until(EC.presence_of_element_located(UrbanRoutesLocators.EXTRA_ITEMS_BLANKET_SWITCH))
        self.driver.execute_script("arguments[0].click();", switch)
        assert routes_page.get_blanket_selected() == "true"

    # Prueba 7: Pedir 2 helados
    def test_request_two_icecreams(self):
        wait = WebDriverWait(self.driver, 10)
        routes_page = UrbanRoutesPage(self.driver)

        plus_button = wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.ICE_CREAM_PLUS_BUTTON))
        plus_button.click()
        time.sleep(0.5)  # espera corta para que la UI actualice
        plus_button.click()

        assert routes_page.get_ice_cream_count() == "2"

    # Prueba 8: Clic en "Pedir un taxi"
    def test_click_request_taxi_button(self):
        wait = WebDriverWait(self.driver, 2)
        routes_page = UrbanRoutesPage(self.driver)
        taxi_button = wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.TAXI_REQUEST_BUTTON))
        self.driver.execute_script("arguments[0].click();", taxi_button)
        assert routes_page.get_car_modal_title() == "Buscar automóvil"

    # Prueba 9: Esperar 30 segundos para que aparezca la información del conductor (opcional)
    def test_wait_for_driver_info(self):
        wait = WebDriverWait(self.driver, 30)
        routes_page = UrbanRoutesPage(self.driver)
        wait.until(EC.presence_of_element_located(UrbanRoutesLocators.CAR_DETAILS_TITLE))
        assert "Buscar automóvil" in routes_page.get_car_details_title()

    # Cerrar el navegador
    @classmethod
    def teardown_class(cls):
        time.sleep(60)
        cls.driver.quit()