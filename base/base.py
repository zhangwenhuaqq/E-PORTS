import logging
import time
from selenium.webdriver.support.wait import WebDriverWait
from tools.get_log import GetLogger

log = GetLogger.get_logger()

class Base():
    def __init__(self,driver):
        log.info("初始化driver{}".format(driver))
        self.driver = driver

    #查找元素方法封装
    def base_find_element(self,loc,timeout=30,poll=0.5):
        log.info("正在查找元素：{}".format(loc))
        #使用显示等待查找元素
        return WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll).until(lambda x:x.find_element(*loc))
    #点击元素方法封装
    def base_click(self,loc):
        log.info("正在点击元素：{}".format(loc))
        self.base_find_element(loc).click()
    #输入元素方法封装
    def base_input(self,loc,value):
        #获取元素
        log.info("成功获取元素：{}".format(loc))
        el=self.base_find_element(loc)
        #清空
        log.info("正在清空元素：{}".format(loc))
        el.clear()
        log.info("正在输入元素：{}".format(loc))
        #输入元素
        el.send_keys(value)
    #获取文本信息方法封装
    def base_get_text(self,loc):
        return self.base_find_element(loc).text
    #截图方法封装
    def base_get_image(self):
        self.driver.get_screenshot_as_file("../image/image{}.png".format(time.strftime("%Y_%m_%d %H_%M_S")))
    #判断元素是否存在方法封装
    def base_element_is_exist(self,loc):
        try:
            self.base_find_element(loc)
            return True #代表元素存在
        except Exception as e:
            log.info("元素不存在：{}".format(loc))
            return False #代表元素不存在

