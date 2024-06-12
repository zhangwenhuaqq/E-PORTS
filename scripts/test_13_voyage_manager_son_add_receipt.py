import pytest
from page.page_change_role import PageChangeRole
from tools.get_path import get_file_path
from tools.get_yaml import get_read
from tools.get_log import GetLogger
from page.page_voyage_manager_son_add_receipt import PageVoyageManagerSonAddReceipt

log = GetLogger.get_logger()

@pytest.mark.parametrize("indata", get_read(get_file_path('scripts_data', 'voyage_manager_son_add_receipt.yaml')))
def test_voyage_manager_operate_agent_Bill(driver, indata):
    # #切换角色至航管
    # indata_role = get_read(get_file_path('scripts_data', 'change_role.yaml'))
    # change_Role = PageChangeRole(driver)
    # change_Role.changeRole(indata_role[0]["Voyage_Manger"])
    # 调用航管-结算管理子单添加付款方法
    voyage_add_receipt = PageVoyageManagerSonAddReceipt(driver)
    voyage_add_receipt.voyage_Manager_Son_Add_Settlement_receipt(indata["Name_receiver"],indata["Collection_Serial_Number"])
    if indata["success"]:
        try:
            # 判断添加付款按钮存在
            assert voyage_add_receipt.page_is_add_receipt_success()
            log.info("航管-结算管理子单添加付款成功")
        except Exception as e:
            log.error(e)
            # 截图
            voyage_add_receipt.page_get_image()
    else:
        try:
            pass
        except Exception as e:
            log.error(e)
            # 截图
            voyage_add_receipt.base_get_image()


if __name__ == '__name__':
    pytest.main()
