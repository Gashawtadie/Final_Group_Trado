import random
import time

from pymongo import MongoClient
from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.support.select import Select

from Locators.all_locators import Locators
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class BaseSetups(Locators):

    def setup_trado(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver = webdriver.Chrome()
        self.driver.get(self.TRADO_HOME)
        self.driver.maximize_window()
        return self.driver

    def find(self, path, locator) -> webelement:
        return self.driver.find_element(path, locator)

    def click(self, path, locator):
        self.wait_until_element_is_visible(path, locator)
        self.find(path, locator).click()

    def fields(self, path, locate, values):
        self.wait_until_element_is_visible(path, locate)
        self.driver.find_element(path, locate).clear()
        self.driver.find_element(path, locate).send_keys(values)

    def selector(self, path, locate, choose):
        self.wait_until_element_is_visible(path, locate)
        element = Select(self.find(path, locate))
        element.select_by_visible_text(choose)

    def wait_until_element_is_visible(self, by, locate, time: int = 10):
        wait = WebDriverWait(self.driver, time)
        wait.until(ec.visibility_of_element_located((by, locate)))

    def assertion(self, path, error_path):
        self.wait_until_element_is_visible(path, error_path)
        return self.find(path, error_path).text

    def message(self, by, locate):
        self.wait_until_element_is_visible(by, locate)
        return self.find(by, locate).text

    def tear_down(self):
        self.driver.quit()

    def alert_ok_button(self, popup, time: int = 10):
        wait = WebDriverWait(self.driver, time)
        wait.until(ec.alert_is_present())

        alert = self.driver.switch_to.alert
        assert popup in alert.text
        alert.accept()

    def color_check_up(self, by, locate):
        category_color = self.find(by, locate).value_of_css_property('background-color')
        category_color = Color.from_string(category_color).hex
        print(category_color)

    def scroll_bar(self, by, locate):
        self.wait_until_element_is_visible(by, locate)
        self.driver.execute_script("window.scrollBy(0, Document.body.scrollHeight)")

    def checkbox(self, by, locate):
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((by, locate))).click()

    def home_page_extra(self, locater):
        self.driver.get(locater)
        return self.driver

    def code_generator(self):
        cluster = self.DB_CONNECTION
        db_client = MongoClient(cluster)
        db = db_client['trado_qa']
        collection = db['users']
        results = collection.find({"phone": '0502006336'})
        for reset in results:
            login_code = (reset['loginCode'])
            return login_code

    def up_down_scroll(self):
        return self.fields(By.XPATH, self.BN_NUMBER_UP, Keys.END)

    def price_assertion_with_mongodb(self):
        cluster = self.DB_CONNECTION
        db_client = MongoClient(cluster)
        db = db_client['trado_qa']
        collection = db['products']
        results = collection.find({"name": 'גורילה גלו'})
        for pro in results:
            price = (pro['price'])
            return price

    def amount_in_stock(self):
        cluster = self.DB_CONNECTION
        db_client = MongoClient(cluster)
        db = db_client['trado_qa']
        collection = db['products']
        results = collection.find({"name": 'סוכר'})
        for pro in results:
            qtn = (pro['salesQuantity'])
            return qtn

    def product_name_inStock(self):
        cluster = self.DB_CONNECTION
        db_client = MongoClient(cluster)
        db = db_client['trado_qa']
        collection = db['products']
        coll = collection.find({'name': "וודקה רוסקי סטנדרט"})
        for name in coll:
            pro_name = (name['price'])
            stock = (name['salesQuantity'])
            return pro_name, stock

    def users_first_name(self):
        cluster = self.DB_CONNECTION
        db_client = MongoClient(cluster)
        db = db_client['trado_qa']
        collection = db['users']
        coll = collection.find({'phone': '0502006336'})

        for name in coll:
            lname = (name['firstName'])
            return lname

    def product_name(self):
        cluster = self.DB_CONNECTION
        db_client = MongoClient(cluster)
        db = db_client['trado_qa']
        collection = db['products']
        coll = collection.find({'name': 'שמן למון קוש'})

        for name in coll:
            oil = (name['name'])
            return oil

    def product_category(self):
        cluster = self.DB_CONNECTION
        db_client = MongoClient(cluster)
        db = db_client['trado_qa']
        collection = db['departments']
        coll = collection.find_raw_batches({'active': 'true'})

        for x in coll:
            update = (x['lastUpdate'])
            return update

    def orders(self):
        cluster = self.DB_CONNECTION
        db_client = MongoClient(cluster)
        db = db_client['trado_qa']
        collection = db['orders']
        coll = collection.find_raw_batches({'firstName': 'team-3 0526802789'})

        for name in coll:
            oil = (name['status'])
            return oil

    def orders_payment_type(self):
        cluster = self.DB_CONNECTION
        db_client = MongoClient(cluster)
        db = db_client['trado_qa']
        collection = db['orders']
        coll = collection.find_raw_batches({'firstName': 'team-3 0526802789'})
        for name in coll:
            pay = (name['paymentType'])
            return pay

    def test_product_name_department(self):
        cluster = self.DB_CONNECTION
        db_client = MongoClient(cluster)
        db = db_client['trado_qa']
        collection = db['products']
        coll = collection.find({'name': 'שמן למון קוש'})

        for name in coll:
            oil = (name['departmentName'])
            print(oil)

    # def code_all(self, key, value):
    #     from pymongo import MongoClient
    #     cluster = self.DB_CONNECTION
    #     db_client = MongoClient(cluster)
    #     db = db_client['trado_qa']
    #     collection = db['products']
    #     results = collection.find_one({"name": f'{key}'})
    #     login_code = (results[f'{value}'])
    #     return login_code

    def code_registration(self):
        cluster = self.DB_CONNECTION
        db_client = MongoClient(cluster)
        db = db_client['trado_qa']
        collection = db['users']
        results = collection.find_one({"phone": '0545566770'})
        login_code = (results['loginCode'])
        return login_code

    def phone_gen(self):
        phone = random.randint(1000000000, 10000000000)
        return phone

    def set_page_load_timeout(self):
        return self.driver.set_page_load_timeout(7)

    def wait_until_ready(self):
        time.sleep(2)
