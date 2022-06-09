from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Users\\shivaputra.wadeyar\\Downloads\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes =driver.find_elements_by_xpath("//input[@type='checkbox']")

for checkbox in checkboxes:
    if checkbox.get_attribute("value") =="option2":
        checkbox.click()
        print(checkbox.is_selected())
        assert checkbox.is_selected()

radiobuttons= driver.find_elements_by_xpath("//input[@type='radio']")
radiobuttons[1].click()
assert radiobuttons[2].is_selected()

assert driver.find_element_by_id("displayed-text").is_displayed()
driver.find_element_by_id("hide-textbox").click()
assert not driver.find_element_by_id("displayed-text").is_displayed()