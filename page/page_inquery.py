import page
from base.base_set import Base
from tools.get_path import get_file_path
from tools.get_yaml import *
from time import sleep
data = get_read(get_file_path('page_data','page_inquery.yaml'))

class PageInquery(Base):
    #点击订单管理按钮
    def page_order_manager_list(self):
        self.base_click(data[0]["type"],data[0]["element"])
    #点击发布询价按钮
    def page_add_inquery(self):
        self.base_click(data[1]["type"],data[1]["element"])
    #选择船舶
    def page_add_ship(self):
        self.base_click(data[2]["type"],data[2]["element"])
        self.base_click(data[3]["type"],data[3]["element"])
    #选择港口
    def page_click_port(self,port):
        self.select_send(data[4]["type"],data[4]["element"],port)
    #选择服务类型
    def page_click_service(self,service):
        self.select_send(data[5]["type"],data[5]["element"],service)
    #选择上一港口
    def page_click_front_port(self,front_prot):
        self.select_send(data[6]["type"],data[6]["element"],front_prot)
    #点击时间选择框
    def page_click_time(self):
        self.base_click(data[7]["type"],data[7]["element"])
        self.base_click(data[8]["type"],data[8]["element"])
    #选择代理-航管
    def page_click_agent(self):
        self.base_click(data[9]["type"],data[9]["element"])
    #点击发布询价
    def page_click_inquery(self):
        self.base_click(data[10]["type"],data[10]["element"])
    #点击弹窗中的确定按钮
    def page_click_confirm(self):
        self.base_click(data[11]["type"],data[11]["element"])
    #点击进入询价单详情
    def page_click_inquery_detail(self):
        self.base_click(data[12]["type"],data[12]["element"])
    #判断是否发布成功(检查首页"询价中"存在)
    def page_is_inquery_success(self):
        return self.base_element_is_exist(data[14]["type"],data[14]["element"])
    #获取订单号文本
    def page_NO(self):
        No = self.base_get_text(data[13]["type"],data[13]["element"])
        #组合成字典存入一个变量
        extract_data = {data[13]["info"]: No}
        return extract_data
    #记录订单号到yaml中
    def page_record_NO(self):
        return get_write(get_file_path('page_data','test_data.yaml'),self.page_NO())
    #截图
    def page_get_image(self):
        self.base_get_image()

    #组合业务方法
    def add_inquery(self,port,service,front_prot):
        sleep(3)
        self.page_order_manager_list()
        sleep(3)
        self.page_add_inquery()
        sleep(2)
        self.page_add_ship()
        #sleep(1)
        self.page_click_port(port)
        #sleep(1)
        self.page_click_service(service)
        #sleep(1)
        self.page_click_front_port(front_prot)
        #sleep(1)
        self.page_click_time()
        sleep(1)
        self.page_click_agent()
        sleep(1)
        self.page_click_inquery()
        sleep(1)
        self.page_click_confirm()
        sleep(1)
        self.page_click_inquery_detail()
        sleep(1)
        self.page_NO()
        sleep(1)
        self.page_record_NO()




# if __name__=='__main__':
#     login=PageLogin()
