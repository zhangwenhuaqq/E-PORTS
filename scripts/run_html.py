#unittest报告使用
import time
import  unittest
from tools.HTMLTestRunner import HTMLTestRunner

#定义测试套件
suit = unittest.defaultTestLoader.discover("", pattern="test_*.py")
#定义报告存放路径及文件名称
report_dir = "../report/report{}.html".format(time.strftime("%Y_%m_%d %H_M_S"))
#获取报告文件流并执行
with open(report_dir,"wb") as f:
    HTMLTestRunner(stream=f,verbosity=2,title="E-PORTS项目Web端自动化测试报告",description="操作系统 win11").run(suit)