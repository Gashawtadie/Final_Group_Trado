import time

import pytest
from selenium.webdriver.common.by import By

from Base_setups.main_setups import BaseSetups
from Locators.all_locators import Locators

class TestRegister(BaseSetups, Locators):

    def login(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.CSS_SELECTOR, self.CONNECTION_REGISTER)
        self.fields(By.XPATH, self.PHONE_FIELD, "0502006336")
        self.checkbox(By.XPATH, self.CHECK_BOX)
        self.click(By.XPATH, self.CONNECT)
        self.fields(By.XPATH, self.FILL_ONE, self.code_generator())
        self.click(By.XPATH, self.AUTHENTICATION)

    def test_register_positive(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.CSS_SELECTOR, self.CONNECTION_REGISTER)
        self.click(By.XPATH, self.REGISTER_BTN)
        self.fields(By.XPATH, self.TELEPHONE_REGISTER, '0789654120')
        self.fields(By.XPATH, self.BN_NUMBER, "51570246")
        self.checkbox(By.XPATH, self.REMIND_ME_BOX)
        self.click(By.XPATH, self.CONNECT_REGISTER_BTN)
        self.fields(By.XPATH, self.LOGIN_CODE1, self.code_registration())
        self.click(By.XPATH, self.ACCEPT_CODE_REGISTER)
        self.click(By.XPATH, self.REGI_STER)
        self.click(By.XPATH, self.REGI_CLICK)

    @pytest.mark.parametrize("phoneNo, BnNumber, messages", [('', '515074946', 'נא למלא שדה זה'),
                                                             ('', '', 'נא למלא שדה זה')])
    def test_negative_signup(self, phoneNo, BnNumber, messages):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.CSS_SELECTOR, self.CONNECTION_REGISTER)
        self.click(By.XPATH, self.REGISTER_BTN)
        self.fields(By.XPATH, self.TELEPHONE_REGISTER, phoneNo)
        self.fields(By.XPATH, self.BN_NUMBER, BnNumber)
        self.checkbox(By.XPATH, self.REMIND_ME_BOX)
        self.click(By.XPATH, self.CONNECT_REGISTER_BTN)
        self.message(By.XPATH, self.ERROR_PATH)

    @pytest.mark.parametrize("phoneNo, BnNumber, messages", [('111', '515074946', 'מס׳ טלפון לא תקין'),
                                                             ('1111111111111', '12445747', 'מס׳ טלפון לא תקין'),
                                                             ('@#$12afsdj', '48568762', 'מס׳ טלפון לא תקין'),
                                                             ('abcdef123456', '36985214', 'מס׳ טלפון לא תקין'),
                                                             ('acvfrdefg', '45867129', 'מס׳ טלפון לא תקין')])
    def test_telephone_notfix_signup(self, phoneNo, BnNumber, messages):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.CSS_SELECTOR, self.CONNECTION_REGISTER)
        self.click(By.XPATH, self.REGISTER_BTN)
        self.fields(By.XPATH, self.TELEPHONE_REGISTER, phoneNo)
        self.fields(By.XPATH, self.BN_NUMBER, BnNumber)
        self.checkbox(By.XPATH, self.REMIND_ME_BOX)
        self.click(By.XPATH, self.CONNECT_REGISTER_BTN)
        assert self.assertion(By.XPATH, self.ERROR_TELEPHONE_NOTFIX) == messages

    def without_checkbox(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.CSS_SELECTOR, self.CONNECTION_REGISTER)
        self.click(By.XPATH, self.REGISTER_BTN)
        self.fields(By.XPATH, self.TELEPHONE_REGISTER, "0521234567")
        self.fields(By.XPATH, self.BN_NUMBER, "")
        self.click(By.XPATH, self.CHECK_BOX_TWO)
        self.click(By.XPATH, self.CONNECT_REGISTER_BTN)
        assert self.message(By.XPATH, self.APPROVED_POLICY) == 'Please Approve Our Policy'

    @pytest.mark.parametrize("phoneNo, BnNumber, messages", [('0521234567', '515074946', 'שדה צריך להיות ייחודיי'),
                                                             ('0521234567', '515074946', 'שדה צריך להיות ייחודיי')])
    def test_with_two_checkbox_assign(self, phoneNo, BnNumber, messages):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.CSS_SELECTOR, self.CONNECTION_REGISTER)
        self.click(By.XPATH, self.REGISTER_BTN)
        self.fields(By.XPATH, self.TELEPHONE_REGISTER, phoneNo)
        self.fields(By.XPATH, self.BN_NUMBER, BnNumber)
        self.checkbox(By.XPATH, self.REMIND_ME_BOX)
        self.click(By.XPATH, self.CONNECT_REGISTER_BTN)
        assert self.message(By.XPATH, self.BN_NUMBER_ERROR) == messages

    def without_checkbox_assign(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.CSS_SELECTOR, self.CONNECTION_REGISTER)
        self.click(By.XPATH, self.REGISTER_BTN)
        self.fields(By.XPATH, self.TELEPHONE_REGISTER, "0521234567")
        self.fields(By.XPATH, self.BN_NUMBER, "515074946")
        self.click(By.XPATH, self.CHECK_BOX_TWO)
        self.click(By.XPATH, self.CONNECT_REGISTER_BTN)
        assert self.message(By.XPATH, self.APPROVED_POLICY) == 'Please Approve Our Policy'

    def register_with_google(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.CSS_SELECTOR, self.CONNECTION_REGISTER)
        self.click(By.XPATH, self.REGISTER_BTN)
        self.click(By.XPATH, self.GOOGLE)
        assert self.assertion(By.XPATH, self.GO_404) == "שגיאה 400: redirect_uri_mismatch"

    def register_with_fb(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.CSS_SELECTOR, self.CONNECTION_REGISTER)
        self.click(By.XPATH, self.REGISTER_BTN)
        self.click(By.XPATH, self.FB)

    def register_with_twitt(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.CSS_SELECTOR, self.CONNECTION_REGISTER)
        self.click(By.XPATH, self.REGISTER_BTN)
        self.click(By.XPATH, self.TWITT)

    def test_click_addorder_payment(self):
        self.setup_trado()
        self.click(By.XPATH, self.X_CLOSE_BTN)
        num = 0
        orders = []
        for products in range(2):
            self.click(By.XPATH,
                       f"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[3]/a[{num + 1}]/div[1]/div[2]/div[2]/div[1]")
            self.click(By.XPATH, self.X_CLOSE_BTN)
            orders.append(self.click(By.XPATH, self.TOTAL_ADD))
            self.wait_until_ready()
            self.driver.back()
            self.click(By.XPATH, self.X_CLOSE_BTN)
            num += 1
            # self.wait_until_ready()

            self.click(By.XPATH, self.CHECKOUT)
            self.fields(By.XPATH, self.PHONE_FIELD, "0502006336")
            self.checkbox(By.XPATH, self.CHECK_BOX)
            self.click(By.XPATH, self.CONNECT)
            self.fields(By.XPATH, self.FILL_ONE, self.code_generator())
            self.click(By.XPATH, self.AUTHENTICATION)
            self.click(By.XPATH, self.CHECKOUT)
            self.fields(By.XPATH, self.BUSINESS_NAME_FIELD, "Teamthree")
            self.fields(By.XPATH, self.BN_NUMBER_FIELD, "515074946")
            self.fields(By.XPATH, self.EMAIL_FIELD, "abcd@gmail.com")
            self.fields(By.XPATH, self.CITY_FIELD, "באר שבע, Israel")
            self.fields(By.XPATH, self.STREET_FIELD, "5")
            self.fields(By.XPATH, self.NUMBER_FIELD, "3")
            self.fields(By.XPATH, self.ENTRANCE_FIELD, "5")
            self.fields(By.XPATH, self.FLOOR_FIELD, "8")
            self.fields(By.XPATH, self.DELIVERY_CITY_FIELD, "תל אביב, Israel")
            self.fields(By.XPATH, self.DELIVERY_STREET_FIELD, "5")
            self.fields(By.XPATH, self.DELIVERY_NUMBER_FIELD, "7")
            self.fields(By.XPATH, self.DELIVERY_ENTRANCE_FIELD, "9")
            self.fields(By.XPATH, self.DELIVERY_FLOOR_FIELD, "3")
            self.fields(By.XPATH, self.CONTACT_RECIVER_NAME, "team")
            self.fields(By.XPATH, self.FIRST_NAME_FIELD, "team-3")
            self.fields(By.XPATH, self.LAST_NAME_FIELD, "team-3")
            self.fields(By.XPATH, self.TELEPHONE_FIELD, "0526802789")
            self.click(By.XPATH, self.COMPLETE_PURCHASE)
            self.click(By.XPATH, self.B2B_METHOD)
            self.fields(By.XPATH, self.BN_NUMBER_PAYMENT, "5251784945")
            self.fields(By.XPATH, self.BN_CUSTOMER_ID, "557")
            self.click(By.XPATH, self.CONFIRM_TRANSFER)
            self.click(By.XPATH, self.PURCHASE)
            assert self.assertion(By.XPATH, self.SUCCESS_TITLE) == 'תודה שהזמנת דרכנו!'
            self.click(By.XPATH, self.BACK_TO_HOME)
            self.tear_down()
