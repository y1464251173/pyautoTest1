import unittest
from time import sleep

from selenium import webdriver

from chapter8.the_basic_use_poium.test_case.baidu_page import BaiduPage


class TestBaidu(unittest.TestCase):
    """百度搜索测试"""
    @classmethod
    def setUpClass(cls):
       cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_search_search_case(self):
        """搜索关键字：Selenium"""
        page = BaiduPage(self.driver)
        page.get("https://www.baidu.com")
        page.search_input = "Selenium"
        page.search_button.click()
        sleep(2)
        self.assertEqual(page.get_title(), "Selenium_百度搜索")

if __name__ == "__main__":
    unittest.main(verbosity=2)