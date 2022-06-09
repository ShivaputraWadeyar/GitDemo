from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Users\\shivaputra.wadeyar\\Downloads\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/frames")
driver.find_element_by_link_text("iFrame").click()

driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("I am in iframe")
driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)