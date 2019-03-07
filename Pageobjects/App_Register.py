from Pageobjects.Base_App import basepage
from appium.webdriver.common.mobileby import By
class Register(basepage):
    menu_loc=(By.ID,"com.pdswp.su.smartcalendar:id/ab_icon2")#定位菜单栏
    click_register_loc = (By.ID, "com.pdswp.su.smartcalendar:id/email")#定位注册按钮
    click1_register_loc=(By.ID, "com.pdswp.su.smartcalendar:id/register")#定位“点击注册”
    username_test_loc=(By.ID,"com.pdswp.su.smartcalendar:id/username")#定位名字的位置
    eamil_test_loc = (By.ID, "com.pdswp.su.smartcalendar:id/email")  # 定位email位置
    pwd_test_loc = (By.ID, "com.pdswp.su.smartcalendar:id/password")  # 定位密码的位置
    submit_loc=(By.ID,"com.pdswp.su.smartcalendar:id/reguser")#定位注册的位置
    click_login_loc = (By.ID, "com.pdswp.su.smartcalendar:id/username")  # 定位登录按钮

    exit_loc = (By.ID, "com.pdswp.su.smartcalendar:id/exit")  # 定位退出按钮

    uuuu=(By.ID, "com.pdswp.su.smartcalendar:id/index_ab_title")



    def register(self,admin,email,pwd):
        self.click(*self.menu_loc)
        self.click(*self.click_register_loc)
        self.click(*self.click1_register_loc)
        self.sendkeys(admin,*self.username_test_loc)#输入用户
        self.sendkeys(email,*self.eamil_test_loc)#输入email
        self.sendkeys(pwd, *self.pwd_test_loc)#输入密码
        self.click(*self.submit_loc)#点击注册
        self.aser=self.get_text(*self.uuuu)
        self.click(*self.menu_loc)  # 点击菜单按钮
        self.click(*self.click_login_loc)  # 点击用户
        self.click(*self.exit_loc)  # 点击退出