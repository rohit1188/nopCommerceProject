import random
import string
import time

import pytest

from pageObjects.AddCutomerPage import AddCustomerPage
from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass



class TestAddCustomer(BaseClass):
    username = "admin@yourstore.com"
    password = "admin"

    @pytest.mark.regression
    def test_AddCutomers(self):
        log = self.getLogger()
        log.info("******test 02******")
        loginpage = LoginPage(self.driver)
        loginpage.setUserEmail().clear()
        log.info("Enter username:" + self.username)
        loginpage.setUserEmail().send_keys(self.username)
        loginpage.setPassword().clear()
        log.info("Enter password:" + self.password)
        loginpage.setPassword().send_keys(self.password)
        loginpage.ClickLoginBtn().click()

        addcustomerpage = AddCustomerPage(self.driver)
        addcustomerpage.selectCustomersMenu().click()
        addcustomerpage.setCutomersMenuItem().click()
        addcustomerpage.ClickAddNewBtn().click()
        Email = random_generator() + "@gmail.com"
        addcustomerpage.setEmail(Email)
        addcustomerpage.setPassword().send_keys("1234")
        addcustomerpage.setFirstName().send_keys("alan")
        addcustomerpage.setLastName().send_keys("smith")
        radios = addcustomerpage.setGender()
        radios[0].click()
        addcustomerpage.setDob().send_keys("03/10/1988")
        addcustomerpage.setCompanyName().send_keys("softech")
        addcustomerpage.setCustomerRoles("Administrators")
        self.SelectOptionByText(addcustomerpage.setManagerOfVendor(), "Vendor 1")
        addcustomerpage.setAdminContent().send_keys("this is for testing")
        addcustomerpage.ClickOnSave().click()


def random_generator(size=8,chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

