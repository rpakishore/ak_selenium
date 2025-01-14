import json

import pytest

from ak_selenium import Chrome


@pytest.fixture(scope="module")
def chrome_instance():
    chrome = Chrome(headless=True)
    yield chrome
    chrome.driver.quit()


def test_useragent(chrome_instance):
    """Confirm Useragent is transferred to requests session"""
    chrome = chrome_instance
    session = chrome.session
    url = "https://httpbin.org/headers"
    chrome.get(url)
    browser_headers: dict = json.loads(chrome.soup.find("pre").text).get("headers", {})
    assert browser_headers.get("User-Agent", "") == chrome.USERAGENT

    req_headers = session.get(url).json().get("headers", {})
    assert browser_headers.get("User-Agent", "") == req_headers.get("User-Agent", "")


def test_cookies(chrome_instance):
    """Confirm cookies are transferred to requests session"""
    chrome = chrome_instance
    url = "https://httpbin.org/cookies/set"
    cookie = ("browser_set", 1)
    chrome.get(f"{url}/{cookie[0]}/{cookie[1]}")

    session = chrome.session
    session.get(f"{url}/requests_set/1")

    assert session.cookies.items() == [("browser_set", "1"), ("requests_set", "1")]

    cookies: dict = json.loads(chrome.soup.find("pre").text).get("cookies", {})
    assert cookies["browser_set"] == "1"
