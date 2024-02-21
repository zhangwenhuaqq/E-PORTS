import pytest
from configparser import ConfigParser
from base.get_driver import get_driver

@pytest.fixture(scope='session', autouse=True)
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

# def pytest_addoption(parser):
#     parser.addoption("--env", action="store", help="choose env: uat,pro")
#     parser.addini('env', help="choose env: uat,pro")
#
#
# @pytest.fixture(scope='session')
# def env_vars(request):
#     config = request.config
#     cur_env = config.getoption('--env') or  config.getini('env')
#     inifile = config.inifile
#     conf = ConfigParser()
#     conf.read(inifile)
#     variables = {}
#     if conf.has_section('global'):
#         variables.update(conf.items('global'))
#     if conf.has_section(cur_env):
#         variables.update(conf.items(cur_env))
#     return variables
