from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

class Test_Sauce:
    def test_invalid_login(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        usernameInput.send_keys("1")
        passwordInput.send_keys("1")
        loginButton = driver.find_element(By.XPATH, "//*[@id='login-button']")
        loginButton.click()
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        print(errorMessage)
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"Test sonucu: {testResult}")
        sleep(2)

testClass = Test_Sauce()
testClass.test_invalid_login()
sleep(15)