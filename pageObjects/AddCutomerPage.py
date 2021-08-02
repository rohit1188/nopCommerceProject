import time

from selenium.webdriver.common.by import By


class AddCustomerPage:
    def __init__(self,driver):
        self.driver = driver

    customersmenu = (By.LINK_TEXT, "Customers")
    customersItem = (By.XPATH, "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p")
    addnewtBtn =(By.CSS_SELECTOR, "a[class='btn btn-primary']")
    email = (By.ID, "Email")
    password = (By.ID, "Password")
    fname = (By.ID, "FirstName")
    lname = (By.ID, "LastName")
    gender = (By.XPATH,  "//input[@type='radio']")
    dob = (By.ID, "DateOfBirth")
    company = (By.ID, "Company")
    Cstroles = (By.XPATH, "//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div")
    adminstrators= (By.XPATH, "//li[contains(text(),'Administrators')]")
    forummoderators = (By.XPATH, "//li[contains(text(),'Forum Moderators')]")
    guests = (By.XPATH, "//li[contains(text(),'Guests')]")
    registered = (By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[1]")
    vendors = (By.XPATH, "//li[contains(text(),'Vendors')]")

    MOV = (By.ID, "VendorId")
    addcomnt = (By.ID, "AdminComment")
    savebtn = (By.NAME, "save")



    def selectCustomersMenu(self):
       return self.driver.find_element(*AddCustomerPage.customersmenu)

    def setCutomersMenuItem(self):
        return self.driver.find_element(*AddCustomerPage.customersItem)

    def ClickAddNewBtn(self):
        return self.driver.find_element(*AddCustomerPage.addnewtBtn)

    def setEmail(self,Email):
        return self.driver.find_element(*AddCustomerPage.email).send_keys(Email)

    def setPassword(self):
        return self.driver.find_element(*AddCustomerPage.password)

    def setFirstName(self):
        return self.driver.find_element(*AddCustomerPage.fname)


    def setLastName(self):
        return self.driver.find_element(*AddCustomerPage.lname)

    def setGender(self):
        return self.driver.find_elements(*AddCustomerPage.gender)

    def  setDob(self):
        return self.driver.find_element(*AddCustomerPage.dob)

    def setCompanyName(self):
        return self.driver.find_element(*AddCustomerPage.company)

    def setCustomerRoles(self,role):

        self.driver.find_element(*AddCustomerPage.Cstroles).click()
        time.sleep(3)
        if role == "Registered":
            self.value = self.driver.find_element(*AddCustomerPage.registered)
        elif role == 'Administrators':
            self.value = self.driver.find_element(*AddCustomerPage.adminstrators)
        elif role == 'Guests':
            time.sleep(3)
            self.driver.find_element(*AddCustomerPage.registered).click()
            self.value = self.driver.find_element(*AddCustomerPage.guests)
        elif role == 'Vendors':
            self.value = self.driver.find_element(*AddCustomerPage.vendors)
        else:
            self.value = self.driver.find_element(*AddCustomerPage.guests)
        time.sleep(3)
        role = self.driver.execute_script("arguments[0].click();", self.value)
        return role

    def setManagerOfVendor(self):
        return self.driver.find_element(*AddCustomerPage.MOV)

    def setAdminContent(self):
        return self.driver.find_element(*AddCustomerPage.addcomnt)

    def ClickOnSave(self):
        return self.driver.find_element(*AddCustomerPage.savebtn)

