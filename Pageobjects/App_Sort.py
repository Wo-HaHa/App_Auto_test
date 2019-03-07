from Pageobjects.Base_App import basepage
from appium.webdriver.common.mobileby import By
import time

class App_sort(basepage):
    note_loc = (By.ID, "com.pdswp.su.smartcalendar:id/note_title")  # 定位按压的备忘录
    sort_loc = (By.ID, "com.pdswp.su.smartcalendar:id/menu_sort")  # 定位点击排序的按钮
    confirm_ok_loc=(By.ID,"com.pdswp.su.smartcalendar:id/toolbar_ok")#定位对勾
    guidang_loc=(By.NAME,"归档")#定位归档
    menu_loc = (By.ID, "com.pdswp.su.smartcalendar:id/ab_icon2")  # 定位菜单栏
    recover_loc=(By.ID,"com.pdswp.su.smartcalendar:id/menu")#定位恢复
    back_loc=(By.ID,"com.pdswp.su.smartcalendar:id/ab_icon2")#定位返回
    def app_sort(self):
        self.longpress(*self.note_loc)#长按备忘录
        self.click(*self.sort_loc)#点击排序
        self.Swipe(694,176,694,300,1000)
        self.click(*self.confirm_ok_loc)#点击对勾
        self.longpress(*self.note_loc)  # 长按备忘录
        self.click(*self.guidang_loc)#点击归档
        self.click(*self.menu_loc)#点击菜单栏
        self.click(*self.guidang_loc)  # 点击归档
        self.Swipe(663,150,550,150,300)#向左滑动
        time.sleep(5)
        self.click(*self.recover_loc)#点击复原
        self.click(*self.back_loc)#点击返回





