import page
from base.base_set import Base
from tools.get_path import get_file_path
from tools.get_yaml import *
from time import sleep
data = get_read(get_file_path('page_data','page_agent_add_bill.yaml'))

class PageAgentAddBill(Base):
    #点击”账单管理“title
    def page_click_bill_title(self):
        self.base_click(data[0]["type"],data[0]["element"])
    #点击DN编辑按钮
    def page_click_DN_edit(self):
        self.base_click(data[1]["type"],data[1]["element"])
    #点击预览按钮
    def page_click_DN_preview(self):
        self.base_click(data[2]["type"],data[2]["element"])
    #点击返回按钮
    def page_click_DN_preview_back(self):
        self.base_click(data[3]["type"],data[3]["element"])
    #点击发送按钮
    def page_click_DN_send(self):
        self.base_click(data[4]["type"],data[4]["element"])
    #点击”下载“按钮
    def page_click_DN_download(self):
        self.base_click(data[5]["type"],data[5]["element"])
    #点击添加账单
    def page_click_add_bill(self):
        self.base_click(data[6]["type"],data[6]["element"])
    #点击本账单付款时间
    def page_click_add_bill_payment_time(self):
        self.base_click(data[7]["type"],data[7]["element"])
    #点击”今天“
    def page_click_add_bill_payment_time_today(self):
        self.base_click(data[8]["type"],data[8]["element"])
    #输入已收金额
    def page_click_add_bill_amount_receive(self,money):
        self.base_input(data[9]["type"],data[9]["element"],money)
    #点击发送
    def page_click_TN_send(self):
        self.base_click(data[10]["type"],data[10]["element"])
    #截图
    def page_get_image(self):
        self.base_get_image()
    #判断服务项变更信息正确
    def page_is_add_service_success(self):
        return self.base_element_is_exist(data[11]["type"], data[11]["element"])

    #组合业务方法
    def agent_add_bill(self,money):
        self.page_click_bill_title()
        sleep(2)
        self.page_click_DN_edit()
        sleep(4)
        self.scroll_foot(800)
        sleep(2)
        self.page_click_DN_preview()
        sleep(3)
        self.scroll_foot(800)
        sleep(2)
        self.page_click_DN_preview_back()
        sleep(3)
        self.scroll_foot(800)
        sleep(2)
        self.page_click_DN_send()
        sleep(4)
        self.page_click_bill_title()
        sleep(2)
        self.page_click_DN_download()
        sleep(2)
        self.page_click_add_bill()
        sleep(4)
        self.scroll_foot(350)
        sleep(2)
        self.page_click_add_bill_payment_time()
        sleep(1)
        self.page_click_add_bill_payment_time_today()
        sleep(2)
        self.page_click_add_bill_amount_receive(money)
        sleep(1)
        self.scroll_foot(800)
        sleep(2)
        self.page_click_TN_send()
        sleep(2)


# if __name__=='__main__':
#     login=PageLogin()
