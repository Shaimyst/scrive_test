import time

# Create a selenium test that does the following:
    # Go to https://staging.scrive.com/t/9221714692410699950/7348c782641060a9
    # Fill in the full name in the document.
    # Click on Next
    # There should be a confirmation modal (the one that has text "by clicking the button you will..."). Take a screenshot of this confirmation modal and try to make it only show what is actually visible in the modal (not the whole web page).
    # Sign the document
    # Verify that there is a text “Document signed” on the screen.
# Make the test runnable on both Firefox and Chrome locally.
# Make the test runnable on IE11 on Browserstack or Saucelabs (free account available for those sites).
# Document how to run the test on Linux.
# Skip the part that is too time-consuming and describe in your own language how it would be done if you have more time. But completing all steps will be considered a bonus rather than describing it.
# Send the results as a compressed file via email.

def test_scrive(chrome_driver):
    chrome_driver.get("https://staging.scrive.com/t/9221714692410699950/7348c782641060a9")
    time.sleep(5)