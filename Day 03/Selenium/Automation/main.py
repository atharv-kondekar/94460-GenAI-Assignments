from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://duckduckgo.com")
time.sleep(0.5)
print("Title  : ",driver.title)

#driver.implicitly_wait(5)

search_box = driver.find_element(By.NAME , "q")

search_box.clear()
search_box.send_keys("Dkte Ichalkaranji")
time.sleep(0.5)
search_box.send_keys(Keys.RETURN)
time.sleep(5)
print("Titile : ",driver.title)

driver.quit()
