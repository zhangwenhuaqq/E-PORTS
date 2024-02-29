import pytest
from page.page_change_role import PageChangeRole
from tools.get_path import get_file_path
from tools.get_yaml import get_read
from tools.get_log import GetLogger
from page.page_voyage_manager_appoint import PageVoyageManagerAppoint

log = GetLogger.get_logger()

@pytest.mark.parametrize("indata", get_read(get_file_path('scripts_data', 'voyage_manager_appoint.yaml')))
def test_voyage_manager_appoint(driver, indata):
    #切换角色至航管
    indata_role = get_read(get_file_path('scripts_data', 'change_role.yaml'))
    change_Role = PageChangeRole(driver)
    change_Role.changeRole(indata_role[0]["Voyage_Manger"])
    # 调用航管委托方代理
    voyage_manager = PageVoyageManagerAppoint(driver)
    voyage_manager.add_voyage_manager_appoint()
    if indata["success"]:
        try:
            # 判断“已委托”按钮存在
            assert voyage_manager.page_is_appoint_success()
            log.info("航管成功委托代理")
        except Exception as e:
            log.error(e)
            # 截图
            voyage_manager.page_get_image()
    else:
        try:
            pass
        except Exception as e:
            log.error(e)
            # 截图
            voyage_manager.base_get_image()


if __name__ == '__name__':
    pytest.main()
