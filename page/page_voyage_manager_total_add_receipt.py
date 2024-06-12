import page
from base.base_set import Base
from tools.get_path import get_file_path
from tools.get_yaml import *
from time import sleep
data = get_read(get_file_path('page_data','page_voyage_manager_total_add_receipt.yaml'))

class PageVoyageManagerTotalAddReceipt(Base):
    #切换结算管理
    def page_click_settlement(self):
        self.base_click(data[0]["type"],data[0]["element"])
    #点击查看订单
    def page_click_checkorder(self):
        self.base_click(data[1]["type"],data[1]["element"])
    #点击航程号输入框
    def page_click_voyage(self,voyage_no):
        self.select_send(data[2]["type"],data[2]["element"],voyage_no)
    #点击搜索按钮
    def page_click_search(self):
        self.base_click(data[3]["type"],data[3]["element"])
    #点击订单详情
    def page_click_order_detail(self):
        self.base_click(data[4]["type"],data[4]["element"])
    #点击总单收款管理
    def page_click_receipt_manager(self):
        self.base_click(data[5]["type"],data[5]["element"])
    #点击添加收款
    def page_click_add_receipt(self):
        self.base_click(data[6]["type"],data[6]["element"])
    #添加收款流水号
    def page_click_Collection_Serial_Number(self,Collection_Serial_Number):
        self. base_input(data[7]["type"],data[7]["element"],Collection_Serial_Number)
    #点击上传收款凭证
    def page_click_Receipt_Voucher(self):
        self.upload(data[8]["type"],data[8]["element"])
    #输入凭证流水金额
    def page_click_Voucher_flow_amount(self,Voucher_flow_amount):
        self. base_input(data[9]["type"],data[9]["element"],Voucher_flow_amount)
    #输入收款公司
    def page_click_Name_receiver(self,Name_receiver):
        self.select_send(data[10]["type"],data[10]["element"],Name_receiver)
    #点击确认按钮
    def page_click_confirm(self):
        self.base_click(data[11]["type"],data[11]["element"])
    #截图
    def page_get_image(self):
        self.base_get_image()
    #判断添加收款按钮存在
    def page_is_add_receipt_success(self):
        return self.base_element_is_exist(data[12]["type"], data[12]["element"])

    #组合业务方法
    def voyage_Manager_Total_Add_Settlement_receipt(self,voyage_no,Collection_Serial_Number,Voucher_flow_amount,Name_receiver):
        sleep(3)
        self.page_click_settlement()
        sleep(4)
        self.page_click_checkorder()
        sleep(2)
        self.page_click_voyage(voyage_no)
        sleep(2)
        self.page_click_search()
        sleep(2)
        self.page_click_order_detail()
        sleep(2)
        self.page_click_receipt_manager()
        sleep(2)
        self.page_click_add_receipt()
        sleep(2)
        self.page_click_Collection_Serial_Number(Collection_Serial_Number)
        sleep(2)
        self.page_click_Receipt_Voucher()
        sleep(2)
        self.page_click_Voucher_flow_amount(Voucher_flow_amount)
        sleep(2)
        self.page_click_Name_receiver(Name_receiver)
        sleep(2)
        self.page_click_confirm()
        sleep(2)


# if __name__=='__main__':
#     login=PageLogin()
