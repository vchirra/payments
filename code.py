import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Launch Chrome automatically using WebDriver Manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.google.com")
print("Page Title:", driver.title)

time.sleep(10)
driver.quit()
