import page
from base.base_set import Base
from tools.get_path import get_file_path
from tools.get_yaml import *
from time import sleep
data = get_read(get_file_path('page_data','page_voyage_manager_appoint.yaml'))

class PageVoyageManagerAppoint(Base):
    #点击切换子询价但
    def page_click_agent_inquiry(self):
        self.base_click(data[0]["type"],data[0]["element"])
    #点击点击委托方按钮
    def page_click_appoint(self):
        self.base_click(data[1]["type"],data[1]["element"])
    #点击点击确认委托按钮
    def page_click_appoint_confirm(self):
        self.base_click(data[2]["type"],data[2]["element"])
    #点击提交按钮
    def page_click_submit(self,):
        self.base_click(data[3]["type"],data[3]["element"])
    #点击弹窗确认按钮
    def page_click_confirm(self):
        self.base_click(data[4]["type"],data[4]["element"])
    #点击查看订单详情
    def page_order_detial(self,):
        self.base_click(data[5]["type"],data[5]["element"])
    #截图
    def page_get_image(self):
        self.base_get_image()
    #判断”已委托“按钮存在
    def page_is_appoint_success(self):
        return self.base_element_is_exist(data[6]["type"], data[6]["element"])
    #组合业务方法
    def add_voyage_manager_appoint(self):
        sleep(5)
        self.page_click_agent_inquiry()
        sleep(2)
        self.page_click_appoint()
        sleep(2)
        self.page_click_appoint_confirm()
        sleep(1)
        self.page_click_submit()
        sleep(1)
        self.page_click_confirm()
        sleep(1)
        self.page_order_detial()

# if __name__=='__main__':
#     login=PageLogin()
