import page
from base.base_set import Base
from tools.get_path import get_file_path
from tools.get_yaml import *
from time import sleep
data = get_read(get_file_path('page_data','page_agent_operate_service.yaml'))

class PageAgentOperateService(Base):
    #点击服务项后的“详情”按钮
    def page_click_service_detail(self):
        self.base_click(data[0]["type"],data[0]["element"])
    #点击弹窗“知道了”
    def page_click_I_konw(self):
        self.base_click(data[1]["type"],data[1]["element"])
    #再次点击服务项后的“详情”按钮
    def page_click_service_detail_again(self):
        self.base_click(data[0]["type"],data[0]["element"])
    #2点击“提交”按钮
    def page_click_submit(self):
        self.base_click(data[2]["type"],data[2]["element"])
    #截图
    def page_get_image(self):
        self.base_get_image()
    #判断服务项变更信息正确
    def page_is_service_change_success(self):
        return self.base_element_is_exist(data[3]["type"], data[3]["element"])

    #组合业务方法
    def agent_operate_service(self):
        sleep(3)
        self.page_click_service_detail()
        sleep(2)
        self.page_click_I_konw()
        sleep(2)
        self.page_click_service_detail_again()
        sleep(2)
        self.page_click_submit()
        sleep(5)

# if __name__=='__main__':
#     login=PageLogin()
