import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# import codecs

def test_scores_service(app='http://127.0.0.1:5000/'):
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(executable_path=r"./chromedriver.exe")
    driver.get(app)
    driver.maximize_window()
    search = int(driver.find_element_by_id('score2'))
    if (search > 0) and (search < 1000):
        result = 0
    else:
        result = -1
    time.sleep(10)
    driver.close()
    return result


def main_function():
    return 0
