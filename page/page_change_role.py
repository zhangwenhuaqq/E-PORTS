import page
from base.base import Base
from tools.get_path import get_file_path
from tools.get_yaml import *
import time
data = get_read(get_file_path('page_data','page_change_role.yaml'))

class PageChangeRole(Base):
    #点击昵称
    def page_click_nickname(self):
        self.base_click(data[0]["type"],data[0]["element"])
    #点击切换角色
    def page_click_change_role(self):
        self.base_click(data[1]["type"],data[1]["element"])
    #点击需要切换的角色
    def page_click_role(self,role):
        #航管
        if role == "Voyage Manger":
            self.base_click(data[2]["type"],data[2]["element"])
        #委托
        if role == "Ship Owner":
            self.base_click(data[5]["type"],data[5]["element"])
        #代理
        if role == "Ship Agent":
            self.base_click(data[6]["type"],data[6]["element"])
        #加油商
        if role == "Supplier":
            self.base_click(data[7]["type"],data[7]["element"])
    #点击我们开始吧
    def page_click_we_start(self):
        self.base_click(data[3]["type"],data[3]["element"])
    #截图
    def page_get_image(self):
        self.base_get_image()
    # 判断详情页的航程号存在
    def page_is_Voyage_NO_success(self):
        return self.base_element_is_exist(data[4]["type"], data[4]["element"])

    #组合业务方法
    def changeRole(self,role):
        self.page_click_nickname()
        time.sleep(1)
        self.page_click_change_role()
        time.sleep(1)
        self.page_click_role(role)
        time.sleep(1)
        self.page_click_we_start()


# if __name__=='__main__':
#     login=PageLogin()
