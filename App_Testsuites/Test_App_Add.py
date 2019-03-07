import unittest
from Pageobjects.Add_Memo import Add
from appium.webdriver.common.mobileby import By
from App_Testsuites.Base_testcase import BaseTestCase
class Test_add(BaseTestCase):
    def test_add(self):
        add=Add(self.driver)
        add.add("11","22")
        self.assertEqual(add.find_element(By.ID, "com.pdswp.su.smartcalendar:id/index_ab_title"), "智能备忘录")


if __name__=="__main__":
    unittest.main()