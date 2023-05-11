
import time
import pymongo
import pytest
from pymongo import MongoClient
from selenium.webdriver.common.by import By

from Base_setups.main_setups import BaseSetups

class TestHeaderPage(BaseSetups):
    def title_logo(self):
        self.setup_trado()
        try:
            assert 'trado' in self.driver.title
            print("trado title is verified")
        except:
            print("trado title is not verified")



    def language(self):
        self.setup_trado()
        self.click(By.XPATH, self.RESTRAUNAT)
        self.click(By.XPATH, self.SAVE)
        self.click(By.XPATH, self.US_IL_LANGUAGE)

        self.setup_trado()
        self.color_check_up(By.XPATH, self.BACKGROUND_COLOR)

    def test_scroll(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.driver.execute_script("window.scrollBy(0, 100);")
        self.click(By.XPATH, self.NEXT_SLIDE)
        self.click(By.XPATH, self.BACK_SLIDE)



    def test_search_assert_price(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.fields(By.XPATH, self.SEARCH_PRODUCTS, "גורילה גלו")
        self.click(By.XPATH, self.SEARCH_BUTTON)
        self.click(By.XPATH, self.SEARCH_LIST)
        time.sleep(2)
        assert self.assertion(By.CSS_SELECTOR, self.PRICE_PRODUCT) == 'עלות לקרטון: ₪27.90'

    def test_cartoon_in_stock(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.fields(By.XPATH, self.SEARCH_PRODUCTS, "גורילה גלו")
        self.click(By.XPATH, self.SEARCH_BUTTON)
        self.click(By.XPATH, self.SEARCH_LIST)
        assert self.assertion(By.XPATH, self.CARTOON_IN_STOCK) == 'קרטונים במלאי:9976'

    @pytest.mark.parametrize("name,message",[('eggeggggg', '0 תוצאות'),
                                               ('corona', '0 תוצאות'),
                                               ('קורונה 335 מ"ל', '2 תוצאות'),
                                               ('בירה', '7 תוצאות'),
                                               ('','0 תוצאות'),
                                             ('@#$$#@', '0 תוצאות'),
                                             ('12456789', '0 תוצאות')
                                               ])
    def test_search_not_in_stock(self, name, message):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.fields(By.XPATH, self.SEARCH_PRODUCTS, name)
        self.click(By.XPATH, self.SEARCH_BUTTON)
        time.sleep(2)
        self.click(By.XPATH, self.SEARCH_LIST)
        assert self.message(By.XPATH, self.SEARCH_RESULT_MESSAGE) == message



    def  add_two_numbers(self,a,b):
        return a+b

    @pytest.mark.small
    def test_large_number(self):
        assert self.add_two_numbers(4, 5) == 9
    @pytest.mark.large
    def test_small_number(self):
        assert  self.add_two_numbers(100, 450) == 400













