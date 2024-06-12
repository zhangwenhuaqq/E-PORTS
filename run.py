import os
import pytest
import time
from tools.email_send import EmailHandler

if __name__ == '__main__':
    pytest.main()
    time.sleep(5)
    # os.system("allure generate ./allure_reports -o ./allure_results --clean")
    # time.sleep(5)
    # EmailHandler().send_email()
