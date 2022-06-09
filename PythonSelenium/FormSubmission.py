from selenium import webdriver

from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path="C:\\Users\\shivaputra.wadeyar\\Downloads\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_css_selector("[name='name']").send_keys("Shivu")
driver.find_element_by_css_selector("[name='email']").send_keys("Shivu.wadeyar@gmail.com")
sel= Select(driver.find_element_by_id("exampleFormControlSelect1"))
sel.select_by_visible_text("Male")
driver.find_element_by_css_selector("[type='submit']").click()
alertText = driver.find_element_by_css_selector("[class='alert alert-success alert-dismissible']").text

assert ("Success" in alertText)