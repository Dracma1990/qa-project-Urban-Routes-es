import data
import Selectors
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriver, WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from data import message_for_driver



class UrbanRoutesPage:

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        #self.driver.find_element(*self.from_field).send_keys(from_address)
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(Selectors.from_field)
        ).send_keys(from_address)

    def set_to(self, to_address):
        #self.driver.find_element(*self.to_field).send_keys(to_address)
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(Selectors.to_field)
        ).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*Selectors.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*Selectors.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_request_taxi_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(Selectors.request_taxi_button)
        )

    def click_on_request_taxi_button(self):
        self.get_request_taxi_button().click()

    def get_comfort_rate_icon(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(Selectors.comfort_rate_icon)
        )

    def click_on_comfort_rate_icon(self):
        self.get_comfort_rate_icon().click()

    def get_phone_field_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(Selectors.phone_field_button)
        )

    def click_on_phone_field_button(self):
        self.get_phone_field_button().click()

    def get_phone_field_text(self):
        return self.driver.find_element(*Selectors.phone_field).get_attribute('value')

    def set_phone_field_text(self, phone_number):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(Selectors.phone_field)
        ).send_keys(phone_number)

    def get_next_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(Selectors.next_button)
        )

    def click_on_next_button(self):
        self.get_next_button().click()

    def get_confirm_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(Selectors.confirm_button)
        )

    def click_on_confirm_button(self):
        self.get_confirm_button().click()

    def get_payment_method_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(Selectors.payment_method_button)
        )

    def click_on_payment_method_button(self):
        self.get_payment_method_button().click()

    def get_add_card_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(Selectors.add_card_button)
        )

    def click_on_add_card_button(self):
        self.get_add_card_button().click()

    def get_card_number_text(self):
        return self.driver.find_element(*Selectors.card_text).get_attribute('value')

    def set_card_number_text(self, card_number):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(Selectors.card_text)
        ).send_keys(data.card_number)

    def get_card_code(self):
        return self.driver.find_element(*Selectors.card_code).get_attribute('value')

    def set_card_code(self, card_code):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(Selectors.card_code)
        ).send_keys(data.card_code)

    def scroll_to_message_for_driver_button(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", message_for_driver)

    def get_message_for_driver_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(Selectors.message_for_driver_button)
        )

    def click_on_message_for_driver_button(self):
        self.get_message_for_driver_button().click()

    def get_message_for_driver_text(self):
        return self.driver.find_element(*Selectors.message_for_driver_button).get_attribute('value')

    def set_message_for_driver_text(self, card_number):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(Selectors.message_for_driver_button)
        ).send_keys(data.message_for_driver)

    def scroll_to_reqs_button(self):
        self.driver.execute_script("arguments[0].scrollIntoView(); ", Selectors.reqs_button)

    def get_reqs_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(Selectors.reqs_button)
        )

    def click_on_reqs_button(self):
        self.reqs_button.click()

    def get_slider_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(Selectors.slider_button)
        )

    def get_plus_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(Selectors.plus_button)
        )

    def car_modal_title(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(Selectors.car_modal_title)
        )

    def get_blanket_selected(self):
        Selectors.blanket_button.__getattribute__(Selectors, __class='r-sw-label')

    def get_supportive_class(self):
        Selectors.comfort_rate_icon.__getattribute__(Selectors, __class='tcard-title')

    # no modificar
    def retrieve_phone_code(driver) -> str:

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


    def get_blanket_selected():
        return None

    def click_on_plus_button():
        Selectors.plus_button.click()

    def get_ice_cream_count():
        # Selectors.ice_cream_label.__getattribute__(Selectors, __class='r-counter-label')
        return self.driver.find_element(*Selectors.ice_cream_label).get_text

    def click_on_final_blue_button():
        Selectors.car_modal_title.click()

    def click_on_slider_button():
        Selectors.slider_button.click()