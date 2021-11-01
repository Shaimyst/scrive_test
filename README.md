# scrive_test
A test for Scrive

---


### Initial Setup


#### Python installs with pipenv

setup pipenv virtual-environment for project:    
```sh
pipenv install
```

spin-up virtual-environment:
```sh
pipenv shell
```

spin-down the virtual-environment:
```sh
exit
```


---

### Run Selenium test

```sh
pytest
```

### Notes to Devs
Below are some issues to solve if I had more time:

Screenshot:
To make sure the test captures a screenshot of the desired object, I put in a time.sleep(2) command. This could be problematic - replacing that with a wait command for the specific object to be loaded or visible would be ideal.

Browserstack & Sauce Labs:
I haven't used Browserstack or Sauce Labs before but this was a good introduction to them. I got further on Browserstack as it has a Quick Integration Guide. I was able to get about half way through before running out of time and having to move on.

Headless:
I could get one browser to run headless but not both at the same time. They are affecting each other, particularly the Options lines, a workaround would be to put in an if/elif statement like the solution at the bottom of this page: https://github.com/SeleniumHQ/selenium/issues/4643. However, I was told headless was optional, so I just removede it.
