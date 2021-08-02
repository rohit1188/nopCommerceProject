import pytest

from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass


class TestLoginPage(BaseClass):
    username = "admin@yourstore.com"
    password = "admin"

    @pytest.mark.sanity
    def test_login(self):
        log = self.getLogger()
        log.info("******test 01******")
        loginpage = LoginPage(self.driver)
        loginpage.setUserEmail().clear()
        log.info("Enter username:"+self.username)
        loginpage.setUserEmail().send_keys(self.username)
        loginpage.setPassword().clear()
        log.info("Enter password:"+self.password)
        loginpage.setPassword().send_keys(self.password)
        loginpage.ClickLoginBtn().click()
        loginpage.LogOutClick().click()



