import allure
import pytest
import requests

from Locators.all_locators import Locators


class TestApi(Locators):
    @allure.description('API test for search button using post ')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search(self):
        req = requests.post(self.API_PAYMENT)
        view_source = req.json()
        status = req.status_code
        time = req.elapsed.total_seconds()
        required = req.is_permanent_redirect
        print(f"view source = {view_source}\nThe status code is = {status}\nIt takes  {time} seconds\n{required}")
        assert 200
        assert time < 10
        assert required == False

    @allure.description('API test for credit card using post ')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_files(self):
        req = requests.post(self.API_CREATE)
        view_source = req.json()
        status = req.status_code
        time = req.elapsed.total_seconds()
        required = req.is_permanent_redirect
        print(f"view source = {view_source}\nThe status code is = {status}\nIt takes  {time} seconds\n{required}")
        assert 200
        assert time < 10
        assert required == False

    @allure.description('API test for LANGUAGE using post ')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_language(self):
        req = requests.post(self.API_LANUGUAGE)
        view_source = req.json()
        status = req.status_code
        time = req.elapsed.total_seconds()
        required = req.is_permanent_redirect

        print(f"view source = {view_source}\nThe status code is = {status}\nIt takes  {time} seconds\n{required}")
        assert 200
        assert time < 10
        assert required == False

    @allure.description('API test for LANGUAGE using post ')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_(self):
        req = requests.post(self.API_ACCOUNT)
        view_source = req.json()
        status = req.status_code
        time = req.elapsed.total_seconds()
        required = req.is_permanent_redirect

        print(f"view source = {view_source}\nThe status code is = {status}\nIt takes  {time} seconds\n{required}")
        assert 504
        assert time < 10
        assert required == False

    @allure.description('API test for LANGUAGE using post ')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_(self):
        req = requests.post(self.API_APPROVE)
        view_source = req.json()
        status = req.status_code
        time = req.elapsed.total_seconds()
        required = req.is_permanent_redirect

        print(f"view source = {view_source}\nThe status code is = {status}\nIt takes  {time} seconds\n{required}")
        assert 200
        assert time < 10
        assert required == False

    @allure.description('API test for LANGUAGE using post ')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_(self):
        req = requests.post(self.API_SUMMERY)
        view_source = req.json()
        status = req.status_code
        time = req.elapsed.total_seconds()
        required = req.is_permanent_redirect

        print(f"view source = {view_source}\nThe status code is = {status}\nIt takes  {time} seconds\n{required}")
        assert 200
        assert time < 10
        assert required == False

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Check Api for payment")
    def test_api_for_payment(self):
        url = self.API_PAYMENT
        data = self.API_DATA
        res = requests.post(url, json=data)
        products = res.json()["Items"]
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
        assert products == ' '
