from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Users\\shivaputra.wadeyar\\Downloads\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
name = "Shivay"
driver.find_element_by_css_selector("#name").send_keys(name)
driver.find_element_by_css_selector("#alertbtn").click()
alert=driver.switch_to.alert
print(alert.text)
assert name in alert.text
alert.accept()

driver.find_element_by_css_selector("#confirmbtn").click()
alert=driver.switch_to.alert
print(alert.text)
alert.dismiss()


