import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# Create a selenium test that does the following:
    # Go to https://staging.scrive.com/t/9221714692410699950/7348c782641060a9
    # Fill in the full name in the document.
    # Click on Next
    # There should be a confirmation modal (the one that has text "by clicking the button you will..."). 
    # Take a screenshot of this confirmation modal and try to make it only show what is actually 
    # visible in the modal (not the whole web page).
    # Sign the document
    # Verify that there is a text “Document signed” on the screen.
# Make the test runnable on both Firefox and Chrome locally.
# Make the test runnable on IE11 on Browserstack or Saucelabs (free account available for those sites).
# Document how to run the test on Linux.
# Skip the part that is too time-consuming and describe in your own language how it would be done 
# if you have more time. But completing all steps will be considered a bonus rather than describing it.
# Send the results as a compressed file via email.

def test_scrive():

    chrome_service = Service(ChromeDriverManager().install())
    chrome_driver = webdriver.Chrome(service = chrome_service)

    firefox_service = Service(executable_path=GeckoDriverManager().install())
    firefox_driver = webdriver.Firefox(service = firefox_service)

    drivers = [chrome_driver, firefox_driver]

    for driver in drivers:
        driver.get("https://staging.scrive.com/t/9221714692410699950/7348c782641060a9")
        driver.implicitly_wait(10)
        driver.maximize_window()
        name_box = driver.find_element(By.ID,"name")
        name_box.send_keys("Jessica Sadler")
        driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[4]/div[1]/a[1]/div[1]").click()
                
        time.sleep(2)

        element = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[4]")
        screenshot_name = str(driver.name) + "_element_screenshot.png"
        element.screenshot(screenshot_name)

        driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[4]/div[1]/a[1]/div").click()
        verification_message = driver.find_element(By.CSS_SELECTOR, "body > div > div > div.main > div:nth-child(2) > div.scroller > div > div.instructions.s-header-doc-signed > h1 > span")
        verification_txt = verification_message.text

        assert verification_txt == "Document signed!", "Oops."
        driver.quit()
