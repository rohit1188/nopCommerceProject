import time

import pytest

from pageObjects.AddCutomerPage import AddCustomerPage
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomerPage
from utilities.BaseClass import BaseClass


class TestSearchCustomerByName(BaseClass):
    username = "admin@yourstore.com"
    password = "admin"

    @pytest.mark.sanity
    def test_SearchCustByEmail(self):
        log = self.getLogger()
        log.info("***** test 003 ******")
        loginpage = LoginPage(self.driver)
        loginpage.setUserEmail().clear()
        log.info("Enter username:" + self.username)
        loginpage.setUserEmail().send_keys(self.username)
        loginpage.setPassword().clear()
        log.info("Enter password:" + self.password)
        loginpage.setPassword().send_keys(self.password)
        loginpage.ClickLoginBtn().click()

        log.info("***Add customer***")
        addcustomerpage = AddCustomerPage(self.driver)
        addcustomerpage.selectCustomersMenu().click()
        addcustomerpage.setCutomersMenuItem().click()

        log.info("****Search Customer****")
        searchCustpage = SearchCustomerPage(self.driver)
        searchCustpage.setFirstName().send_keys("Steve")
        searchCustpage.ClickSearchBtn().click()
        time.sleep(5)
        status = searchCustpage.SearchCustomerByName("Steve Gates")
        assert True == status


