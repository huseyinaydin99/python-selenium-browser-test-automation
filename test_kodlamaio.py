from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

class Test_Kodlamaio:
    def test_invalid_login(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.kodlama.io/")
        sleep(2)
        loginButton = driver.find_element(By.XPATH, "//*[@id='navbar']/div/div/div/ul/li[3]/a")
        loginButton.click()
        sleep(15)

testClass = Test_Kodlamaio()
testClass.test_invalid_login()
sleep(15)