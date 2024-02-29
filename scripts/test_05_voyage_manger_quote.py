import pytest

from page.page_change_role import PageChangeRole
from tools.get_path import get_file_path
from tools.get_yaml import get_read
from tools.get_log import GetLogger
from page.page_voyage_manger_quote import PageVoyageMangerQuote

log = GetLogger.get_logger()

@pytest.mark.parametrize("indata", get_read(get_file_path('scripts_data', 'voyage_manger_quote.yaml')))
def test_voyage_manger_quote(driver, indata):
    #切换至航管角色
    indata_role = get_read(get_file_path('scripts_data', 'change_role.yaml'))
    change_Role = PageChangeRole(driver)
    change_Role.changeRole(indata_role[0]["Voyage_Manger"])
    # 调用报价方法
    hc_quote = PageVoyageMangerQuote(driver)
    hc_quote.add_Page_Voyage_Manger_Quote(indata["new_service"])
    if indata["success"]:
        try:
            # 判断“预览”按钮存在
            assert hc_quote.page_is_preiew_success()
            log.info("航管成功报价")
        except Exception as e:
            log.error(e)
            # 截图
            hc_quote.page_get_image()
    else:
        try:
            pass
        except Exception as e:
            log.error(e)
            # 截图
            hc_quote.base_get_image()


if __name__ == '__name__':
    pytest.main()
