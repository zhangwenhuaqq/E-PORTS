from base.base import Base
import page

class PageLogin(Base):
    #切换至密码登录
    def page_change_password(self):
        self.base_click(page.login_change_password)
    #切换至邮箱登录
    def page_change_mail(self):
        self.base_click(page.login_change_mail)
    #输入登录邮箱账号
    def page_input_mail(self,login_mail):
        self.base_input(page.login_input_mail,login_mail)
    #输入登录密码
    def page_input_password(self,pwd):
        self.base_input(page.login_input_password,pwd)
    #点击登录按钮
    def page_click_login_button(self):
        self.base_click(page.login_click_login_button)
    #点击用户昵称
    def page_click_login_nickname(self):
        self.base_click(page.login_nickname)
    #点击退出登录
    def page_click_login_logout(self):
        self.base_click(page.login_logout)
    #确定退出登录
    def page_click_login_logout_bt(self):
        self.base_click(page.login_logout_bt)
    #截图
    def page_get_image(self):
        self.base_get_image()
    #判断是否成功登录(检查首页"用户昵称"存在)
    def page_is_login_success(self):
        return self.base_element_is_exist(page.login_nickname)
    #判断是否成功退登(检查登录页"密码登录"存在)
    def page_is_logout_success(self):
        return self.base_element_is_exist(page.login_change_password)

    #组合业务方法
    def page_login(self,login_mail,pwd):
        self.page_change_password()
        self.page_change_mail()
        self.page_input_mail(login_mail)
        self.page_input_password(pwd)
        self.page_click_login_button()


if __name__=='__main__':
    login=PageLogin()
