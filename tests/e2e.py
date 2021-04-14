import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_scores_service(app= 'http://127.0.0.1:5000/'):
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
    driver.get(app)
    search = driver.find_element_by_id('score2').text
    search2 = int(search)
    print("The score is :" , search2)
    if (search2 > 0) and (search2 < 1000):
        result = 0
    else:
        result = -1
    time.sleep(10)
    driver.close()
    return result


def main_function():
    return 0

res = test_scores_service('http://127.0.0.1:5000/')


if res == 0:
    print("value is :", res)
else:
    print('exited with -1')

