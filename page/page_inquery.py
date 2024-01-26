import page
from base.base import Base
from tools.get_path import get_file_path
from tools.get_yaml import get_read

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
    #截图
    def page_get_image(self):
        self.base_get_image()

#     #判断是否成功登录(检查首页"用户昵称"存在)
#     def page_is_login_success(self):
#         return self.base_element_is_exist(page.login_nickname)
#     #判断是否成功退登(检查登录页"密码登录"存在)
#     def page_is_logout_success(self):
#         return self.base_element_is_exist(page.login_nickname)
#
    #组合业务方法
    def add_inquery(self,port,service,front_prot):
        self.page_order_manager_list()
        self.page_add_inquery()
        self.page_add_ship()
        self.page_click_port(port)
        self.page_click_service(service)
        self.page_click_front_port(front_prot)
        self.page_click_time()
        self.page_click_agent()
        self.page_click_inquery()
        self.page_click_confirm()
        self.page_click_inquery_detail()



# if __name__=='__main__':
#     login=PageLogin()
