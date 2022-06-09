from selenium import webdriver

driver = webdriver.Ie(executable_path="C:\\Users\\shivaputra.wadeyar\\Downloads\\IEDriverServer.exe")

driver.get("https://rahulshettyacademy.com/")
print(driver.title)
print(driver.current_url)
driver.close()