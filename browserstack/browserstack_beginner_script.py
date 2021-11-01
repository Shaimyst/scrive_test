import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common import by
import webdriver_manager
from selenium.webdriver.common.by import By
from webdriver_manager.manager import DriverManager

# Other imports and desired_cap definition goes here
desired_cap = {
 "browserstack.local" : "true"
}
username = os.environ['BROWSERSTACK_USERNAME'];
accessKey = os.environ['BROWSERSTACK_ACCESS_KEY'];

# Rest of the test case goes here
def test_scrive():

    driver = webdriver.Remote(
    command_executor='https://'+username+':'+accessKey+'@hub-cloud.browserstack.com/wd/hub',
    desired_capabilities=desired_cap
    )

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