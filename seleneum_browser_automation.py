from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")
input = driver.find_element(By.NAME, "q")
input.send_keys("kodlamaio")
searchButton = driver.find_element(By.NAME, "btnK")
sleep(1)
searchButton.click()
sleep(1)
first_result = driver.find_element(By.XPATH, "//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/div/a")
first_result.click()
sleep(1)
listOfCourses = driver.find_elements(By.CLASS_NAME, "course-listing")
print(f"Kodlama IO sitesinde şu anda {len(listOfCourses)} adet kurs var.")
sleep(1)
