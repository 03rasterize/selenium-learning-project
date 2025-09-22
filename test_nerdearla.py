from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

#------ Suppress all unnecessary logs
os.environ['WDM_LOG_LEVEL'] = '0'  # I turn off webdriver-manager logs for quick readability purposes.

chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--log-level=3')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')

print("Testing Agenda button navigation...")

#------- Setup browser
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)
print('Opening uo the browser...')

#------- Go to website
driver.get("https://nerdear.la/")
driver.maximize_window()
time.sleep(2)

try:
    agenda_button = driver.find_element(By.LINK_TEXT, "Agenda") # Focused on finding a TEXT match on a LINK
    print("Agenda button found!")
    agenda_button.click()
    time.sleep(3)
    
    current_url = driver.current_url
    
    if "agenda" in driver.current_url.lower():
        print("✅ Success! Navigated to Agenda page")
        print(f'Redirected to: {current_url}')
    else:
        print("❌ Failed navigation")

except:
    print("❌ Agenda button not found")

driver.quit()
print("Test completed!")