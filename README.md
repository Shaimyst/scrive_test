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
Below are some issues I would solve if I had more time:

Headless
I could get one browser to run headless but not both at the same time. They are affecting each other, particularly the Options lines, a workaround would be to put in an if/elif statement like the solution at the bottom of this page: https://github.com/SeleniumHQ/selenium/issues/4643

