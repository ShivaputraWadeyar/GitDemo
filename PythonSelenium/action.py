from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:\\Users\\shivaputra.wadeyar\\Downloads\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element_by_id("mousehover").click()
action = ActionChains(driver)

action.move_to_element(driver.find_element_by_link_text("Reload")).click().perform()
action.move_to_element(driver.find_element_by_id("displayed-text")).perform()

