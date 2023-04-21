<!--- Heading --->
<div align="center">
  <h1>ak_selenium</h1>
  <p>
    Selenium package with requests integration and anti-bot detection measures
  </p>
<h4>
    <a href="https://github.com/rpakishore/ak_selenium/">View Demo</a>
  <span> · </span>
    <a href="https://github.com/rpakishore/ak_selenium">Documentation</a>
  <span> · </span>
    <a href="https://github.com/rpakishore/ak_selenium/issues/">Report Bug</a>
  <span> · </span>
    <a href="https://github.com/rpakishore/ak_selenium/issues/">Request Feature</a>
  </h4>
</div>
<br />

![GitHub commit activity](https://img.shields.io/github/commit-activity/m/rpakishore/ak_selenium)
![GitHub last commit](https://img.shields.io/github/last-commit/rpakishore/ak_selenium)
<!-- Table of Contents -->
<h2>Table of Contents</h2>

- [1. About the Project](#1-about-the-project)
  - [1.1. Features](#11-features)
- [2. Getting Started](#2-getting-started)
  - [2.1. Installation](#21-installation)
- [3. Usage](#3-usage)
- [4. Roadmap](#4-roadmap)
- [5. License](#5-license)
- [6. Contact](#6-contact)
- [7. Acknowledgements](#7-acknowledgements)

<!-- About the Project -->
## 1. About the Project

<!-- Features -->
### 1.1. Features

- launch Selenium with custom options
- Add anti-bot detection measures
- Pass selenium headers/cookies to requests library

<!-- Getting Started -->
## 2. Getting Started

<!-- Installation -->
### 2.1. Installation

Install my-project with flit

```bash
git clone https://github.com/rpakishore/ak_selenium.git
cd ak_selenium
pip install flit
flit install
```

Alternatively, you can use pip

```bash
pip install ak_selenium
```

<!-- Usage -->
## 3. Usage

```python
from ak_selenium import Chrome
chrome = Chrome(
    headless=False, 
    Chrome_userdata_path=r"Path\to\User Data",
    half_screen=True,
)

#Get Chromedriver
driver = chrome.init_chrome()

#Get the website
driver.get("https://example.com")

By, Keys = chrome.get_By_and_Keys()

#Wait for elements to load
locator = (By.TAG_NAME, "h1")
chrome.Wait_for_locator(locator)

#Get Requests Session
s = chrome.update_req_headers_cookies()
s.get('https://www.iana.org/domains/reserved')
```

<!-- Roadmap -->
## 4. Roadmap

- [ ]

<!-- License -->
## 5. License

See LICENSE.txt for more information.

<!-- Contact -->
## 6. Contact

Arun Kishore - [@rpakishore](mailto:rpakishore@gmail.com)

Project Link: [https://github.com/rpakishore/](https://github.com/rpakishore/ak_selenium)

<!-- Acknowledgments -->
## 7. Acknowledgements

Use this section to mention useful resources and libraries that you have used in your projects.

- [Awesome README Template](https://github.com/Louis3797/awesome-readme-template/blob/main/README-WITHOUT-EMOJI.md)
- [Banner Maker](https://banner.godori.dev/)
- [Shields.io](https://shields.io/)
- [Carbon](https://carbon.now.sh/)