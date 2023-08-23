# Generated by Selenium IDE
from unittest import TestCase

import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestInvalidloginwait2(TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def tearDown(self):
    self.driver.quit()
  
  def test_invalidloginwait2(self):
    self.driver.get("https://www.saucedemo.com/")
    self.driver.set_window_size(1552, 832)
    WebDriverWait(self.driver, 0.005).until(expected_conditions.visibility_of_element_located((By.ID, "user-name")))
    self.driver.find_element(By.ID, "user-name").send_keys("1")
    WebDriverWait(self.driver, 0.005).until(expected_conditions.visibility_of_element_located((By.ID, "password")))
    self.driver.find_element(By.ID, "password").send_keys("1")
    WebDriverWait(self.driver, 0.005).until(expected_conditions.visibility_of_element_located((By.ID, "login-button")))
    self.driver.find_element(By.ID, "login-button").click()
    WebDriverWait(self.driver, 0.005).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"error\"]")))
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"error\"]").text == "Epic sadface: Username and password do not match any user in this service"
  
