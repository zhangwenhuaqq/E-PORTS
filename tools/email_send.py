import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
import logging
import logging.config
from tools.get_log import GetLogger
from tools.get_path import get_file_path

log = GetLogger.get_logger()

class EmailHandler:


    def __init__(self) -> object:
        self.my_sender = '18217555671@163.com'  # 发件人邮箱账号
        self.my_pass = 'ECYNUGJXQGFSUYZK'  # 发件人邮箱密码,此处为授权码
        self.my_user = '18217555671@163.com'  # 收件人邮箱账号，我这边发送给自己

    def email_content(self):
        with open(get_file_path('allure_reports','reports.html'),'r',encoding='utf-8') as f:
            return f.read()

    def send_email(self):

        f = self.email_content()
        ret = True
        try:
            #创建一个带附件的实例
            message = MIMEMultipart()
            msg = MIMEText('测试结果详见附件测试报告', 'plain', 'utf-8')  # 这里面写的是发送的是html
            message['From'] = formataddr(["winson", self.my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            message['To'] = formataddr(["winson", self.my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            message['Subject'] = "E-PORTS WEB端UI自动化测试"  # 邮件的主题，也可以说是标题
            message.attach(msg)  # 邮件正文内容
            #添加附件
            att1 = MIMEText(f, 'html', 'utf-8')
            att1["Content-Type"] = 'application/octet-stream'
            # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
            att1["Content-Disposition"] = 'attachment; filename="WEB_UI_TEST_RESULTS.html"'
            message.attach(att1)
            #发送邮件
            server = smtplib.SMTP_SSL("smtp.163.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
            server.login(self.my_sender, self.my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(self.my_sender, [self.my_user, ], message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            ret = False
            log.info("邮件发送失败")
        log.info("邮件发送成功")

        return ret

if __name__ == '__main__':
    EmailHandler().send_email()