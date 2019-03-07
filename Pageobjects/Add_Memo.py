from Pageobjects.Base_App import basepage
from appium.webdriver.common.mobileby import By
class Add(basepage):
    menu_loc=(By.ID,"com.pdswp.su.smartcalendar:id/ab_icon2")#定位菜单栏
    click_memo_loc = (By.ID, "com.pdswp.su.smartcalendar:id/design_menu_item_text")#定位备忘录
    content_loc=(By.ID,"com.pdswp.su.smartcalendar:id/add_input_content")#定位备忘录输入框
    confirm_loc=(By.ID,"com.pdswp.su.smartcalendar:id/quick_add")#定位确定按钮


    add_loc=(By.ID,"com.pdswp.su.smartcalendar:id/menuAdd")#定位页面上的添加

    def add(self,content1,content2):
        self.click(*self.menu_loc)#点击菜单
        self.click(*self.click_memo_loc)#点击备忘录
        self.sendkeys(content1,*self.content_loc)#输入备忘录内容
        self.click(*self.confirm_loc)#点击确定按钮


        self.click(*self.add_loc)#点击页面上的添加
        self.sendkeys(content2, *self.content_loc)  # 输入备忘录内容
        self.click(*self.confirm_loc)  # 点击确定按钮

