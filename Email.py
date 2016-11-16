# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr


# 第三方SMTP服务
mail_host = 'smtp.qq.com'
mail_user = '843113495@qq.com'
mail_pass = 'vrfmpxtdrysibdhh'

sender = '843113495@qq.com'
# receivers = ['852597034@qq.com', '843113495@qq.com']


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = input('From:')
to_addr = input('To:')
msg = MIMEText('python 邮件测试', 'plain', 'utf-8')
# 因为如果包含中文，需要通过Header对象进行编码。
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)

Subject = 'python SMTP 测试'
msg['Subject'] = Header('来自smtp的问候...', 'utf-8').encode()

try:
    smtpObj = smtplib.SMTP_SSL(mail_host, 465)
    # 可以打印出和SMTP服务器交互的所有信息
    smtpObj.set_debuglevel(1)
    smtpObj.login(from_addr, mail_pass)
    # 邮件正文是一个str，as_string()把MIMEText对象变成str
    smtpObj.sendmail(from_addr, [to_addr], msg.as_string())
    smtpObj.quit()
    print('邮件发送成功')
except smtplib.SMTPException:
    print('Error:无法发送邮件')
