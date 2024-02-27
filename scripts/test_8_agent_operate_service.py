import pytest
from page.page_change_role import PageChangeRole
from tools.get_path import get_file_path
from tools.get_yaml import get_read
from tools.get_log import GetLogger
from page.page_agent_operate_service import PageAgentOperateService

log = GetLogger.get_logger()

@pytest.mark.parametrize("indata", get_read(get_file_path('scripts_data', 'agent_operate_service.yaml')))
def test_agent_operate_service(driver, indata):
    #切换角色至代理
    indata_role = get_read(get_file_path('scripts_data', 'change_role.yaml'))
    change_Role = PageChangeRole(driver)
    change_Role.changeRole(indata_role[0]["Ship_Agent"])
    # 调用操作服务项方法
    Ship_Agent = PageAgentOperateService(driver)
    Ship_Agent.agent_operate_service()
    if indata["success"]:
        try:
            # 判断“预览”按钮存在
            assert Ship_Agent.page_is_service_change_success()
            log.info("委托方成功委托订单")
        except Exception as e:
            log.error(e)
            # 截图
            Ship_Agent.page_get_image()
    else:
        try:
            pass
        except Exception as e:
            log.error(e)
            # 截图
            Ship_Agent.base_get_image()


if __name__ == '__name__':
    pytest.main()
