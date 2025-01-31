import logging
import os
import sys
from pathlib import Path

from ak_requests.utils import latest_useragent
from helium import start_chrome
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ak_selenium.browser import Browser

# Disable webdriver-manager logs per https://github.com/SergeyPirogov/webdriver_manager#wdm_log
os.environ["WDM_LOG"] = str(logging.NOTSET)


class Chrome(Browser):
    USERAGENT: str = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    )
    """default fallback useragent"""

    def __init__(
        self,
        headless: bool = False,
        chrome_userdata_path: str | None = None,
        half_screen: bool = True,
    ) -> None:
        """Initialize a chrome instance

        Args:
            headless (bool, optional): Start in headless mode. Defaults to False.
            chrome_userdata_path (str | None, optional): existing `userdata` path. Defaults to None.
            half_screen (bool, optional): split to half-screen width. Defaults to True.

        Returns:
            None
        """

        _useragent: str = latest_useragent("Chrome")
        if _useragent != "":
            self.USERAGENT = _useragent

        self.headless = headless
        self.half_screen = half_screen
        self.chrome_userdata_path = chrome_userdata_path

        self.driver: webdriver.Chrome = self._driver()
        super().__init__(driver=self.driver)
        self._prep_driver(useragent=self.USERAGENT)

        if half_screen:
            self.halfscreen()
        return None

    def _set_userdata_path(self, datapath: str | None) -> str | None:
        self.chrome_userdata_path: str | None = None

        if not datapath and sys.platform == "win32":
            _chrome_userdata_path: Path = (
                Path.home() / "AppData" / "Local" / "Google" / "Chrome" / "User Data"
            )
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

    def _driver(self) -> webdriver.Chrome:
        """
        Initializes a Chrome web driver with specific options and configurations.

        Returns:
            webdriver.Chrome: The initialized Chrome driver object.
        """
        driver = start_chrome(
            url=None, headless=self.headless, maximize=False, options=self.options
        )
        driver = self.__inject_antidetection_script(driver=driver)
        return driver  # type: ignore

    @property
    def options(self) -> webdriver.ChromeOptions:
        """Set default `webdriver.ChromeOptions`"""
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-gpu")
        if self.headless:
            options.add_argument("--headless")
            options.add_argument("--window-size=1920,1080")
        options.add_argument("start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_experimental_option("useAutomationExtension", False)

        options.add_argument("--hide-scrollbars")
        options.add_argument("--mute-audio")
        options.add_argument("--disable-popup-blocking")

        self.chrome_userdata_path = userdata_path(folderpath=self.chrome_userdata_path)
        if self.chrome_userdata_path:
            options.add_argument("--user-data-dir=" + self.chrome_userdata_path)

        options = self.__ram_optimization_browser_options(options)
        options = self.__options_override_javascript_variables(options=options)
        return options

    @staticmethod
    def __options_override_javascript_variables(options: Options):
        # Override JavaScript Variables: Many websites check navigator.webdriver. Override it to avoid detection:
        options.add_experimental_option(
            "prefs", {"profile.managed_default_content_settings.images": 2}
        )
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--enable-blink-features=ShadowDOMV0")
        return options

    def __inject_antidetection_script(
        self, driver: webdriver.Chrome
    ) -> webdriver.Chrome:
        # Inject scripts to modify window properties:
        driver.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument",
            {
                "source": """
                Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
                """
            },
        )
        return driver

    @staticmethod
    def __ram_optimization_browser_options(options: Options) -> Options:
        options.add_argument("disable-infobars")
        options.add_experimental_option(
            "excludeSwitches", ["enable-automation", "enable-logging"]
        )
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-application-cache")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--lang=en-US")

        # Based on https://stackoverflow.com/questions/59514049/unable-to-sign-into-google-with-selenium-automation-because-of-this-browser-or
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--disable-web-security")

        options.add_argument("--disable-sync")
        options.add_argument("--disable-3d-apis")
        options.add_argument("--disk-cache-size=0")

        return options


def userdata_path(folderpath: str | None) -> str | None:
    """Get Chrome Userdata Path

    Args:
        folderpath (str | None): Chrome Userdata Path

    Returns:
        str | None: Chrome Userdata Path
    """
    if folderpath:
        return folderpath
    elif sys.platform == "win32":
        _chrome_userdata_path: Path = (
            Path.home() / "AppData" / "Local" / "Google" / "Chrome" / "User Data"
        )
        if _chrome_userdata_path.exists():
            return str(_chrome_userdata_path)
    return None
