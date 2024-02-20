import pytest
from tools.get_path import get_file_path
from tools.get_yaml import get_read
from tools.get_log import GetLogger
from page.page_change_role import PageChangeRole

log = GetLogger.get_logger()

@pytest.mark.parametrize("indata", get_read(get_file_path('scripts_data', 'change_role.yaml')))
def test_change_role(driver, indata):
    # 调用询价方法
    change_Role = PageChangeRole(driver)
    change_Role.changeRole()
    if indata["success"]:
        try:
            # 判断航程号存在
            assert change_Role.page_is_Voyage_NO_success()
            log.info("成功切换角色至航管")
        except Exception as e:
            log.error(e)
            # 截图
            log.page_get_image()
    else:
        try:
            pass
        except Exception as e:
            log.error(e)
            # 截图
            log.base_get_image()


if __name__ == '__name__':
    pytest.main()
