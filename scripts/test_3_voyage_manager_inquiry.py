import pytest

from page.page_change_role import PageChangeRole
from page.page_voyage_manger_inquiry import PageVoyageMangerInquiry
from tools.get_path import get_file_path
from tools.get_yaml import get_read
from tools.get_log import GetLogger


log = GetLogger.get_logger()

@pytest.mark.parametrize("indata", get_read(get_file_path('scripts_data', 'voyage_manger_inquiry.yaml')))
def test_voyage_manger_inquiry(driver, indata):
    #切换至航管角色
    indata_role = get_read(get_file_path('scripts_data', 'change_role.yaml'))
    change_Role = PageChangeRole(driver)
    change_Role.changeRole(indata_role[0]["Voyage_Manger"])
    # 调用航管询价方法
    hc_inquiry = PageVoyageMangerInquiry(driver)
    hc_inquiry.add_Page_Voyage_Manger_inquiry(indata["agent"])
    if indata["success"]:
        try:
            # 判断航程号存在
            assert hc_inquiry.page_is_voyage_no_success()
            log.info("航管成功询价")
        except Exception as e:
            log.error(e)
            # 截图
            hc_inquiry.page_get_image()
    else:
        try:
            pass
        except Exception as e:
            log.error(e)
            # 截图
            hc_inquiry.base_get_image()


if __name__ == '__name__':
    pytest.main()
