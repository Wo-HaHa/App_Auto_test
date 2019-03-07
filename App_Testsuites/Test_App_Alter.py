import unittest
from App_Testsuites.Base_testcase import BaseTestCase
from Pageobjects.App_Alter import Alter
from appium.webdriver.common.mobileby import By
import time
class Test_alter(BaseTestCase):
    def test_alter(self):
        al=Alter(self.driver)
        al.login("2478346011@qq.com","19970803")
        al.alter("lixiuzhi")
        self.assertEqual(al.find_element(By.ID,"com.pdswp.su.smartcalendar:id/index_ab_title").text,"用户中心")


if __name__=="__main__":
    unittest.main()
