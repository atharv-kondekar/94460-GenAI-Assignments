from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


driver.get("https://duckduckgo.com/")
time.sleep(2)

search_box=driver.find_element(By.NAME,"q")

for ch in "DKTE College Ichalkaranji":
    search_box.send_keys(ch)
    time.sleep(0.5)

search_box.send_keys(Keys.RETURN)

time.sleep(2)
print("Tilte : ",driver.title)

driver.quit()