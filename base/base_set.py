import logging
import os
import time
from pywinauto import Desktop
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from tools.get_log import GetLogger
from selenium.webdriver.support.ui import Select

log = GetLogger.get_logger()


class Base():
    def __init__(self, driver):
        log.info("初始化driver{}".format(driver))
        self.driver = driver

    # 查找元素方法封装
    def base_find_element(self, X, loc, timeout=30, poll=0.5):
        # 使用显示等待查找元素
        if X == "xpath":
            return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
                lambda x: x.find_element_by_xpath(loc))
        if X == "css_selector":
            return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
                lambda x: x.find_element_by_css_selector(loc))
        else:
            return print("元素未找到")

    # 滑块验证封装
    def sw(self, X, loc):
        action_chains = ActionChains(self.driver)
        sp = self.base_find_element(X, loc)
        action_chains.drag_and_drop_by_offset(sp, 400, 0).perform()

    # 点击元素方法封装
    def base_click(self, X, loc):
        log.info("正在点击元素：{}".format(loc))
        self.base_find_element(X, loc).click()

    # 输入元素方法封装
    def base_input(self, X, loc, value):
        # 获取元素
        log.info("成功获取元素：{}".format(loc))
        el = self.base_find_element(X, loc)
        # 清空
        log.info("正在清空元素：{}".format(loc))
        el.clear()
        log.info("正在输入元素：{}".format(loc))
        # 输入元素
        el.send_keys(value)

    # 键盘操作
    def send_key(self, data):
        action = ActionChains(self.driver)
        if data == 'ENTER':
            action.send_keys(Keys.ENTER).pause(1).perform()
        else:
            action.send_keys(data).pause(1).perform()
        time.sleep(0.5)

    # 先点击操作后下拉写入
    def select_send(self, X, loc, data):
        self.base_click(X, loc)
        self.send_key(data)
        time.sleep(4)
        self.send_key(Keys.ENTER)

    # 上传文件
    def upload(self, x, loc):
        self.base_click(x, loc)
        dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        app = Desktop()
        dialog = app['打开']  # 根据名字找到弹出窗口
        dialog["Edit"].type_keys(dir_path + '\\image\\image2023_12_2913_28_S.png')  # 在输入框中输入值
        time.sleep(2)
        dialog["Button"].click()
        dialog["Button"].click()


    # 上传文件
    # def upload_image(file_path):
    #     url = 'http://example.com/upload_image'  # 上传图片的API接口地址
    #     files = {'image': open(file_path, 'rb')}
    #     response = requests.post(url, files=files)
    #     if response.status_code == 200:
    #         print('图片上传成功')
    #     else:
    #         print('图片上传失败')
    #
    # file_path = 'path/to/image.jpg'  # 图片文件的路径
    # upload_image(file_path)

    # 获取文本信息方法封装
    def base_get_text(self, X, loc):
        return self.base_find_element(X, loc).text

    # 下拉选择框方法封装
    def base_get_select(self, X, loc):
        els = self.base_find_element(X, loc)
        select = Select(els)
        log.info("成功获取元素列表：{}".format(loc))
        return select.select_by_index(1)

    # 截图方法封装
    def base_get_image(self):
        self.driver.get_screenshot_as_file("../image/image{}.png".format(time.strftime("%Y_%m_%d %H_%M_S")))

    # 判断元素是否存在方法封装
    def base_element_is_exist(self, X, loc):
        try:
            self.base_find_element(X, loc, 5)
            return True  # 代表元素存在
        except Exception as e:
            log.info("元素不存在：{}".format(loc))
            return False  # 代表元素不存在

    # 鼠标滚动
    def scroll_top(self):
        if self.driver.name == "Chrome":
            js = "var q=document.body.scrollTop=0"
        else:
            js = "var q=document.documentElement.scrollTop=0"
        return self.driver.execute_script(js)

    # 鼠标滚动到底部
    def scroll_foot(self, leng):
        if self.driver.name == "Chrome":
            js = "var q=document.body.scrollTop=%d" % (leng)
        else:
            js = "var q=document.documentElement.scrollTop=%d" % (leng)
        return self.driver.execute_script(js)

    # 鼠标滚动
    def scrool(self):
        actions = ActionChains()
        actions.move_by_offset(0, 200).perform()

    # 缩放(废弃)
    def narrow_key(self, zoom):
        if zoom == "zoom_in":
            return self.driver.execute_script("document.body.style.zoom='1.2'")
        else:
            return self.driver.execute_script("document.body.style.zoom='0.7'")

    # chrome设置缩放比例
    def set_zoom(self, zoom):
        self.driver.get('chrome://settings/')
        if zoom == "zoom_in":
            self.driver.execute_script('chrome.settingsPrivate.setDefaultZoom(1.2);')
        elif zoom == "zoom_out":
            self.driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.8);')
        self.driver.back()

    # 获取节点属性
    def get_attr(self, value, data, locateType='xpath'):
        el = self.locate(value, locateType)
        attr_data = el.get_attribute(data)
        return attr_data

    # 鼠标右键操作
    def actClick(self, value):
        el = self.locate(value)
        actions = ActionChains(self.driver)
        actions.context_click(el)
        actions.perform()

    # 获取弹出框
    def get_alert(self):
        time.sleep(2)
        text = self.driver.switch_to.alert.text
        return text

    # 选择下拉框
    def get_Select(self, value, locateType='xpath'):
        s = Select(self.locate(value, locateType))
        return s

    # 获取当前页面title
    def get_title(self, driver):
        time.sleep(2)
        title = driver.title
        return title
