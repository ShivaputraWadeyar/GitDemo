import time

from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Users\\shivaputra.wadeyar\\Downloads\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input[type='search'").send_keys("a")
time.sleep(4)
images = len(driver.find_elements_by_css_selector("div.product img"))
print(images)
