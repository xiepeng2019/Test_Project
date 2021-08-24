from selenium import webdriver
import unittest





"""声明浏览器驱动"""
class SearchTest(unittest.TestCase):
    def setup(self):
        self.driver = webdriver.Chrome
        self.driver.maximize_window()
        self.driver.get('http://demo.magentocommerce.com')
    def test_search(self):
        self.aa=self.driver.find_element_by_name("q")
        self.aa.clear()
        self.aa.send_keys("Flask web开发实战")
        self.submit()


if __name__=="__main__":
    unittest.main()