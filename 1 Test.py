from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


def exit(self):
    try:
        self.browser.stop_client()
    except (WebDriverException, AttributeError):
        warn('Assumed use of a local webdriver')
    finally:
        self.browser.quit()

driver = webdriver.Chrome("D:\Python_Projekty\Selenium\chromedriver.exe")
driver.set_page_load_timeout(10)
driver.get("http://www.bing.com")
driver.find_element_by_name("q").send_keys("Selenium first project in python")
driver.find_element_by_name("go").send_keys(Keys.ENTER)
time.sleep(10)

driver.quit()