import allure
import pytest

from All_pages.header_page import TestHeaderPage
from All_pages.mongodb import TestMongoVsWebsite
from All_pages.payment import TestPayments
from All_pages.register import TestRegister


class TestFinal(TestPayments, TestHeaderPage, TestMongoVsWebsite, TestRegister):

    def final_object(self):
        final = TestFinal()
        return final

    @allure.description('verify the logo is displayed on website')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_title_logo(self):
        self.final_object().title_logo()

    @allure.description('verify the language icons is displayed on website and can change')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_language(self):
        self.final_object().language()

    @allure.description('able to make successful payment with valid credit card')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_valid_payment_credit_card(self):
        self.final_object().valid_payment_credit_card()

    @allure.description('able to make successful payment with invalid credit card')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_credit_card_without(self):
        self.final_object().invalid_credit_card()

    @allure.description('able to make successful payment with b2b system')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_b2b_payment(self):
        self.final_object().b2b_payment()

    @allure.description('able to make successful payment with valid digital_check')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_valid_payment_digital_check(self):
        self.final_object().valid_payment_digital_check()

    @allure.description('able to make successful payment with valid digital_check with flowing30')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_valid_payment_digital_check_with_flowing30(self):
        self.final_object().valid_payment_digital_check_with_flowing30()

    @allure.description('able to make successful payment with valid fintrado')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_valid_payment_FinTrado(self):
        self.final_object().valid_payment_FinTrado()

    @allure.description('without accepting policy able to pay with fitrado')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_valid_payment_FinTrado_without_accepting_1policy(self):
        self.final_object().valid_payment_FinTrado_without_accepting_1policy()

    @allure.description('without accepting policy able to pay with fitrado')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_valid_payment_FinTrado_without_accepting_2policy(self):
        self.final_object().valid_payment_FinTrado_without_accepting_2policy()

    @allure.description('able to make successful payment with invalid b2b system')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_customer_id_b2b_payment(self):
        self.final_object().invalid_customer_id_b2b_payment()

    @allure.description('able to make successful payment with invalid digital check')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_payment_digital_check(self):
        self.final_object().invalid_payment_digital_check()

    @allure.description('able to make successful payment with digital chekc flowing 60')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_valid_payment_digital_check_with_flowing60(self):
        self.final_object().valid_payment_digital_check_with_flowing60()

    @allure.description('able to make successful payment with digital check flowing 90')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_valid_payment_digital_check_with_flowing90(self):
        self.final_object().valid_payment_digital_check_with_flowing90()

    @allure.description('able to make successful payment with valid bank transfer')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_valid_payment_bank_transfer(self):
        self.final_object().valid_payment_bank_transfer()

    @allure.description('able to make successful payment with invalid bank transfer')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_account_no_payment_bank_transfer(self):
        self.final_object().invalid_account_no_payment_bank_transfer()

    @allure.description('able to make successful payment with invalid bank transfer without baranch number')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_branch_no_payment_bank_transfer(self):
        self.final_object().invalid_branch_no_payment_bank_transfer()

    @allure.description('able to make successful payment with invalid invoice business name')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_invoice_Business_name(self):
        self.final_object().invalid_invoice_Business_name()

    @allure.description('able to make successful payment with invalid invoice bnnumber')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_invoice_BNnumber(self):
        self.final_object().invalid_invoice_BNnumber()

    @allure.description('able to make successful payment with invalid invoice email')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)

    def test_invalid_invoice_email(self):
        self.final_object().invalid_invoice_email()

    @allure.description('able to make successful payment with invalid invoice city')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_invoice_CITY(self):
        self.final_object().test_invalid_invoice_CITY()

    @allure.description('able to make successful payment with invalid invoice street number')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_invoice_STREEETNO(self):
        self.final_object().invalid_invoice_STREEETNO()

    @allure.description('able to make successful payment with invalid invoice house number')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_invoice_HOUSENO(self):
        self.final_object().invalid_invoice_HOUSENO()

    @allure.description('able to make successful payment with invalid invoice entrance')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_invoice_ENTRANCE(self):
        self.final_object().invalid_invoice_ENTRANCE()

    @allure.description('able to make successful payment with invalid invoice floor number')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_invoice_FLOORNO(self):
        self.final_object().invalid_invoice_FLOORNO()

    @allure.description('able to make successful payment with invalid invoice delivery city')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_invoice_TOWN(self):
        self.final_object().invalid_invoice_TOWN()

    @allure.description('able to make successful payment with invalid invoice street delivery')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_invoice_STREET_DELIVERY(self):
        self.final_object().invalid_invoice_STREET_DELIVERY()

    @allure.description('able to make successful payment with invalid delivery house number')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_invoice_DELIVERY_HOUSENO(self):
        self.final_object().invalid_invoice_DELIVERY_HOUSENO()

    @allure.description('able to make successful payment with invalid delivery entrance number')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_invoice_ENTRANCE_DELIVERY(self):
        self.final_object().invalid_invoice_ENTRANCE_DELIVERY()

    @allure.description('able to make successful payment with invalid delivery entrance number')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_invoice_FLOOR(self):
        self.final_object().invalid_delivery_FLOOR()

    @allure.description('able to make successful payment with invalid delivery first nanme')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_invoice_FIRSTNAME(self):
        self.final_object().invalid_delivery_FIRSTNAME()

    @allure.description('able to make successful payment with invalid delivery last nanme')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_invoice_LASTNAME(self):
        self.final_object().invalid_delivery_LASTNAME()

    @allure.description('able to make successful payment with invalid delivery contact address')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_invoice_CONTACT_DELIVERY(self):
        self.final_object().invalid_CONTACT_DELIVERY()

    @allure.description('able to make successful payment with invalid delivery phone no')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_invoice_PHONENO(self):
        self.final_object().invalid__PHONENO()

    @allure.description('able to make delete order product from cart item')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_product(self):
        self.final_object().delete_product()

    @allure.description('able to make minus order product from cart item')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_minus_specific_product(self):
        self.final_object().minus_specific_product()

    @allure.description('able to make delete specific order product from cart item')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_specific_product(self):
        self.final_object().delete_specific_product()

    @allure.description('verify all product is properly ordered in price from cart item')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_total_price_negative(self):
        self.final_object().total_price_negative()

    @allure.description('able to make up and down the scroll of the page ')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def total_price_assertion(self):
        self.final_object().up_down_scroll()

    @allure.description('verify the trado brand logo the payment method of the page')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_valid_trado_logo(self):
        self.final_object().valid_trado_logo()

    @allure.description('able to make back from the page and buy again')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_valid_back_to_page(self):
        self.final_object().valid_back_to_page()

    @allure.description('able to make back to the home page in order to buy products')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_valid_back_to_page_shopping(self):
        self.final_object().valid_back_to_page_shopping()

    # MongoVsSearch
    @allure.description('able to verify the product name in mongo data base mathes with website displayed in gui')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_product_name_in_data_matches_with_gui_display(self):
        self.final_object().product_name_in_data_matches_with_gui_display()

    @allure.description('Verify the product price is equal to tin the data')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_product_price(self):
        self.final_object().product_price()

    @allure.description(
        'able to verify the product in the stock in mongo data base mathes with website displayed in gui')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_product_inStock(self):
        self.final_object().product_inStock()

    @allure.description('able to verify the product in stock in mongo data base mathes with website displayed in gui')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_product_price_inStock(self):
        self.final_object().product_price_inStock()

    @allure.description('able to verify the user name in mongo data base mathes with website displayed in gui')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_users_name_(self):
        self.final_object().users_name_()

    @allure.description('able to verify the product category in mongo data base mathes with website displayed in gui')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_product_category(self):
        self.final_object().product_category()

    @allure.description('able to verify the order status from admin dash board name in mongo data base mathes properly')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_orders_status(self):
        self.final_object().orders_status()

    @allure.description('able to verify the product name in mongo data base mathes with website displayed in gui')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_orders_payment_type(self):
        self.final_object().orders_payment_type()

    @allure.description('able to verify the login operation is worked properly')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_login(self):
        self.final_object().login()

    @allure.description('able to verify register except accepting the policy')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_without_checkbox(self):
        self.final_object().without_checkbox()

    @allure.description('able to verify register with twit and check twit is clickable')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_without_checkbox_assign(self):
        self.final_object().without_checkbox_assign()

    @allure.description('able to verify register with google and check twit is clickable')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_register_with_google(self):
        self.final_object().register_with_google()

    @allure.description('able to verify register with twit and check facebook is clickable')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_register_with_fb(self):
        self.final_object().register_with_fb()

    @allure.description('able to verify register with twit and check twit is clickable')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_register_with_twitt(self):
        self.final_object().register_with_twitt()
