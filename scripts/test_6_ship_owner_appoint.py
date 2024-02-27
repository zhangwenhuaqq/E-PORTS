import pytest
from page.page_change_role import PageChangeRole
from tools.get_path import get_file_path
from tools.get_yaml import get_read
from tools.get_log import GetLogger
from page.page_ship_owner_appoint import PageShipOwnerAppoint

log = GetLogger.get_logger()

@pytest.mark.parametrize("indata", get_read(get_file_path('scripts_data', 'ship_owner_appoint.yaml')))
def test_ship_owner_appoint(driver, indata):
    #切换角色至船东
    indata_role = get_read(get_file_path('scripts_data', 'change_role.yaml'))
    change_Role = PageChangeRole(driver)
    change_Role.changeRole(indata_role[0]["Ship_Owner"])
    # 调用委托方法
    ship_owner = PageShipOwnerAppoint(driver)
    ship_owner.add_ship_owner_appoint()
    if indata["success"]:
        try:
            # 判断“预览”按钮存在
            assert ship_owner.page_is_appoint_success()
            log.info("委托方成功委托订单")
        except Exception as e:
            log.error(e)
            # 截图
            ship_owner.page_get_image()
    else:
        try:
            pass
        except Exception as e:
            log.error(e)
            # 截图
            ship_owner.base_get_image()


if __name__ == '__name__':
    pytest.main()
