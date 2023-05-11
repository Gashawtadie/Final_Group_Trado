import time

import pytest
from selenium.webdriver.common.by import By
from Base_setups.main_setups import BaseSetups
import unittest


class TestMongoVsWebsite(BaseSetups):

    def product_name_in_data_matches_with_gui_display(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.XPATH, self.CANABIS_CATEGORY)
        self.click(By.XPATH, self.LEMON_OIL_PRO)
        self.click(By.XPATH, self.LEMON_ADD)
        assert self.assertion(By.XPATH, self.PRO_NAME_WITH_MONGO) == 'שמן למון קוש'
        assert self.product_name() == 'שמן למון קוש'

    def product_price(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.fields(By.XPATH, self.SEARCH_PRODUCTS, "גורילה גלו")
        self.click(By.XPATH, self.SEARCH_BUTTON)
        time.sleep(2)
        self.click(By.XPATH, self.SEARCH_LIST)
        assert self.assertion(By.CSS_SELECTOR, self.PRICE_PRODUCT) == 'עלות לקרטון: ₪27.90'
        assert self.price_assertion_with_mongodb() == 27.9

    def product_inStock(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.fields(By.XPATH, self.SEARCH_PRODUCTS, 'סוכר')
        self.click(By.XPATH, self.SEARCH_BUTTON)
        time.sleep(2)
        self.click(By.XPATH, self.SEARCH_LIST)
        assert self.assertion(By.CSS_SELECTOR, self.CARTON_IN_STOCK) == 'קרטונים במלאי:-1'
        assert self.amount_in_stock() == 40

    def product_price_inStock(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.fields(By.XPATH, self.SEARCH_PRODUCTS, "וודקה רוסקי סטנדרט")
        self.click(By.XPATH, self.SEARCH_BUTTON)
        time.sleep(2)
        self.click(By.XPATH, self.SEARCH_LIST)
        assert self.assertion(By.CSS_SELECTOR, self.PRICE_PRODUCT) == 'עלות לקרטון: ₪408.00'
        assert self.assertion(By.XPATH, self.PRO_QUEEN_INSTOCK) == 'קרטונים במלאי:-1'
        assert self.product_name_inStock() == (68, 486)

    def users_name_(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        time.sleep(2)
        self.click(By.CSS_SELECTOR, self.CONNECTION_REGISTER)
        self.fields(By.XPATH, self.PHONE_FIELD, "0502006336")
        self.checkbox(By.XPATH, self.CHECK_BOX)
        self.click(By.XPATH, self.CONNECT)
        self.click(By.XPATH, self.CODE0)
        self.fields(By.XPATH, self.FILL_ONE, self.code_generator()[0])
        self.click(By.XPATH, self.CODE1)
        self.fields(By.XPATH, self.FILL_TWO, self.code_generator()[1])
        self.click(By.XPATH, self.CODE2)
        self.fields(By.XPATH, self.FILL_THREE, self.code_generator()[2])
        self.click(By.XPATH, self.CODE3)
        self.fields(By.XPATH, self.FILL_FOUR, self.code_generator()[3])
        self.click(By.XPATH, self.CODE4)
        self.fields(By.XPATH, self.FILL_FIVE, self.code_generator()[4])
        self.click(By.XPATH, self.AUTHENTICATION)
        self.click(By.XPATH, self.HEAD_TITLE)
        assert self.assertion(By.XPATH, self.HEAD_TITLE) == 'שלום team-3 0526802789,\nאזור אישי'
        assert self.users_first_name() == 'peace'

    def product_category(self):
        self.setup_trado()
        self.click(By.XPATH, self.X_CLOSE_BTN)
        self.fields(By.XPATH, self.SEARCH_PRODUCTS, "קווין ג'קי")
        self.click(By.XPATH, self.SEARCH_BUTTON)
        time.sleep(2)
        self.click(By.XPATH, self.SEARCH_LIST)
        assert self.assertion(By.XPATH, self.QUEEN_GEL) == '₪2290.00'

    def orders_status(self):
        self.driver.get(self.HOME_ADMIN)
        self.driver.maximize_window()
        self.fields(By.XPATH, self.TELEPHONE_ADMIN, '1952222222')
        self.click(By.XPATH, self.CLICK_ADMIN)
        time.sleep(1)
        self.fields(By.XPATH, self.CODE_ADMIN, '1234')
        self.click(By.XPATH, self.CLICK_CODE)
        self.click(By.XPATH, self.ORDERS_ADMIN)
        self.click(By.XPATH, self.TEAM3_ORDERS)
        assert self.assertion(By.CSS_SELECTOR, self.STATUS_ORDERS) == 'התקבלה'
        assert self.orders() == 'received'

    def orders_payment_type(self):
        self.driver.get(self.HOME_ADMIN)
        self.driver.maximize_window()
        self.fields(By.XPATH, self.TELEPHONE_ADMIN, '1952222222')
        self.click(By.XPATH, self.CLICK_ADMIN)
        time.sleep(1)
        self.fields(By.XPATH, self.CODE_ADMIN, '1234')
        self.click(By.XPATH, self.CLICK_CODE)
        self.click(By.XPATH, self.ORDERS_ADMIN)
        self.click(By.XPATH, self.TEAM3_ORDERS)
        assert self.assertion(By.CSS_SELECTOR, self.PAYMENT_TYPE) == 'b2b'
        assert self.orders_payment_type() == 'b2b'  # team3 ordered with bank transfer payment method

    # def test_pic(self):
    #     self.driver.get(self.HOME_ADMIN)
    #     self.driver.maximize_window()
    #     self.fields(By.XPATH, self.TELEPHONE_ADMIN, '1952222222')
    #     self.click(By.XPATH, self.CLICK_ADMIN)
    #     time.sleep(1)
    #     self.fields(By.XPATH, self.CODE_ADMIN, '1234')
    #     self.click(By.XPATH, self.CLICK_CODE)
    #     self.click(By.XPATH, "//span[contains(text(),'מחלקות')]")
    #     self.click(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[1]/span[1]/i[1]")
    #     self.click(By.XPATH, "//span[contains(text(),'הוספה')]")
    #     self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/form[1]/div[1]/div[2]").send_keys("C://Users/user/Pictures/Saved/gashu.jpg")
    #

