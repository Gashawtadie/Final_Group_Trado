import time
import pymongo
import pytest
from pymongo import MongoClient
from selenium.webdriver.common.by import By

from Base_setups.main_setups import BaseSetups


class TestImportants(BaseSetups):
    def test_who_we_are(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.XPATH, self.WHO_WE_ARE)
        self.home_page_extra(self.HOME_PAGE_EXTRA)
        self.click(By.XPATH, self.TRADING_PAGE)
        self.home_page_extra(self.TRADO_ANOTHER_HOME)
        self.click(By.XPATH, self.CHICKENS)
        self.checkbox(By.XPATH, self.PUB_BAR)
        self.click(By.XPATH, self.PUB_BAR)
        self.click(By.XPATH, self.SUPERMARKET)
        self.click(By.XPATH, self.SAVE_CHOICES)
        # self.click(By.XPATH, self.CLOSEBTN)
        # self.click(By.XPATH, self.EXTRA_PROFILES)
        # time.sleep(5)

    def test_my_account(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.XPATH, self.MY_ACCOUNT)
        self.click(By.XPATH, self.REGISTER_BTN)
        self.fields(By.XPATH, self.TELEPHONE_REGISTER, '0545566777')
        self.fields(By.XPATH, self.BN_NUMBER, "51570223")
        self.checkbox(By.XPATH, self.REMIND_ME_BOX)
        self.click(By.XPATH, self.CONNECT_REGISTER_BTN)
        self.fields(By.XPATH, self.LOGIN_CODE1, self.code_registration())
        self.click(By.XPATH, self.ACCEPT_CODE_REGISTER)

    def test_my_account_withlogin(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.XPATH, self.MY_ACCOUNT)
        self.fields(By.XPATH, self.PHONE_FIELD, "0591111113")
        self.checkbox(By.XPATH, self.CHECK_BOX)
        self.click(By.XPATH, self.CONNECT)

        self.click(By.XPATH, self.AUTHENTICATION)
        time.sleep(2)

    def test_e_trado_withlogin(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.XPATH, self.E_TRADO)
        self.click(By.XPATH, self.ENTRANCE_ETARDO)
        self.fields(By.XPATH, self.PHONE_FIELD, "0591111113")
        self.checkbox(By.XPATH, self.CHECK_BOX)
        self.click(By.XPATH, self.CONNECT)
        self.fields(By.XPATH, self.FILL_FIVE, "8")
        self.fields(By.XPATH, self.FILL_FOUR, "6")
        self.fields(By.XPATH, self.FILL_THREE, "1")
        self.fields(By.XPATH, self.FILL_TWO, "3")
        self.fields(By.XPATH, self.FILL_ONE, "1")
        self.click(By.XPATH, self.AUTHENTICATION)
        time.sleep(2)

    def test_etrado_register(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.XPATH, self.E_TRADO)
        self.click(By.XPATH, self.ENTRANCE_ETARDO)
        self.click(By.XPATH, self.REGISTER_BTN)
        self.fields(By.XPATH, self.TELEPHONE_REGISTER, "1234567821")
        self.fields(By.XPATH, self.BN_NUMBER, "515074946")
        self.checkbox(By.XPATH, self.REMIND_ME_BOX)
        self.click(By.XPATH, self.CONNECT_REGISTER_BTN)
        self.fields(By.XPATH, self.LOGIN_CODE5, "")
        self.fields(By.XPATH, self.LOGIN_CODE4, "")
        self.fields(By.XPATH, self.LOGIN_CODE3, "")
        self.fields(By.XPATH, self.LOGIN_CODE2, "")
        self.fields(By.XPATH, self.LOGIN_CODE1, "")
        self.click(By.XPATH, self.ACCEPT_CODE_REGISTER)

    def test_contact_us(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.XPATH, self.CONTACT_US)
        self.fields(By.XPATH, self.PERSONAL_NAME, "gashu")
        self.fields(By.XPATH, self.LAST_NAME_CONTACT, "tade")
        self.fields(By.XPATH, self.EMAIL_CONTACT, "gashumec@gmail.com")
        self.fields(By.XPATH, self.PHONE_CONTACT, "0526162719")
        self.fields(By.XPATH, self.CONTENT, "its unrated website")
        self.click(By.XPATH, self.SEND_CONTACT)

    @pytest.mark.parametrize("fname, lname, email, phoneno, comment, message",
                             [('love', '', 'gashu@gmail.com', '0521234568', 'we love it', 'נא למלא שדה זה'),
                              ('', 'love', 'gashu@gmail.com', '0521234568', 'we love it', 'נא למלא שדה זה'),
                              ('one', 'love', '', '0521234568', 'we love it', 'נא למלא שדה זה'),
                              ('unit', 'peace', 'gashu@gmail.com', '', 'we like it', 'נא למלא שדה זה'),
                              ('', '', 'gashu@gmail.com', '0521234568', 'keep up', 'נא למלא שדה זה'),
                              ('peace', 'love', 'gashu@gmail.com', '0521234568', '',),
                              ('love', '', '', '0521234568', 'keep up', 'נא למלא שדה זה'),
                              ('love', '', 'gashu@gmail.com', '', 'keep up', 'נא למלא שדה זה'),
                              ('', 'love', '', '1234567895', 'keep up', 'נא למלא שדה זה'),
                              ('peace', 'love', '', '', 'keep up', 'נא למלא שדה זה'),
                              ('peace', '', '', '', '', 'נא למלא שדה זה'),
                              ('', '', '', '', '', 'נא למלא שדה זה'),
                              ('', 'love', 'abcd@gmail.com', '', '', 'נא למלא שדה זה'),
                              ])
    def test_contact_us_negative_lname(self, fname, lname, email, phoneno, comment, message):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.XPATH, self.CONTACT_US)
        self.fields(By.XPATH, self.PERSONAL_NAME, fname)
        self.fields(By.XPATH, self.LAST_NAME_CONTACT, lname)
        self.fields(By.XPATH, self.EMAIL_CONTACT, email)
        self.fields(By.XPATH, self.PHONE_CONTACT, phoneno)
        self.fields(By.XPATH, self.CONTENT, comment)
        self.click(By.XPATH, self.SEND_CONTACT)
        assert self.assertion(By.XPATH, self.ERROR_MESSAGE) == message

    # Meshek business

    def test_business_path(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.XPATH, self.MESHEK_BUSINESS)
        self.fields(By.XPATH, self.LTD_NAME, "three")
        self.fields(By.XPATH, self.LTD_LAST, "two")
        self.fields(By.XPATH, self.LTD_BNNUMBER, "507504946")
        self.fields(By.XPATH, self.LTD_BUSINESS_NAME, "tara")
        self.selector(By.XPATH, self.SELECTOR, "מסעדות")
        self.fields(By.XPATH, self.YOUR_PHONE, "0512689745")
        self.fields(By.XPATH, self.EMAIL_LTD, "abcd@gmail.com")
        self.fields(By.XPATH, self.CITY_LTD, "beersehva")
        self.fields(By.XPATH, self.STREET_LTD, "45")
        self.fields(By.XPATH, self.HOUSE_NO, "13")
        self.click(By.XPATH, self.SEND_REQUEST)
        assert self.assertion(By.XPATH, self.ACCEPT_POLICY_LTD) == 'Please Approve Our Policy'

    def test_business_invalid_name(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.XPATH, self.MESHEK_BUSINESS)
        self.fields(By.XPATH, self.LTD_NAME, "")
        self.fields(By.XPATH, self.LTD_LAST, "two")
        self.fields(By.XPATH, self.LTD_BNNUMBER, "507504946")
        self.fields(By.XPATH, self.LTD_BUSINESS_NAME, "tara")
        self.selector(By.XPATH, self.SELECTOR, "מסעדות")
        self.fields(By.XPATH, self.YOUR_PHONE, "0512689745")
        self.fields(By.XPATH, self.EMAIL_LTD, "abcd@gmail.com")
        self.fields(By.XPATH, self.CITY_LTD, "beersehva")
        self.fields(By.XPATH, self.STREET_LTD, "45")
        self.fields(By.XPATH, self.HOUSE_NO, "13")
        self.click(By.XPATH, self.SEND_REQUEST)
        assert self.assertion(By.XPATH, self.ERROR_MSG) == 'נא למלא שדה זה'

    def test_business_invalid_last(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.XPATH, self.MESHEK_BUSINESS)
        self.fields(By.XPATH, self.LTD_NAME, "yes")
        self.fields(By.XPATH, self.LTD_LAST, "")
        self.fields(By.XPATH, self.LTD_BNNUMBER, "507504946")
        self.fields(By.XPATH, self.LTD_BUSINESS_NAME, "tara")
        self.selector(By.XPATH, self.SELECTOR, "מסעדות")
        self.fields(By.XPATH, self.YOUR_PHONE, "0512689745")
        self.fields(By.XPATH, self.EMAIL_LTD, "abcd@gmail.com")
        self.fields(By.XPATH, self.CITY_LTD, "beersehva")
        self.fields(By.XPATH, self.STREET_LTD, "45")
        self.fields(By.XPATH, self.HOUSE_NO, "13")
        self.click(By.XPATH, self.SEND_REQUEST)
        assert self.assertion(By.XPATH, self.ERROR_MSG) == 'נא למלא שדה זה'

    def test_business_invalid_bnnumber(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.XPATH, self.MESHEK_BUSINESS)
        self.fields(By.XPATH, self.LTD_NAME, "yes")
        self.fields(By.XPATH, self.LTD_LAST, "love")
        self.fields(By.XPATH, self.LTD_BNNUMBER, "")
        self.fields(By.XPATH, self.LTD_BUSINESS_NAME, "tara")
        self.selector(By.XPATH, self.SELECTOR, "מסעדות")
        self.fields(By.XPATH, self.YOUR_PHONE, "0512689745")
        self.fields(By.XPATH, self.EMAIL_LTD, "abcd@gmail.com")
        self.fields(By.XPATH, self.CITY_LTD, "beersehva")
        self.fields(By.XPATH, self.STREET_LTD, "45")
        self.fields(By.XPATH, self.HOUSE_NO, "13")
        self.click(By.XPATH, self.SEND_REQUEST)
        assert self.assertion(By.XPATH, self.ERROR_MSG) == 'נא למלא שדה זה'

    def test_business_invalid_businessName(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.XPATH, self.MESHEK_BUSINESS)
        self.fields(By.XPATH, self.LTD_NAME, "yes")
        self.fields(By.XPATH, self.LTD_LAST, "love")
        self.fields(By.XPATH, self.LTD_BNNUMBER, "507564946")
        self.fields(By.XPATH, self.LTD_BUSINESS_NAME, "")
        self.selector(By.XPATH, self.SELECTOR, "מסעדות")
        self.fields(By.XPATH, self.YOUR_PHONE, "0512689745")
        self.fields(By.XPATH, self.EMAIL_LTD, "abcd@gmail.com")
        self.fields(By.XPATH, self.CITY_LTD, "beersehva")
        self.fields(By.XPATH, self.STREET_LTD, "45")
        self.fields(By.XPATH, self.HOUSE_NO, "13")
        self.click(By.XPATH, self.SEND_REQUEST)
        assert self.assertion(By.XPATH, self.ERROR_MSG) == 'נא למלא שדה זה'

    def test_business_invalid_category(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.XPATH, self.MESHEK_BUSINESS)
        self.fields(By.XPATH, self.LTD_NAME, "yes")
        self.fields(By.XPATH, self.LTD_LAST, "love")
        self.fields(By.XPATH, self.LTD_BNNUMBER, "507564946")
        self.fields(By.XPATH, self.LTD_BUSINESS_NAME, "tara")
        # self.selector(By.XPATH, self.SELECTOR, "")
        self.fields(By.XPATH, self.YOUR_PHONE, "0512689745")
        self.fields(By.XPATH, self.EMAIL_LTD, "abcd@gmail.com")
        self.fields(By.XPATH, self.CITY_LTD, "rishon")
        self.fields(By.XPATH, self.STREET_LTD, "45")
        self.fields(By.XPATH, self.HOUSE_NO, "13")
        self.click(By.XPATH, self.SEND_REQUEST)
        assert self.assertion(By.XPATH, self.ERROR_MSG) == 'נא למלא שדה זה'

    def test_business_invalid_phone(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.XPATH, self.MESHEK_BUSINESS)
        self.fields(By.XPATH, self.LTD_NAME, "yes")
        self.fields(By.XPATH, self.LTD_LAST, "love")
        self.fields(By.XPATH, self.LTD_BNNUMBER, "507564946")
        self.fields(By.XPATH, self.LTD_BUSINESS_NAME, "tara")
        self.selector(By.XPATH, self.SELECTOR, "מסעדות")
        self.fields(By.XPATH, self.YOUR_PHONE, "")
        self.fields(By.XPATH, self.EMAIL_LTD, "abcd@gmail.com")
        self.fields(By.XPATH, self.CITY_LTD, "telaviv")
        self.fields(By.XPATH, self.STREET_LTD, "45")
        self.fields(By.XPATH, self.HOUSE_NO, "13")
        self.click(By.XPATH, self.SEND_REQUEST)
        assert self.assertion(By.XPATH, self.ERROR_MSG) == 'נא למלא שדה זה'

    def test_business_invalid_email(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.XPATH, self.MESHEK_BUSINESS)
        self.fields(By.XPATH, self.LTD_NAME, "yes")
        self.fields(By.XPATH, self.LTD_LAST, "love")
        self.fields(By.XPATH, self.LTD_BNNUMBER, "507564946")
        self.fields(By.XPATH, self.LTD_BUSINESS_NAME, "tara")
        self.selector(By.XPATH, self.SELECTOR, "מסעדות")
        self.fields(By.XPATH, self.YOUR_PHONE, "124567896")
        self.fields(By.XPATH, self.EMAIL_LTD, "")
        self.fields(By.XPATH, self.CITY_LTD, "telaviv")
        self.fields(By.XPATH, self.STREET_LTD, "45")
        self.fields(By.XPATH, self.HOUSE_NO, "13")
        self.click(By.XPATH, self.SEND_REQUEST)
        assert self.assertion(By.XPATH, self.ERROR_MSG) == 'נא למלא שדה זה'

    def test_business_invalid_city(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.XPATH, self.MESHEK_BUSINESS)
        self.fields(By.XPATH, self.LTD_NAME, "yes")
        self.fields(By.XPATH, self.LTD_LAST, "love")
        self.fields(By.XPATH, self.LTD_BNNUMBER, "507564946")
        self.fields(By.XPATH, self.LTD_BUSINESS_NAME, "tara")
        self.selector(By.XPATH, self.SELECTOR, "מסעדות")
        self.fields(By.XPATH, self.YOUR_PHONE, "124567896")
        self.fields(By.XPATH, self.EMAIL_LTD, "abcd@gmail.com")
        self.fields(By.XPATH, self.CITY_LTD, "")
        self.fields(By.XPATH, self.STREET_LTD, "45")
        self.fields(By.XPATH, self.HOUSE_NO, "13")
        self.click(By.XPATH, self.SEND_REQUEST)
        assert self.assertion(By.XPATH, self.ERROR_MSG) == 'נא למלא שדה זה'

    def test_business_invalid_street(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.XPATH, self.MESHEK_BUSINESS)
        self.fields(By.XPATH, self.LTD_NAME, "yes")
        self.fields(By.XPATH, self.LTD_LAST, "love")
        self.fields(By.XPATH, self.LTD_BNNUMBER, "507564946")
        self.fields(By.XPATH, self.LTD_BUSINESS_NAME, "tara")
        self.selector(By.XPATH, self.SELECTOR, "מסעדות")
        self.fields(By.XPATH, self.YOUR_PHONE, "124567896")
        self.fields(By.XPATH, self.EMAIL_LTD, "abcd@gmail.com")
        self.fields(By.XPATH, self.CITY_LTD, "jerusalem")
        self.fields(By.XPATH, self.STREET_LTD, "")
        self.fields(By.XPATH, self.HOUSE_NO, "13")
        self.click(By.XPATH, self.SEND_REQUEST)
        assert self.assertion(By.XPATH, self.ERROR_MSG) == 'נא למלא שדה זה'

    def test_business_invalid_houseNo(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.XPATH, self.MESHEK_BUSINESS)
        self.fields(By.XPATH, self.LTD_NAME, "yes")
        self.fields(By.XPATH, self.LTD_LAST, "love")
        self.fields(By.XPATH, self.LTD_BNNUMBER, "507564946")
        self.fields(By.XPATH, self.LTD_BUSINESS_NAME, "tara")
        self.selector(By.XPATH, self.SELECTOR, "מסעדות")
        self.fields(By.XPATH, self.YOUR_PHONE, "124567896")
        self.fields(By.XPATH, self.EMAIL_LTD, "abcd@gmail.com")
        self.fields(By.XPATH, self.CITY_LTD, "jerusalem")
        self.fields(By.XPATH, self.STREET_LTD, "45")
        self.fields(By.XPATH, self.HOUSE_NO, "")
        self.click(By.XPATH, self.SEND_REQUEST)
        assert self.assertion(By.XPATH, self.ERROR_MSG) == 'נא למלא שדה זה'

    def test_business_invalid_all_empty(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.XPATH, self.MESHEK_BUSINESS)
        self.fields(By.XPATH, self.LTD_NAME, "")
        self.fields(By.XPATH, self.LTD_LAST, "")
        self.fields(By.XPATH, self.LTD_BNNUMBER, "")
        self.fields(By.XPATH, self.LTD_BUSINESS_NAME, "")
        # self.selector(By.XPATH, self.SELECTOR, "")
        self.fields(By.XPATH, self.YOUR_PHONE, "")
        self.fields(By.XPATH, self.EMAIL_LTD, "")
        self.fields(By.XPATH, self.CITY_LTD, "")
        self.fields(By.XPATH, self.STREET_LTD, "")
        self.fields(By.XPATH, self.HOUSE_NO, "")
        self.click(By.XPATH, self.SEND_REQUEST)
        assert self.assertion(By.XPATH, self.ERROR_MSG) == 'נא למלא שדה זה'

    def test_business_name_last_invalid(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.XPATH, self.MESHEK_BUSINESS)
        self.fields(By.XPATH, self.LTD_NAME, "")
        self.fields(By.XPATH, self.LTD_LAST, "")
        self.fields(By.XPATH, self.LTD_BNNUMBER, "507564946")
        self.fields(By.XPATH, self.LTD_BUSINESS_NAME, "tara")
        self.selector(By.XPATH, self.SELECTOR, "מסעדות")
        self.fields(By.XPATH, self.YOUR_PHONE, "124567896")
        self.fields(By.XPATH, self.EMAIL_LTD, "abcd@gmail.com")
        self.fields(By.XPATH, self.CITY_LTD, "jerusalem")
        self.fields(By.XPATH, self.STREET_LTD, "45")
        self.fields(By.XPATH, self.HOUSE_NO, "")
        self.click(By.XPATH, self.SEND_REQUEST)
        assert self.assertion(By.XPATH, self.ERROR_MSG) == 'נא למלא שדה זה'

    def test_business_name_bnnumber_invalid(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.XPATH, self.MESHEK_BUSINESS)
        self.fields(By.XPATH, self.LTD_NAME, "")
        self.fields(By.XPATH, self.LTD_LAST, "kl")
        self.fields(By.XPATH, self.LTD_BNNUMBER, "")
        self.fields(By.XPATH, self.LTD_BUSINESS_NAME, "tara")
        self.selector(By.XPATH, self.SELECTOR, "מסעדות")
        self.fields(By.XPATH, self.YOUR_PHONE, "124567896")
        self.fields(By.XPATH, self.EMAIL_LTD, "abcd@gmail.com")
        self.fields(By.XPATH, self.CITY_LTD, "jerusalem")
        self.fields(By.XPATH, self.STREET_LTD, "45")
        self.fields(By.XPATH, self.HOUSE_NO, "")
        self.click(By.XPATH, self.SEND_REQUEST)
        assert self.assertion(By.XPATH, self.ERROR_MSG) == 'נא למלא שדה זה'

    # aditional

    def test_business_invalid(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.XPATH, self.QUESTIONS)
        self.click(By.XPATH, self.EXTRA_PRODUCT)

    def test_business_upload(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.XPATH, self.QUESTIONS)
        self.click(By.XPATH, self.UPLOAD_PRO)
        self.click(By.XPATH, self.REGISTER_BTN)
        self.fields(By.XPATH, self.TELEPHONE_REGISTER, "1234567811")
        self.fields(By.XPATH, self.BN_NUMBER, "515074946")
        self.checkbox(By.XPATH, self.REMIND_ME_BOX)
        self.click(By.XPATH, self.CONNECT_REGISTER_BTN)
        self.fields(By.XPATH, self.LOGIN_CODE5, "")
        self.fields(By.XPATH, self.LOGIN_CODE4, "")
        self.fields(By.XPATH, self.LOGIN_CODE3, "")
        self.fields(By.XPATH, self.LOGIN_CODE2, "")
        self.fields(By.XPATH, self.LOGIN_CODE1, "")
        self.click(By.XPATH, self.ACCEPT_CODE_REGISTER)
        time.sleep(2)

    def test_business_upload_login(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.XPATH, self.QUESTIONS)
        self.click(By.XPATH, self.UPLOAD_PRO)
        self.fields(By.XPATH, self.PHONE_FIELD, "0591111113")
        self.checkbox(By.XPATH, self.CHECK_BOX)
        self.click(By.XPATH, self.CONNECT)
        self.fields(By.XPATH, self.FILL_FIVE, "5")
        self.fields(By.XPATH, self.FILL_FOUR, "4")
        self.fields(By.XPATH, self.FILL_THREE, "0")
        self.fields(By.XPATH, self.FILL_TWO, "8")
        self.fields(By.XPATH, self.FILL_ONE, "1")
        self.click(By.XPATH, self.AUTHENTICATION)

    def test_shippement(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.XPATH, self.HOW_TO_SEND)
        assert self.assertion(By.XPATH,
                              self.SHIPMENT_HEADER) == 'שיטת השילוח שלנו נורא פשוטה.\nמהספק או מהמחסן הלוגיסטי,\nאליך עד 72 שעות.'

    def test_shippement_color(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.XPATH, self.HOW_TO_SEND)
        self.color_check_up(By.XPATH, self.color)

