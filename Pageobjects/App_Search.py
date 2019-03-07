from Pageobjects.Base_App import basepage
from appium.webdriver.common.mobileby import By
class Search(basepage):
    # menu_loc=(By.ID,"com.pdswp.su.smartcalendar:id/ab_icon2")#定位菜单栏
    click_search_loc = (By.ID, "com.pdswp.su.smartcalendar:id/toolbar_search")#定位搜索按钮
    search_title_loc=(By.ID,"android:id/search_src_text")#定位搜索框

    def search(self,content):
        # self.click(*self.menu_loc)#点击菜单
        self.click(*self.click_search_loc)#点击搜索
        self.sendkeys(content,*self.search_title_loc)#输入搜索的内容
        self.driver.keyevent(66)
