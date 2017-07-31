import os
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
class SeleniumTest(StaticLiveServerTestCase):
    chromedriver = "C:\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.get("http://stackoverflow.com")
    driver.quit()
    # def setUp(self):
    #     self.browser = WebDriver()
    #     self.browser.implicitly_wait(10)
    #
    # def tearDown(self):
    #     self.browser.quit()
    #
    # def test_search(self):
    #
    #     self.browser.get('/')
    #     search_text = self.browser.find_element_by_id('search')
    #     search_text.send_keys('java')
    #     self.browser.find_element_by_name('submit').click()
    #
    #     search_page_header = self.browser.find_element_by_tag_name('h2').text
    #     self.assertIn('Wyniki wyszukiwania:', search_page_header)
