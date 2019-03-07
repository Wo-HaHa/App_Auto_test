from Pageobjects.Base_App import basepage
from appium.webdriver.common.mobileby import By
import unittest
class Login(basepage):
    menu_loc=(By.ID,"com.pdswp.su.smartcalendar:id/ab_icon2")#定位菜单栏
    click_login_loc = (By.ID, "com.pdswp.su.smartcalendar:id/username")#定位登录按钮
    email_test_loc=(By.ID, "com.pdswp.su.smartcalendar:id/email")#定位输入邮箱的文本框
    pwd_test_loc=(By.ID,"com.pdswp.su.smartcalendar:id/password")#定位输入密码的位置
    login_loc=(By.ID,"com.pdswp.su.smartcalendar:id/login")#定位点击登录的位置
    exit_loc=(By.ID,"com.pdswp.su.smartcalendar:id/exit")#定位退出按钮

    uuu=(By.ID, "com.pdswp.su.smartcalendar:id/index_ab_title")


    def login(self,email,pwd):
        self.click(*self.menu_loc)
        self.click(*self.click_login_loc)
        self.sendkeys(email,*self.email_test_loc)#输入email
        self.sendkeys(pwd,*self.pwd_test_loc)#输入密码
        self.click(*self.login_loc)#点击登录

        self.asser=self.get_text(self.uuu)

        self.click(*self.menu_loc)#点击菜单按钮
        self.click(*self.click_login_loc)#点击用户
        self.click(*self.exit_loc)#点击退出
