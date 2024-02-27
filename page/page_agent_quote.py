import page
from base.base_set import Base
from tools.get_yaml import *
from time import sleep
data = get_read(get_file_path('page_data','page_agent_quote.yaml'))

class PageAgentQuote(Base):
    #点击删除PortAgentFee服务项
    def page_click_delete_PortAgentFee(self):
        self.base_click(data[0]["type"],data[0]["element"])
    #点击确认删除按钮
    def page_click_delete_ortAgentFee_confirm(self):
        self.base_click(data[1]["type"],data[1]["element"])
    #点击新增服务项
    def page_click_add_service(self):
        self.base_click(data[2]["type"],data[2]["element"])
    #输入新增服务项内容
    def page_input_add_service_text(self,new_service):
        self.base_input(data[3]["type"],data[3]["element"],new_service)
    #点击确认按钮
    def page_click_add_service_confirm(self):
        self.base_click(data[4]["type"],data[4]["element"])
    #点击删除BunkeringAgent服务项
    def page_click_delete_BunkeringAgent(self):
        self.base_click(data[5]["type"],data[5]["element"])
    #点击确认删除按钮
    def page_click_delete_BunkeringAgent_confirm(self):
        self.base_click(data[6]["type"],data[6]["element"])
    #点击Inward Formality编辑按钮
    def page_click_edit_Inward_Formality(self):
        self.base_click(data[7]["type"],data[7]["element"])
    #输入价格
    def page_input_Inward_Formality_price(self,price1):
        self.base_input(data[8]["type"],data[8]["element"],price1)
    #点击确认
    def page_ckick_Inward_Formality_confirm(self):
        self.base_click(data[9]["type"],data[9]["element"])
    #点击Outward Formality编辑按钮
    def page_click_edit_Outward_Formality(self):
        self.base_click(data[10]["type"],data[10]["element"])
    #输入价格
    def page_input_Outward_Formality_price(self,price2):
        self.base_input(data[11]["type"],data[11]["element"],price2)
    #点击确认
    def page_click_Outward_Formality_confirm(self):
        self.base_click(data[12]["type"],data[12]["element"])
    #点击删除”新增服务项“按钮
    def page_click_delete_new_service(self):
        self.base_click(data[18]["type"],data[18]["element"])
    #点击确认按钮
    def page_click_delete_new_service_confirm(self):
        self.base_click(data[19]["type"], data[19]["element"])
    #预览报价
    def page_click_preview(self):
        self.base_click(data[13]["type"],data[13]["element"])
    #取消预览报价
    def page_click_close_preview(self):
        self.base_click(data[14]["type"],data[14]["element"])
    #立即报价
    def page_click_quote_now(self):
        self.base_click(data[15]["type"],data[15]["element"])
    #弹窗“继续”
    def page_click_contiune(self):
        self.base_click(data[16]["type"],data[16]["element"])
    #点击”立即报价“提交后的”确认“按钮
    def page_click_contiune_confirm(self):
        self.base_click(data[20]["type"],data[20]["element"])
    #截图
    def page_get_image(self):
        self.base_get_image()
    # 判断“已报价”按钮存在
    def page_is_quote_success(self):
        return self.base_element_is_exist(data[17]["type"], data[17]["element"])

    #组合业务方法
    def add_Page_Agent_Quote(self,new_service,price1,price2):
        sleep(5)
        self.page_click_delete_PortAgentFee()
        sleep(2)
        self.page_click_delete_ortAgentFee_confirm()
        sleep(2)
        self.page_click_add_service()
        sleep(2)
        self.page_input_add_service_text(new_service)
        sleep(2)
        self.page_click_add_service_confirm()
        sleep(2)
        self.page_click_delete_BunkeringAgent()
        sleep(2)
        self.page_click_delete_BunkeringAgent_confirm()
        sleep(2)
        self.page_click_edit_Inward_Formality()
        self.scroll_foot(400)
        sleep(2)
        self.page_input_Inward_Formality_price(price1)
        sleep(2)
        self.page_ckick_Inward_Formality_confirm()
        sleep(2)
        self.page_click_edit_Outward_Formality()
        sleep(2)
        self.page_input_Outward_Formality_price(price2)
        sleep(2)
        self.page_click_Outward_Formality_confirm()
        sleep(2)
        self.page_click_delete_new_service()
        sleep(2)
        self.page_click_delete_new_service_confirm()
        sleep(2)
        self.page_click_preview()
        sleep(2)
        self.page_click_close_preview()
        sleep(2)
        self.page_click_quote_now()
        sleep(2)
        self.page_click_contiune()
        sleep(2)
        self.page_click_contiune_confirm()


# if __name__=='__main__':
#     login=PageLogin()
