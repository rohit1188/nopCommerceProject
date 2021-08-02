from selenium.webdriver.common.by import By


class SearchCustomerPage:
    def __init__(self,driver):
        self.driver = driver

    email = (By.ID, "SearchEmail")
    fname = (By.ID, "SearchFirstName")
    lname = (By.ID, "SearchLastName")
    searchBtn = (By.ID, "search-customers")

    tblsearchresult = (By.XPATH, "//table[@role='grid']")
    tablexpath = (By.XPATH, "//table[@id='customers-grid']")
    rows = (By.XPATH, "//*[@id='customers-grid']/tbody/tr")
    cols = (By.XPATH, "//*[@id='customers-grid']/thead/tr/th/div")

    def setEmail(self):
        return self.driver.find_element(*SearchCustomerPage.email)

    def setFirstName(self):
        return self.driver.find_element(*SearchCustomerPage.fname)

    def setLastName(self):
        return self.driver.find_element(*SearchCustomerPage.lname)

    def ClickSearchBtn(self):
        return self.driver.find_element(*SearchCustomerPage.searchBtn)
    
    def getRows(self):
        return len(self.driver.find_elements(*SearchCustomerPage.rows))

    def SearchCustomerByEmail(self,email):
        flag = False
        for r in range(1,self.getRows()+1):
            table = self.driver.find_element(*SearchCustomerPage.tablexpath)
            emailid = table.find_element_by_xpath("//*[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def SearchCustomerByName(self,Name):
        flag = False
        for r in range(1,self.getRows()+1):
            table = self.driver.find_element(*SearchCustomerPage.tablexpath)
            name = table.find_element_by_xpath("//*[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag

