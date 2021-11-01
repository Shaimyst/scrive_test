from os import name
from threading import Thread
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# This array 'caps' defines the capabilities browser, device and OS combinations where the test will run
caps=[{
      'os_version': '10',
      'os': 'Windows',
      'browser': 'ie',
      'browser_version': '11.0',
      'name': 'Parallel Test1', # test name
      'build': 'browserstack-build-1' # Your tests will be organized within this build
      }]	 
#run_session function searches for 'BrowserStack' on google.com
def run_session(desired_cap):
    driver = webdriver.Remote(
        command_executor='https://jessicasadler_RbBTVv:xE8t7EaT7QqcLDMfzfvz@hub-cloud.browserstack.com/wd/hub',
        desired_capabilities=desired_cap)
    # Go to https://staging.scrive.com/t/9221714692410699950/7348c782641060a9
    driver.get("https://staging.scrive.com/t/9221714692410699950/7348c782641060a9")
    driver.implicitly_wait(10)
    driver.maximize_window()
    # Fill in the full name in the document.
    name_box = driver.find_element(By.ID,"name")
    name_box.send_keys("Jessica Sadler")
    # Click on Next
    driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[4]/div[1]/a[1]/div[1]").click()
            
    # # Take a screenshot of confirmation modal
    time.sleep(2)

    element = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[4]")
    screenshot_name = str(driver.name) + "element_screenshot.png"
    element.screenshot(screenshot_name)
    # print(dir(driver))

    # Sign the document
    driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[4]/div[1]/a[1]/div").click()
    # Verify that there is a text “Document signed” on the screen.
    verification_message = driver.find_element(By.CSS_SELECTOR, "body > div > div > div.main > div:nth-child(2) > div.scroller > div > div.instructions.s-header-doc-signed > h1 > span")
    verification_txt = verification_message.text

    assert verification_txt == "Document signed!", "Oops."
    driver.quit()
  

#The Thread function takes run_session function and each set of capability from the caps array as an argument to run each session parallelly
for cap in caps:
  Thread(target=run_session, args=(cap,)).start()