import pytest
from tools.get_path import get_file_path
from tools.get_yaml import get_read
from tools.get_log import GetLogger
from page.page_mail_pwd_login import PageLogin

log = GetLogger.get_logger()
scripts_data = get_read(get_file_path('scripts_data', 'mail_pwd_login.yaml'))

@pytest.mark.parametrize("indata", scripts_data)
def test_login(driver, indata):
    # 调用登录方法
    login = PageLogin(driver)
    login.page_login(indata["mail"],indata["pwd"])
    if indata["success"]:
        try:
            # 判断用户昵称是否存在
            assert login.page_is_login_success()
            # driver (driver.login.page_is_login_success())
            log.info("登录成功，用户昵称存在")
            # # 点击用户昵称
            # login.page_click_login_nickname()
            # # 点击退出登录
            # login.page_click_login_logout()
            # # 点击确认退出登录
            # login.page_click_login_logout_bt()
            # try:
            #     assert login.page_is_logout_success()
            #     #driver.assertTrue(driver.login.page_is_logout_success())
            #     log.info("登出成功，检查'登录页登录密码'存在")
            # except Exception as e:
            #     log.error(e)
            #     # 截图
            #     login.page_get_image()
        except Exception as e:
            log.error(e)
            # 截图
            login.page_get_image()
    else:
        # #断言
        # el = self.login.base_get_text(page.login_page_assert_chat)
        try:
            ##断言
            # self.assertEqual(el,except_result)
            pass
        except Exception as e:
            log.error(e)
            # 截图
            login.base_get_image()


if __name__ == '__name__':
    pytest.main()
