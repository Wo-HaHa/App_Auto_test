from Pageobjects.Base_App import basepage
from appium.webdriver.common.mobileby import By

class App_delete(basepage):
    note_loc = (By.ID, "com.pdswp.su.smartcalendar:id/note_title")  # 定位按压的备忘录
    delete_loc = (By.ID, "com.pdswp.su.smartcalendar:id/menu_delete")  # 定位点击删除的按钮
    menu_loc = (By.ID, "com.pdswp.su.smartcalendar:id/ab_icon2")  # 定位菜单栏
    recycle_loc=(By.NAME,"回收站")#定位回收站
    click_recycle_loc=(By.ID,"com.pdswp.su.smartcalendar:id/button")#定位点击清空回收站
    cnfirm_loc=(By.NAME,"确定")#定位确定按钮
    def app_delete(self):
        self.longpress(*self.note_loc)#长按备忘录
        self.click(*self.delete_loc)#点击删除
        self.click(*self.menu_loc)#点击菜单栏
        self.click(*self.recycle_loc)#点击回收站
        self.click(*self.click_recycle_loc)#点击清空回收站
        self.click(*self.cnfirm_loc)#点击确定按钮
