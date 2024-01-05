import page
from base.base import Base

class PageInquery(Base):
    #点击订单管理按钮
    def page_order_manager_list(self):
        self.base_click(page.order_manager_list)
    #点击发布询价按钮
    def page_add_inquery(self):
        self.base_click(page.add_inquery)
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
    def add_inquery(self):
        self.page_order_manager_list()
        self.page_add_inquery()



# if __name__=='__main__':
#     login=PageLogin()
