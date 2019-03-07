import unittest
from App_Testsuites.Base_testcase import BaseTestCase
from Pageobjects.App_Sort import App_sort
class Test_sort(BaseTestCase):
    def test_sort(self):
        sort=App_sort(self.driver)
        sort.app_sort()
if __name__=="__main__":
    unittest.main()