import unittest
from App_Testsuites.Base_testcase import BaseTestCase
from Pageobjects.App_Delete import App_delete
class Test_delete(BaseTestCase):
    def test_delete(self):
        delete=App_delete(self.driver)
        delete.app_delete()
if __name__=="__main__":
    unittest.main()