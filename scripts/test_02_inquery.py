import pytest
from tools.get_path import get_file_path
from tools.get_yaml import get_read
from tools.get_log import GetLogger
from page.page_inquery import PageInquery

log = GetLogger.get_logger()

@pytest.mark.parametrize("indata", get_read(get_file_path('scripts_data', 'inquery.yaml')))
def test_inquery(driver, indata):
    # 调用询价方法
    inquery = PageInquery(driver)
    inquery.add_inquery(indata["port"], indata["service"], indata["front_prot"])
    if indata["success"]:
        try:
            # 判断"询价中"是否存在
            assert inquery.page_is_inquery_success()
            log.info("成功发布询价")
        except Exception as e:
            log.error(e)
            # 截图
            inquery.page_get_image()
    else:
        try:
            pass
        except Exception as e:
            log.error(e)
            # 截图
            inquery.base_get_image()


if __name__ == '__name__':
    pytest.main()
