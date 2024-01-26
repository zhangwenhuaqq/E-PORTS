from base.base import Base
import page
from tools.get_path import get_file_path
from tools.get_yaml import get_read

data = get_read(get_file_path('page_data','page_mail_pwd_login.yaml'))

class PageLogin(Base):

    #切换至密码登录
    def page_change_password(self):
        self.base_click(data[0]["type"],data[0]["element"])
    #切换至邮箱登录
    def page_change_mail(self):
        self.base_click(data[1]["type"],data[1]["element"])
    #输入登录邮箱账号
    def page_input_mail(self,login_mail):
        self.base_input(data[2]["type"],data[2]["element"],login_mail)
    #输入登录密码
    def page_input_password(self,pwd):
        self.base_input(data[3]["type"],data[3]["element"],pwd)
    #点击登录按钮
    def page_click_login_button(self):
        self.base_click(data[4]["type"],data[4]["element"])
    #点击用户昵称
    def page_click_login_nickname(self):
        self.base_click(data[5]["type"],data[5]["element"])
    #点击退出登录
    def page_click_login_logout(self):
        self.base_click(data[6]["type"],data[6]["element"])
    #确定退出登录
    def page_click_login_logout_bt(self):
        self.base_click(data[7]["type"],data[7]["element"])
    #截图
    def page_get_image(self):
        self.base_get_image()
    #判断是否成功登录(检查首页"用户昵称"存在)
    def page_is_login_success(self):
        return self.base_element_is_exist(data[5]["type"],data[5]["element"])
    #判断是否成功退登(检查登录页"密码登录"存在)
    def page_is_logout_success(self):
        return self.base_element_is_exist(data[0]["type"],data[0]["element"])
    #滑块
    def page_sw(self):
        self.sw(data[8]["type"],data[8]["element"])
    #组合业务方法
    def page_login(self,login_mail,pwd):
        self.page_change_password()
        self.page_change_mail()
        self.page_input_mail(login_mail)
        self.page_input_password(pwd)
        self.page_click_login_button()
        if self.base_element_is_exist(data[8]["type"],data[8]["element"]):
            self.page_sw()
            self.page_click_login_button()
        else:
            pass


if __name__=='__main__':
    login=PageLogin()
