import unittest
from App_Testsuites.Base_testcase import BaseTestCase
from Pageobjects.App_Search import Search
class Test_Search(BaseTestCase):
    def test_search(self):
        se=Search(self.driver)
        se.search("11")
if __name__=="__main__":
    unittest.main()
