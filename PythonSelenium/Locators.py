from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Users\\shivaputra.wadeyar\\Downloads\\chromedriver.exe")

driver.get("https://login.salesforce.com/?locale=us")
#driver.find_element_by_id("username").send_keys("shivu")
driver.find_element_by_css_selector("input[type='email']").send_keys("Putra")
driver.find_element_by_xpath("//input[@type='password']").send_keys("Password Roy")
driver.find_element_by_css_selector("#Login").click()
print(driver.find_element_by_css_selector("#error").text)