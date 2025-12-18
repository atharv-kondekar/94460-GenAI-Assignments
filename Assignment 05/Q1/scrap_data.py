from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless")

browser = webdriver.Chrome(options=options)
wait = WebDriverWait(browser, 15)

browser.get("https://www.sunbeaminfo.com/")
browser.implicitly_wait(5)

# scroll
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

# find toggle (NOT clickable, just present)
plus_button = wait.until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='collapseSix']/preceding-sibling::a"))
)

# click using JS (bypasses Selenium click issues)
browser.execute_script("arguments[0].click();", plus_button)
time.sleep(2)

# scrape internship + batch info
items = browser.find_elements(By.XPATH, "//*[@id='collapseSix']//li")

print("Internship & Batch Info:\n")
for i in items:
    if i.text.strip():
        print(i.text)

browser.quit()
