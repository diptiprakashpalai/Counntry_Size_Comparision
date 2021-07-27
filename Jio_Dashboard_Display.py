import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path ="D:\Softwares\Python\ChromeDriver\Chrome_89\chromedriver_win32\chromedriver")
driver.get("http://52.66.109.243:8080/login")
time.sleep(5)

elem = driver.find_element_by_id("username-input")
elem1 = driver.find_element_by_id("password-input")
elem.send_keys("jiochamrajpet@helixsense.com")
elem1.send_keys("jiocpet@2020")
elem1.submit()