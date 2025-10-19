from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

def test_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    
    try:
        driver.get("https://example.com/login")
        driver.find_element(By.ID, "username").send_keys("test_user")
        driver.find_element(By.ID, "password").send_keys("mySecurePassword")
        driver.find_element(By.ID, "loginBtn").click()
        time.sleep(3)
        message = driver.find_element(By.ID, "welcomeMsg").text
        assert "Welcome" in message
        print("✅ Login test passed!")
    finally:
        driver.quit()
