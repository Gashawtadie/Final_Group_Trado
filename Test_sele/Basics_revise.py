import random
import time

from pymongo import MongoClient
from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.support.select import Select

from Test_sele.locating_revise import Locatores
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.wait import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager


class BasePage(Locatores):

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.FENDI_HOME)
        self.driver.maximize_window()
        return self.driver

    def find(self, path, locator):
        return self.driver.find_element(path, locator)

    def click(self, path, locatores):
        self.until_element_is_visible(path, locatores)
        self.find(path, locatores).click()

    def field(self, path, locate):
        self.until_element_is_visible(path, locate)
        self.find(path, locate).clear()
        self.find(path, locate).send_keys()

    def select(self, path, locate, value):
        self.until_element_is_visible(path, locate)
        element = Select(self.find(path, locate))
        element.select_by_visible_text(value)

    def until_element_is_visible(self, path, locater, time: int = 10):
        wait = WebDriverWait(self.driver, time)
        wait.until(ec.visibility_of_element_located((path, locater)))

    def assertion(self, by, locate):
        self.until_element_is_visible(by, locate)
        return self.find(by, locate).text

    def popup(self, time: int = 10):
        wait = WebDriverWait(self.driver, time)
        wait.until(ec.alert_is_present())

