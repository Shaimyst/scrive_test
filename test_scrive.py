import time
import pytest
from selenium import webdriver
from selenium.webdriver.common import by
from webdriver_manager.chrome import ChromeDriverManager
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

@pytest.fixture(scope="session")
def chrome_driver():
   s=Service(ChromeDriverManager().install())
   driver = webdriver.Chrome(service=s)
   yield driver
   driver.quit()

def test_scrive(chrome_driver):
    # Go to https://staging.scrive.com/t/9221714692410699950/7348c782641060a9
    chrome_driver.get("https://staging.scrive.com/t/9221714692410699950/7348c782641060a9")
    chrome_driver.implicitly_wait(10)
    chrome_driver.maximize_window()
    # Fill in the full name in the document.
    name_box = chrome_driver.find_element(By.ID,"name")
    name_box.send_keys("Jessica Sadler")
    # Click on Next
    chrome_driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[4]/div[1]/a[1]/div[1]").click()
    # Take a screenshot of confirmation modal
    time.sleep(2)
    chrome_driver.save_screenshot("screenshot.png")
    # Sign the document
    chrome_driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[4]/div[1]/a[1]/div").click()
    # Verify that there is a text “Document signed” on the screen.
    verification_message = chrome_driver.find_element(By.CSS_SELECTOR, "body > div > div > div.main > div:nth-child(2) > div.scroller > div > div.instructions.s-header-doc-signed > h1 > span")
    print("verification text: ")
    print(verification_message.text)
    verification_txt = verification_message.text

    assert verification_txt == "Document signed!", "Oops."

    