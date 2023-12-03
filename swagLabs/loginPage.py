from selenium.webdriver.common.by import By


class testLogin:
    def __init__(self, driver):
        self.drive = driver
        self.usernameID = (By.ID, "user-name")
        self.passwordID = (By.ID, "password")
        self.isiClick = (By.ID, "login-button")
        self.sukses = (By.XPATH, "//span[@class='title']")
        self.gagal = (By.XPATH, "//h3[@data-test='error']")
    def masukanUsername(self,userName):
        self.drive.find_element(*self.usernameID).send_keys(userName)
    def masukanPassword(self,passWord):
        self.drive.find_element(*self.passwordID).send_keys(passWord)
    def button(self):
        self.drive.find_element(*self.isiClick).click()
    def infoSukses(self):
        return self.drive.find_element(*self.sukses)
    def infGagal(self):
        return self.drive.find_element(*self.gagal)
