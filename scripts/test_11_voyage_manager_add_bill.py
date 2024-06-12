import pytest
from page.page_change_role import PageChangeRole
from page.page_voyage_manager_add_bill import PageManagerAddBill
from tools.get_path import get_file_path
from tools.get_yaml import get_read
from tools.get_log import GetLogger

log = GetLogger.get_logger()

@pytest.mark.parametrize("indata", get_read(get_file_path('scripts_data', 'voyage_manager_add_bill.yaml')))
def test_manager_add_bill(driver, indata):
    # #切换至代理角色
    # indata_role = get_read(get_file_path('scripts_data', 'change_role.yaml'))
    # change_Role = PageChangeRole(driver)
    # change_Role.changeRole(indata_role[0]["Ship_Agent"])
    # 调用账单操作方法
    add_bill = PageManagerAddBill(driver)
    add_bill.manager_add_bill(indata["money"])
    if indata["success"]:
        try:
            # 判断“添加服务项”按钮存在
            assert add_bill.page_is_add_service_success()
            log.info("航管成功完成账单操作")
        except Exception as e:
            log.error(e)
            # 截图
            add_bill.page_get_image()
    else:
        try:
            pass
        except Exception as e:
            log.error(e)
            # 截图
            add_bill.base_get_image()


if __name__ == '__name__':
    pytest.main()
