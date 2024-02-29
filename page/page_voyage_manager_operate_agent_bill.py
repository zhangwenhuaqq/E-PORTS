import page
from base.base_set import Base
from tools.get_path import get_file_path
from tools.get_yaml import *
from time import sleep
data = get_read(get_file_path('page_data','page_voyage_manager_operate_agent_bill.yaml'))

class PageVoyageManagerOperateAgentBill(Base):
    #切换到子单
    def page_click_agent(self):
        self.base_click(data[0]["type"],data[0]["element"])
    #点击”账单管理“title
    def page_click_bill_title(self):
        self.base_click(data[1]["type"],data[1]["element"])
    #点击DN账单审核
    def page_click_DN_view(self):
        self.base_click(data[2]["type"],data[2]["element"])
    #点击拒绝按钮
    def page_click_DN_refuse(self):
        self.base_click(data[3]["type"],data[3]["element"])
    #填写拒绝原因
    def page_input_resuse_reason(self,reason):
        self.base_input(data[4]["type"],data[4]["element"],reason)
    #点击确定按钮
    def page_click_DN_confirm(self):
        self.base_click(data[5]["type"],data[5]["element"])
    #点击TA审核按钮
    def page_click_TA_view(self):
        self.base_click(data[6]["type"],data[6]["element"])
    #点击接收
    def page_click_DN_accept(self):
        self.base_click(data[7]["type"],data[7]["element"])
    #截图
    def page_get_image(self):
        self.base_get_image()
    #判断服务项变更信息存在
    def page_is_change_service_success(self):
        return self.base_element_is_exist(data[8]["type"], data[8]["element"])

    #组合业务方法
    def voyage_manager_operate_agent_Bill(self,reason):
        sleep(5)
        self.page_click_agent()
        sleep(2)
        self.page_click_bill_title()
        sleep(2)
        self.page_click_DN_view()
        sleep(3)
        self.scroll_foot(800)
        sleep(2)
        self.page_click_DN_refuse()
        sleep(2)
        self.page_input_resuse_reason(reason)
        sleep(2)
        self.page_click_DN_confirm()
        sleep(4)
        self.page_click_agent()
        sleep(2)
        self.page_click_bill_title()
        sleep(2)
        self.page_click_TA_view()
        sleep(4)
        self.scroll_foot(800)
        self(2)
        self.page_click_DN_accept()
        sleep(2)


# if __name__=='__main__':
#     login=PageLogin()
