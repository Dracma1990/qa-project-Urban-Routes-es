import data
import Selectors
import UrbanRoutesPage
import TestUrbanRoutes
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriver, WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from Selectors import blanket_button, comfort_rate_icon, final_blue_button, plus_button, ice_cream_label

from data import message_for_driver

driver = webdriver.Chrome()


# no modificar
def retrieve_phone_code(driver) -> str
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


def get_blanket_selected():
        Selectors.blanket_button.__getattribute__(Selectors, __class='r-sw-label')


def get_supportive_class():
        Selectors.comfort_rate_icon.__getattribute__(Selectors, __class='tcard-title')


def click_on_final_blue_button():
        Selectors.final_blue_button.click()


def click_on_plus_button():
        Selectors.plus_button.click()


def get_ice_cream_count():
        Selectors.ice_cream_label.__getattribute__(Selectors, __class='r-counter-label')


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

