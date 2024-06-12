import pytest
from page.page_change_role import PageChangeRole
from tools.get_path import get_file_path
from tools.get_yaml import get_read
from tools.get_log import GetLogger
from page.page_voyage_manager_add_receipt import PageVoyageManagerAddReceipt

log = GetLogger.get_logger()
#读取航程号
get_data = get_read(get_file_path('page_data', 'test_data.yaml'))
record = get_data['记录订单号']

@pytest.mark.parametrize("indata", get_read(get_file_path('scripts_data', 'voyage_manager_add_receipt.yaml')))
def test_voyage_manager_operate_agent_Bill(driver, indata):
    # #切换角色至航管
    # indata_role = get_read(get_file_path('scripts_data', 'change_role.yaml'))
    # change_Role = PageChangeRole(driver)
    # change_Role.changeRole(indata_role[0]["Voyage_Manger"])
    # 调用航管操作子单账单方法
    voyage_add_receipt = PageVoyageManagerAddReceipt(driver)
    voyage_add_receipt.voyage_Manager_Add_Settlement_receipt(record,indata["Collection_Serial_Number"],indata["Voucher_flow_amount"],indata["Name_receiver"])
    if indata["success"]:
        try:
            # 判断添加收款按钮存在
            assert voyage_add_receipt.page_is_add_receipt_success()
            log.info("航管子单账单操作成功")
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
