import page
from base.base_set import Base
from tools.get_path import get_file_path
from tools.get_yaml import *
from time import sleep
data = get_read(get_file_path('page_data','page_voyage_manager_son_add_receipt.yaml'))

class PageVoyageManagerSonAddReceipt(Base):
    #切换子单
    def page_click_son_order(self):
        self.base_click(data[0]["type"],data[0]["element"])
    #点击支付管理
    def page_click_pay_manage(self):
        self.base_click(data[1]["type"],data[1]["element"])
    #点击添加付款
    def page_click_pay_money(self):
        self.base_click(data[2]["type"],data[2]["element"])
    #输入付款公司名称
    def page_select_company(self,paycompany):
        self.select_send(data[3]["type"],data[3]["element"],paycompany)
    #点击付款时间
    def page_click_pay_time(self):
        self.base_click(data[4]["type"],data[4]["element"])
    #点击今天
    def page_click_today(self):
        self.base_click(data[5]["type"],data[5]["element"])
    #点击上传凭证
    def page_click_upload(self):
        self.upload(data[6]["type"],data[6]["element"])
    #添加收款流水号
    def page_click_Collection_Serial_Number(self,Collection_Serial_Number):
        self. base_input(data[7]["type"],data[7]["element"],Collection_Serial_Number)
    #点击确认按钮
    def page_click_confirm(self):
        self.base_click(data[8]["type"],data[8]["element"])
    #截图
    def page_get_image(self):
        self.base_get_image()
    #判断添加付款按钮存在
    def page_is_add_receipt_success(self):
        return self.base_element_is_exist(data[9]["type"], data[9]["element"])

    #组合业务方法
    def voyage_Manager_Son_Add_Settlement_receipt(self,paycompany,Collection_Serial_Number):
        sleep(5)
        self.page_click_son_order()
        sleep(2)
        self.page_click_pay_manage()
        sleep(2)
        self.page_click_pay_money()
        sleep(2)
        self.page_select_company(paycompany)
        sleep(2)
        self.page_click_pay_time()
        sleep(2)
        self.page_click_today()
        sleep(2)
        self.page_click_upload()
        sleep(2)
        self.page_click_Collection_Serial_Number(Collection_Serial_Number)
        sleep(2)
        self.page_click_confirm()



# if __name__=='__main__':
#     login=PageLogin()
