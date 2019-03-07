from Pageobjects.Base_App import basepage
from appium.webdriver.common.mobileby import By
class Alter(basepage):
    menu_loc=(By.ID,"com.pdswp.su.smartcalendar:id/ab_icon2")#定位菜单栏
    click_login_loc = (By.ID, "com.pdswp.su.smartcalendar:id/username")#定位登录按钮
    title_loc=(By.ID,"com.pdswp.su.smartcalendar:id/title")#定位用户框
    alter_text_loc=(By.ID,"com.pdswp.su.smartcalendar:id/username")#定位修改框
    confirm_loc=(By.ID,"com.pdswp.su.smartcalendar:id/quick_add")#定位确定按钮

    email_test_loc = (By.ID, "com.pdswp.su.smartcalendar:id/email")  # 定位输入邮箱的文本框
    pwd_test_loc = (By.ID, "com.pdswp.su.smartcalendar:id/password")  # 定位输入密码的位置
    login_loc = (By.ID, "com.pdswp.su.smartcalendar:id/login")  # 定位点击登录的位置


    def login(self, email, pwd):
            self.click(*self.menu_loc)
            self.click(*self.click_login_loc)
            self.sendkeys(email, *self.email_test_loc)  # 输入email
            self.sendkeys(pwd, *self.pwd_test_loc)  # 输入密码
            self.click(*self.login_loc)  # 点击登录
    def alter(self,username):
        self.click(*self.menu_loc)#点击菜单
        self.click(*self.click_login_loc)#点击用户名
        self.click(*self.title_loc)#点击用户框
        self.sendkeys(username,*self.alter_text_loc)#输入修改的用户名
        self.click(*self.confirm_loc)#点击确定按钮
