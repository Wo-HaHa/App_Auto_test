from appium import webdriver
from Frame_work.Phone_engine import Engine
import unittest
import warnings
class BaseTestCase(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        En=Engine()
        self.driver=En.start()



    def tearDown(self):
        self.driver.quit()
        # self.driver.close_app()
        pass