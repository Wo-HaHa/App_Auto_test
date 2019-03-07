import os
from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction
apk_path=os.path.dirname(os.path.abspath("."))
desired_caps={}
desired_caps["platformName"]='Android'#设备系统
desired_caps["platformVersion"]="5.1.1"#Android版本
desired_caps["deviceName"]="127.0.0.1:62001"#设备名称
desired_caps["sessionOverride"]=True#覆盖每一次的session
desired_caps["app"]=apk_path+"/app/todolist.apk"#测试apk包的路径
desired_caps["noReset"]=True#检查是否有这个包
desired_caps["appPackage"]="com.example.todolist"
desired_caps["appActivity"]="com.example.todolist.LoginActivity"
driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)#启动app
driver.find_element_by_id("com.example.todolist:id/nameET").send_keys("1")#定位输入框并且输入
driver.find_element_by_id("com.example.todolist:id/passwordET").send_keys("1")#定位输入框并且输入
driver.find_element_by_id("com.example.todolist:id/loginBtn").click()#点击登录
driver.find_element_by_id("com.example.todolist:id/action_new").click()#点击增加
driver.find_element_by_id("com.example.todolist:id/toDoItemDetailET").send_keys("11111")#输入代办事项内容
driver.find_element_by_id("com.example.todolist:id/saveBtn").click()#点击保存
driver.quit()
driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)#启动app
driver.find_element_by_id("com.example.todolist:id/nameET").send_keys("1")#定位输入框并且输入
driver.find_element_by_id("com.example.todolist:id/passwordET").send_keys("1")#定位输入框并且输入
driver.find_element_by_id("com.example.todolist:id/loginBtn").click()#点击登录
el=driver.find_elements_by_id("com.example.todolist:id/toDoItemDetailTv")[0]#定位长按的元素
TouchAction(driver).long_press(el).perform()#进行长按
# time.sleep(3)
driver.find_elements_by_id("android:id/title")[1].click()#点击删除按钮
driver.find_element_by_id("android:id/button1").click()#点击确定按钮
driver.quit()




