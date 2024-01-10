一.框架介绍
1.框架采用PO模式
2.python+pytest+allure
二、框架各模块介绍
1.base
get_driver.py
(1)生成driver
(2)绕过阿里云滑块验证
base.py
(1)基类，元素基本操作方法封装
2.page
(1)_init_.py
保存各业务模块的page元素
(2)page_*
按照业务模块的page独立封装
3.scripts
(1)test_*.py
根据业务模块实现的具体测试用例
(2)conftest.py
@pytest.fixture() 装饰器，实现用例的前后置，全局可直接调用
4.scripts_data.py
(1)业务模块中使用的测试数据
5.tools
(1)email_send.py
发送邮件封装
(2)get_log.py
log封装，控制台和log模块分别记录，可只输出error或者info日志
(3)get_path.py
文件路径方法封装
(4)get_yaml.py
读、写yaml文件方法封装
6.log
操作日志记录
7.image
失败用例截图
8.allure_results/allure_reports
测试报告
9.pytest.ini
pytest核心配置文件
10.run.py
执行文件
11.requirements.txt
存入报名，可以批量安装 pip install -r requirements.txt

二、操作手册

