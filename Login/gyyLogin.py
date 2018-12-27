from selenium.webdriver.common.keys import Keys

class Login():
    def login(self, driver, username, password):
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys(username)
        driver.find_element_by_name("username").send_keys(Keys.TAB)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_name("password").send_keys(Keys.TAB)
        driver.find_element_by_xpath('//div[contains(text(),"登  录")]').click()

