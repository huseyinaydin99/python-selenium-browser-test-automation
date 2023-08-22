from selenium import webdriver
from time import sleep
from unittest import TestCase
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# prefix => ön ek test_
# postfix => son ek demo
# test_demo
class Test_Demo:
    # her testten önce çağrılır
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com")
    #her testten sonra çağrılır
    def teardown_method(self):
        self.driver.quit()
    def test_test_demo_func(self):
        text = "Hello"
        assert text == "Hello"
    def test_merhaba(self):
        assert True
    def test_invalid_login(self):
        assert True

