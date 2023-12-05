from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import logging
import os
from pathlib import Path
import sys

from ak_selenium.browser import Browser, latest_useragent

#Disable webdriver-manager logs per https://github.com/SergeyPirogov/webdriver_manager#wdm_log
os.environ['WDM_LOG'] = str(logging.NOTSET)

class Chrome(Browser):
    USERAGENT: str = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'

    def __init__(self, headless:bool = False, 
        chrome_userdata_path:str|None=None, half_screen:bool=True) -> None:
        
        _useragent: str = latest_useragent('Chrome')
        if _useragent != '':
            self.USERAGENT = _useragent
        
        self.headless = headless
        self._set_userdata_path(datapath=chrome_userdata_path)
        self.half_screen = half_screen
        
        self.driver = self._driver()
        super().__init__(driver=self.driver)
        return None
    
    def _set_userdata_path(self, datapath: str | None) -> str | None:
        self.chrome_userdata_path: str | None = None
        
        if not datapath and sys.platform=="win32":
            _chrome_userdata_path: Path = Path.home() / 'AppData' / 'Local' / 'Google' / 'Chrome' / 'User Data'
            if not _chrome_userdata_path.exists():
                self.chrome_userdata_path = None
            else:
                self.chrome_userdata_path = str(_chrome_userdata_path)
        
        return self.chrome_userdata_path
    
    def __str__(self) -> str:
        return f"""
        Chrome.Object
        UserAgent:{self.USERAGENT}
        Implicit Wait Time: {self.IMPLICITLY_WAIT_TIME:.2f}s
        Max Wait Time: {self.MAX_WAIT_TIME:.2f}s
        Headless: {self.headless}
        Chrome Userdata Path: {self.chrome_userdata_path}
        Half Screen View: {self.half_screen}
        """
    
    def __repr__(self) -> str:
        return f"Chrome(headless={self.headless},\
                chrome_userdata_path={self.chrome_userdata_path},\
                half_screen={self.half_screen})"
    
    def __del__(self) -> None:
        if self.driver:
            self.driver.quit()
        return None
    
    def _driver(self) -> webdriver.Chrome:
        """
        Initializes a Chrome web driver with specific options and configurations.
        
        Returns:
            webdriver.Chrome: The initialized Chrome driver object.
        """
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-gpu')
        if self.headless:
            options.add_argument('--headless')
            options.add_argument("--window-size=1920,1080")
        options.add_argument("start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        if self.chrome_userdata_path:
            options.add_argument('--user-data-dir=' + self.chrome_userdata_path)
        options.add_experimental_option('useAutomationExtension', False)
    
        options = self._ram_optimization_browser_options(options)

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options)

        driver.implicitly_wait(self.IMPLICITLY_WAIT_TIME) 

        driver.execute_script('window.focus()')
        driver.execute_cdp_cmd('Network.setUserAgentOverride',
                                {"userAgent": self.USERAGENT})

        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
        {
            "source": """
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
                })
                """})

        driver.execute_cdp_cmd("Network.enable", {})
        driver.execute_cdp_cmd("Network.setExtraHTTPHeaders",
                                {"headers": {"User-Agent": "browser1"}})

        if self.half_screen:
            size = driver.get_window_size()
            driver.set_window_size(size['width']/2, size['height'])
            driver.set_window_position(size['width']/2-13, 0)
            
        return driver
        
    @staticmethod
    def _ram_optimization_browser_options(options: Options) -> Options:
        options.add_argument("disable-infobars")
        options.add_experimental_option("excludeSwitches", 
                                        ['enable-automation', "enable-logging"])
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-application-cache")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--lang=en-US")
        
        # Based on https://stackoverflow.com/questions/59514049/unable-to-sign-into-google-with-selenium-automation-because-of-this-browser-or
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--disable-web-security")
        return options