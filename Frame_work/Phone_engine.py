from appium import webdriver
import time
import os
import yaml
from appium.webdriver.common.touch_action import TouchAction
class Engine(object):
    def start(self):
        config_path=os.path.dirname(os.path.abspath("."))+"\config\config.yaml"
        with open(config_path,"r",encoding="utf-8") as file:
            data=yaml.load(file)
        desired_caps = {}
        desired_caps["platformName"]=data['platformName']#设备系统
        desired_caps["platformVersion"]=data['platformVersion']#Android版本
        desired_caps["deviceName"]=data['deviceName']#设备名称
        desired_caps["sessionOverride"]=data['sessionOverride']#覆盖每一次的session

        desired_caps["noReset"]=data['noReset']#检查是否有这个包
        desired_caps["appPackage"]=data['appPackage']
        desired_caps["appActivity"]=data['appActivity']#激活
        apk_path = os.path.dirname(os.path.abspath("."))+"/app/znbwl.apk"
        desired_caps["app"] = apk_path  # 测试apk包的路径
        # print(apk_path)

        self.driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub',desired_caps)
        # self.driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)#启动app
        return self.driver
    def end(self):
        self.driver.quit()

# en=Engine()
# en.start()