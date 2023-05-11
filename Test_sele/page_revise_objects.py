from selenium.webdriver.common.by import By

from Test_sele.Basics_revise import BasePage


class TestPages(BasePage):

    def test_home(self):
        self.setup()
        self.click(By.XPATH, self.MENS)
        self.click(By.XPATH, self.VIEW_MAN)
        self.click(By.XPATH, self.SHOES)
        self.click(By.XPATH, self.FENDI_MATCH)
        self.click(By.XPATH, self.SHOES_DEATIL)
