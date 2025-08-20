from selenium.webdriver.common.by import By

class UrbanRoutesLocators:
    FROM_FIELD = (By.ID, 'from')
    TO_FIELD = (By.ID, 'to')
    FLASH_MODE_ACTIVE = (By.XPATH, '//div[@class="mode active" and text()="Flash"]')
    TAXI_ICON = (By.XPATH, '//img[contains(@src, "taxi-active")]')
    CALL_TAXI_BUTTON = (By.XPATH, '//button[contains(@class, "button round") and text()="Pedir un taxi"]')
    COMFORT_CARD = (By.XPATH, '//div[contains(@class, "tcard") and .//div[contains(text(), "Comfort")]]')
    PHONE_TRIGGER = (By.XPATH, '//div[text()="Número de teléfono"]')
    PHONE_INPUT_TAG = (By.TAG_NAME, "input")
    NEXT_BUTTON = (By.XPATH, '//button[text()="Siguiente"]')
    CODE_INPUT = (By.ID, "code")
    CONFIRM_BUTTON = (By.XPATH, '//button[text()="Confirmar"]')
    OVERLAY = (By.CSS_SELECTOR, "div.overlay")
    PAY_BUTTON = (By.CSS_SELECTOR, 'div.pp-button.filled')
    ADD_CARD_OPTION = (By.XPATH, '//div[contains(@class, "pp-row") and .//div[text()="Agregar tarjeta"]]')
    CARD_NUMBER_INPUT = (By.ID, "number")
    CARD_CODE_INPUT = (By.XPATH, '//input[@name="code"]')
    ADD_BUTTON = (By.XPATH, '//button[@type="submit" and contains(@class, "button full") and text()="Agregar"]')
    CLOSE_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    MESSAGE_INPUT = (By.ID, "comment")
    EXTRA_ITEMS_BLANKET_SWITCH = (
        By.XPATH,
        '//div[div[@class="r-sw-label" and text()="Manta y pañuelos"]]//span[@class="slider round"]'
    )
    ICE_CREAM_COUNT = (By.CSS_SELECTOR, "div.r-counter > div.counter > div.counter-value")
    ICE_CREAM_PLUS_BUTTON = (
        By.XPATH,
        '//div[div[@class="r-counter-label" and text()="Helado"]]//div[contains(@class, "counter-plus") and not(contains(@class, "disabled"))]'
    )
    TAXI_REQUEST_BUTTON = (By.XPATH, '//button[@class="smart-button" and .//span[text()="Pedir un taxi"]]')
    EXTRA_ITEMS_BLANKET_CHECKBOX = (By.CSS_SELECTOR, "div.r-type-switch:nth-child(1) input.switch-input")
    REQUEST_TAXI_BUTTON = (By.CSS_SELECTOR, "button.smart-button")
    CAR_MODAL_TITLE = (By.CLASS_NAME, "order-header-title")
    CAR_DETAILS_TITLE = (By.CLASS_NAME, "order-header-title")