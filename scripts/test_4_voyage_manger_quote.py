import pytest
from tools.get_path import get_file_path
from tools.get_yaml import get_read
from tools.get_log import GetLogger
from page.page_voyage_manger_quote import PageVoyageMangerQuote

log = GetLogger.get_logger()

@pytest.mark.parametrize("indata", get_read(get_file_path('scripts_data', 'voyage_manger_quote.yaml')))
def test_voyage_manger_quote(driver, indata):
    # 调用报价方法
    hc_quote = PageVoyageMangerQuote(driver)
    hc_quote.add_Page_Voyage_Manger_Quote(indata["new_service"], indata["price1"], indata["price2"])
    if indata["success"]:
        try:
            # 判断“预览”按钮存在
            assert hc_quote.page_is_preiew_success()
            log.info("航管成功报价")
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
