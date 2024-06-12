from selenium import webdriver
import page
from time import sleep
from base.base_set import Base


# 获取driver
def get_driver():
    # 设置类属性
    driver = webdriver.Chrome()
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
                  Object.defineProperty(navigator, 'webdriver', {
                    get: () => undefined
                  })
                """
    })  # 绕过阿里云滑块检测
    # 打开浏览器
    driver.get(page.url)
    # 浏览器最大化
    driver.maximize_window()
    sleep(2)
    zoom = Base(driver)
    zoom.set_zoom("zoom_out")
    sleep(2)
    return driver
