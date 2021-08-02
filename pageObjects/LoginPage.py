from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class LoginPage():

    def __init__(self,driver):
        self.driver = driver

    username = (By.ID, "Email")
    password = (By.ID, "Password")
    loginBtn = (By.XPATH, "//button[@type='submit']")
    logout = (By.LINK_TEXT,"Logout")

    def setUserEmail(self):
        return self.driver.find_element(*LoginPage.username)

    def setPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def ClickLoginBtn(self):
        return self.driver.find_element(*LoginPage.loginBtn)

    def LogOutClick(self):
        return self.driver.find_element(*LoginPage.logout)


