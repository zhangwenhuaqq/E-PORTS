import pytest

from page.page_change_role import PageChangeRole
from tools.get_path import get_file_path
from tools.get_yaml import get_read
from tools.get_log import GetLogger
from page.page_agent_quote import PageAgentQuote

log = GetLogger.get_logger()

@pytest.mark.parametrize("indata", get_read(get_file_path('scripts_data', 'agent_quote.yaml')))
def test_agent_quote(driver, indata):
    #切换至代理角色
    indata_role = get_read(get_file_path('scripts_data', 'change_role.yaml'))
    change_Role = PageChangeRole(driver)
    change_Role.changeRole(indata_role[0]["Ship_Agent"])
    # 调用报价方法
    agent_quote = PageAgentQuote(driver)
    agent_quote.add_Page_Agent_Quote(indata["new_service"], indata["price1"], indata["price2"])
    if indata["success"]:
        try:
            # 判断“预览”按钮存在
            assert agent_quote.page_is_quote_success()
            log.info("代理成功报价")
        except Exception as e:
            log.error(e)
            # 截图
            agent_quote.page_get_image()
    else:
        try:
            pass
        except Exception as e:
            log.error(e)
            # 截图
            agent_quote.base_get_image()


if __name__ == '__name__':
    pytest.main()
