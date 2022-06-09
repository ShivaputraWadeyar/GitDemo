import time

from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Users\\shivaputra.wadeyar\\Downloads\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5)
driver.find_element_by_css_selector("input[type='search']").send_keys("ber")
time.sleep(4)
count =len(driver.find_elements_by_xpath("//div[@class='products']/div"))
print(count)
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for button in buttons:
    button.click()

driver.find_element_by_css_selector("a.cart-icon").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element_by_css_selector("input.promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector("button.promoBtn").click()
print(driver.find_element_by_css_selector("span.promoInfo").text)
message = driver.find_element_by_css_selector("span.promoInfo").text
message1 = "Code applied ..!"
assert message1 == message
