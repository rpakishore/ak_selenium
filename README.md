<!--- Heading --->
<div align="center">
  <h1>ak_selenium</h1>
  <p>
    Selenium package with requests integration and anti-bot detection measures
  </p>
<h4>
    <a href="https://rpakishore.github.io/ak_selenium/">Documentation</a>
  <span> · </span>
    <a href="https://github.com/rpakishore/ak_selenium/issues/">Report Bug</a>
  <span> · </span>
    <a href="https://github.com/rpakishore/ak_selenium/issues/">Request Feature</a>
  </h4>
</div>
<br />

![GitHub commit activity](https://img.shields.io/github/commit-activity/m/rpakishore/ak_selenium)
![GitHub last commit](https://img.shields.io/github/last-commit/rpakishore/ak_selenium)
[![tests](https://github.com/rpakishore/ak_selenium/actions/workflows/test.yml/badge.svg)](https://github.com/rpakishore/ak_selenium/actions/workflows/test.yml)

<!-- Table of Contents -->
<h2>Table of Contents</h2>

- [1. About the Project](#1-about-the-project)
  - [1.1. Features](#11-features)
  - [2. Installation](#2-installation)
- [3. Usage](#3-usage)
  - [3.1. Additional Options](#31-additional-options)
- [4. Roadmap](#4-roadmap)
- [5. License](#5-license)
- [6. Contact](#6-contact)

<!-- About the Project -->
## 1. About the Project

`ak_selenium` is a Python package that provides an interface for automating browser tasks using Selenium. It comes with built-in functionalities for handling common tasks such as form filling, scrolling, and waiting for elements to load. Additionally, it has a built-in requests session that handles retries and timeouts, making it easier to send HTTP requests.

<!-- Features -->
### 1.1. Features

- Chrome browser automation using Selenium WebDriver.
- Built-in methods for form filling, scrolling, and waiting for elements.
- Anti-bot detection measures
- Pass selenium headers/cookies to requests library
- Built-in requests session with retries and timeouts.
- Ability to use Chrome user data for browser automation.
- RAM optimization for browser options.
- Integrates [Helium](https://github.com/mherrmann/helium) for easier automation


<!-- Installation -->
### 2. Installation

use pip

```bash
pip install ak_selenium@git+https://github.com/rpakishore/ak_selenium
```
<!-- Usage -->
## 3. Usage

```python
from ak_selenium import Chrome, By, Keys

chrome = Chrome(headless=True)                  # Create a new Chrome browser instance
driver = chrome.driver                          #Get Chromedriver
chrome.get("https://example.com")               # Navigate to a webpage

#Wait for element to load
locator = (By.TAG_NAME, "h1")
chrome.wait_for_locator(locator)

s = chrome.session                              # Pass selenium session to requests
s.get("https://www.iana.org/domains/reserved")  # Get a website

# Get a list of websites
## Will randomize requests to not trigger bot detection
s.bulk_get(["https://www.iana.org/domains/reserved", "https://www.example.com"])

```

Integrated with [Helium](https://github.com/mherrmann/helium) to make it easier to set up automation.

Helium methods and functions can be used as intended in the [original documentation](https://github.com/mherrmann/helium/blob/master/README.md)

Example:

```python
import helium
helium.wait_until(helium.Button('Download').exists)
```

Alternatively, helium methods and classes have been collected into two classes `Element` and `Action` for convinience

`Element` exposes the following classes: `Alert`, `Button`, `CheckBox`, `ComboBox`, `Image`, `Link`, `ListItem`, `RadioButton`, `Text`, `TextField` and the method `find_all`

`Action` exposes the following methods: `highlight`, `wait_until`, `refresh`, `attach_file`, `drag_file`, `combobox_select`, `hover`, `write`.
`Action` also incorporates a `Mouse` sub-class that collect mouse-related methods.

Example:

```python
from ak_selenium import Element, Action, Keys
import helium

chrome.get('https://google.com')                      #Go to website
Action.write('helium selenium github')                #Enter text into text field
helium.press(Keys.ENTER)                              #Press Enter
Action.Mouse.click('mherrmann/helium')                #Click
chrome.get('https://github.com/login')                #Goto github
Action.write('username', into='Username')             #Enter Username into Username field
Action.write('password', into='Password')             #Enter Password into Password field
Action.Mouse.click('Sign in')                         #Click Sign-in
Action.Mouse.scroll(direction='down', num_pixels=100) #Scroll down 100px
helium.kill_browser()                                 #Close the browser
```

### 3.1. Additional Options

```python
# Selenium Overrides
## Overide default useragent
chrome.USERAGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                    AppleWebKit/537.36 (KHTML, like Gecko) \
                    Chrome/83.0.4103.53 Safari/537.36'

## Override implicit and max wait times for selenium
chrome.IMPLICITLY_WAIT_TIME = 3 #seconds
chrome.MAX_WAIT_TIME = 5 #seconds

# Requests.Session Override
s.MIN_REQUEST_GAP = 0.9 #seconds between requests
```

<!-- Roadmap -->
## 4. Roadmap

- [ ] Add beautifulsoup integration
- [ ] Proxy

<!-- License -->
## 5. License

See LICENSE for more information.

<!-- Contact -->
## 6. Contact

Arun Kishore - [@rpakishore](mailto:pypi@rpakishore.co.in)

Project Link: [https://github.com/rpakishore/ak_selenium](https://github.com/rpakishore/ak_selenium)