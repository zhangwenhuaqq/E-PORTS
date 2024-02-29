import pytest
from page.page_change_role import PageChangeRole
from tools.get_path import get_file_path
from tools.get_yaml import get_read
from tools.get_log import GetLogger
from page.page_voyage_manager_operate_agent_bill import PageVoyageManagerOperateAgentBill

log = GetLogger.get_logger()

@pytest.mark.parametrize("indata", get_read(get_file_path('scripts_data', 'voyage_manager_operate_agent_bill.yaml')))
def test_voyage_manager_operate_agent_Bill(driver, indata):
    #切换角色至航管
    indata_role = get_read(get_file_path('scripts_data', 'change_role.yaml'))
    change_Role = PageChangeRole(driver)
    change_Role.changeRole(indata_role[0]["Voyage_Manger"])
    # 调用航管操作子单账单方法
    OperateAgentBill = PageVoyageManagerOperateAgentBill(driver)
    OperateAgentBill.voyage_manager_operate_agent_Bill(indata["reason"])
    if indata["success"]:
        try:
            # 判断服务项变更信息存在
            assert OperateAgentBill.page_is_change_service_success()
            log.info("航管子单账单操作成功")
        except Exception as e:
            log.error(e)
            # 截图
            OperateAgentBill.page_get_image()
    else:
        try:
            pass
        except Exception as e:
            log.error(e)
            # 截图
            OperateAgentBill.base_get_image()


if __name__ == '__name__':
    pytest.main()
