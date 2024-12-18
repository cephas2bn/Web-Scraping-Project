from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Correct paths
CHROME_DRIVER_PATH = r"C:\Users\cepha\Downloads\chrome-win64\chrome.exe"
CHROME_BINARY_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

options = Options()
options.binary_location = CHROME_BINARY_PATH

# Initialize ChromeDriver
service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://www.google.com")
    print("Page title:", driver.title)
finally:
    driver.quit()
