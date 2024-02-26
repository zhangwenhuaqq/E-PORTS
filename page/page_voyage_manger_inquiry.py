import page
from base.base_set import Base
from tools.get_yaml import *
from time import sleep
data = get_read(get_file_path('page_data','page_voyage_manger_inquiry.yaml'))

class PageVoyageMangerInquiry(Base):
    #点击航管添加询价
    def page_click_add_inquiry(self):
        self.base_click(data[0]["type"],data[0]["element"])
    #点击选择代理下拉框
    def page_click_add_Agent(self,agent):
        self.select_send(data[1]["type"],data[1]["element"],agent)
    #点击发布询价
    def page_click_send_inquiry(self):
        self.base_click(data[2]["type"],data[2]["element"])
    #点击确认按钮
    def page_click_send_inquiry_confirm(self):
        self.base_click(data[3]["type"],data[3]["element"])
    #点击确认按钮
    def page_click_add_service_confirm(self):
        self.base_click(data[4]["type"],data[4]["element"])
    #点击进入询价详情页
    def page_click_inquery_detial(self):
        self.base_click(data[5]["type"],data[5]["element"])
    #截图
    def page_get_image(self):
        self.base_get_image()
    # 判断“航程号”存在
    def page_is_voyage_no_success(self):
        return self.base_element_is_exist(data[6]["type"], data[6]["element"])

    #组合业务方法
    def add_Page_Voyage_Manger_inquiry(self,agent):
        sleep(4)
        self.page_click_add_inquiry()
        sleep(2)
        self.page_click_add_Agent(agent)
        sleep(2)
        self.page_click_send_inquiry()
        sleep(2)
        self.page_click_send_inquiry_confirm()
        sleep(2)
        self.page_click_add_service_confirm()
        sleep(2)
        self.page_click_inquery_detial()



# if __name__=='__main__':
#     login=PageLogin()
