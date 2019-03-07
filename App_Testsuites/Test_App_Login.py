import unittest
from App_Testsuites.Base_testcase import BaseTestCase
from appium.webdriver.common.mobileby import By
from Pageobjects.App_Login import Login
import time
import os
from appium import webdriver
import unittest
from ddt import data, ddt, unpack
import time
from Frame_work.read_from_exel import Read_exel

data_path = os.path.dirname(os.path.abspath('.')) + "/data/2.xlsx"
testdata = Read_exel.read_excel(data_path, "Sheet1")
@ddt
class Test_Login(BaseTestCase):
    @data(*testdata)
    def test_login(self,data):
        self.search_email = data["email"]
        self.search_pwd = data["pwd"]
        print("输入内容>：%s" %self.search_email )
        print("输入内容>：%s" %self.search_pwd )
        lo = Login(self.driver)
        lo.login(self.search_email, self.search_pwd)
        try:
            self.assertEqual(self.asser, "智能备忘录")
            print("成功登陆")
        except Exception as e:
            print("登录失败")




        # search_input = self.driver.find_element_by_id('kw')
        #
        # # 找到后，键入 java 并提交搜索
        # search_input.send_keys(search_string)
        # time.sleep(3)
        # search_input.submit()

if __name__=="__main__":
    unittest.main()
