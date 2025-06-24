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
from Selectors import blanket_button, comfort_rate_icon, car_modal_title, plus_button, ice_cream_label

from data import message_for_driver


