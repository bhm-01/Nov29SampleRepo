import os
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4

@pytest.mark.webtest
def test_api():
    url = "https://reqres.in/api/users?page=2"
    r = requests.get(url)
    name_api = os.environ.get('projectName')
    print("name from env for api ",name_api)
    assert  r.status_code == 200

@pytest.mark.webtest
def test_ui():
    chrome_options = Options()
    chrome_options.add_argument("window-size=1920,1080");
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    name1 = os.environ.get('projectName')
    print("name from env ui ",name1)
    driver = webdriver.Chrome(options=chrome_options,
                               executable_path=ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())
    driver.get("http://www.python.org")
    assert "Python" in driver.title


@pytest.mark.webtest
def test_ui():
    chrome_options = Options()
    chrome_options.add_argument("window-size=1920,1080");
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    name1 = os.environ.get('projectName')
    print("name from env ui ",name1)
    driver = webdriver.Chrome(options=chrome_options,
                               executable_path=ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())
    driver.get("https://github.com/")
    assert "GitHub: Where the world builds software · GitHub" in driver.title
