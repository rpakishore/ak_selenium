"""

# Project Layout

```mermaid
graph TB
    subgraph User["Application Layer"]
        UserCode["User Code"]
    end

    subgraph Auto["Browser Automation Layer"]
        BaseBrowser["Base Browser Class"]
        Chrome["Chrome Implementation"]
        Firefox["Firefox Implementation"]
        HeliumInt["Helium Integration"]
    end

    subgraph Req["Request Integration Layer"]
        SessionMgmt["Session Management"]
        AntiBot["Anti-bot Features"]
        HeaderTransfer["Header/Cookie Transfer"]
    end

    subgraph Ext["External Dependencies"]
        Selenium["Selenium WebDriver"]
        Helium["Helium"]
        Requests["Requests Library"]
    end

    subgraph Test["Testing Layer"]
        BrowserTests["Browser Tests"]
        RequestTests["Request Tests"]
    end

    %% Relationships
    UserCode --> BaseBrowser
    UserCode --> SessionMgmt
    
    BaseBrowser --> Chrome
    BaseBrowser --> Firefox
    BaseBrowser --> HeliumInt
    
    Chrome --> Selenium
    Firefox --> Selenium
    HeliumInt --> Helium
    
    SessionMgmt --> Requests
    SessionMgmt --> AntiBot
    SessionMgmt --> HeaderTransfer
    
    BrowserTests --> BaseBrowser
    RequestTests --> SessionMgmt

    %% Click Events
    click BaseBrowser "https://github.com/rpakishore/ak_selenium/blob/main/src/ak_selenium/browser.py"
    click Chrome "https://github.com/rpakishore/ak_selenium/blob/main/src/ak_selenium/chrome.py"
    click Firefox "https://github.com/rpakishore/ak_selenium/blob/main/src/ak_selenium/firefox.py"
    click HeliumInt "https://github.com/rpakishore/ak_selenium/blob/main/src/ak_selenium/helium_attribs.py"
    click SessionMgmt "https://github.com/rpakishore/ak_selenium/blob/main/src/ak_selenium/browser.py"
    click RequestTests "https://github.com/rpakishore/ak_selenium/blob/main/src/tests/test_requests.py"
    click BrowserTests "https://github.com/rpakishore/ak_selenium/blob/main/src/tests/test_browser.py"

    %% Styling
    classDef default fill:#f9f9f9,stroke:#333,stroke-width:2px
    classDef browser fill:#dae8fc,stroke:#6c8ebf
    classDef request fill:#d5e8d4,stroke:#82b366
    classDef external fill:#fff2cc,stroke:#d6b656
    classDef test fill:#e1d5e7,stroke:#9673a6
    
    class BaseBrowser,Chrome,Firefox,HeliumInt browser
    class SessionMgmt,AntiBot,HeaderTransfer request
    class Selenium,Helium,Requests external
    class BrowserTests,RequestTests test

    %% Legend
    subgraph Legend
        Browser["Browser Components"]:::browser
        RequestComp["Request Components"]:::request
        Ext["External Dependencies"]:::external
        TestComp["Test Components"]:::test
    end
    ```
    
.. include:: ../../README.md

"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from ak_selenium.browser import RequestsSession
from ak_selenium.chrome import Chrome
from ak_selenium.firefox import Firefox
from ak_selenium.helium_attribs import Action, Element
