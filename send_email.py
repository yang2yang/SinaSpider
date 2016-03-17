# encoding=utf-8
# date:2016-03-18
# I don't have use this moudle before,so I use this to learn how to send email.

from email.mime.text import MIMEText
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

# 输入Email地址和口令:
#from_addr = raw_input('From: ')
from_addr = 'qingliding@gmail.com'
#password = raw_input('Password: ')
password = 'd197753119'
# 输入SMTP服务器地址:
#smtp_server = raw_input('SMTP server: ')
smtp_server = 'smtp.gmail.com'
# 输入收件人地址:
#to_addr = raw_input('To: ')
to_addr = '197753119@qq.com'

import smtplib
server = smtplib.SMTP(smtp_server, 587) # SMTP协议默认端口是25
server.starttls()
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
