#!/user/bin/env/python3
# -*- coding: utf-8 -*-

'python study file'

__author__ = 'heyu<18781085152@163.com>'

import smtplib
from email.mime.text import MIMEText

class SendEmail(object):

    def __init__(self, subject, text, receivers, sender='18781085152@163.com', senderPwd='hy7785330eu',
                 address='smtp.163.com', port=994):
        self._sender = sender  # 发送送人邮箱地址
        self._senderPwd = senderPwd  # 发送人邮箱密码
        self._address = address  # 用网易邮箱使用 smtp 的地址
        self._port = port  # 网易邮箱端口
        self.subject = subject  # 邮件主题
        self.text = text  # 邮件内容
        self.receivers = receivers  # 接收人邮箱地址,注意是个列表[]

    def sendMail(self):

        #组合发送邮件信息
        message = MIMEText(self.text, 'plain', 'utf-8')
        message['Subject'] = self.subject
        message['From'] = self._sender

        #判断是发给个人还是多个人
        if isinstance(self.receivers,list):
            message['To'] = ','.join(self.receivers)
        else:
            message['To'] = self.receivers

        try:
            smtpObj = smtplib.SMTP_SSL(self._address, self._port)
            smtpObj.login(self._sender, self._senderPwd)
            smtpObj.sendmail(self._sender, self.receivers, message.as_string())
        except smtplib.SMTPException as e:
            print('发送邮件失败，原因是：', e)
        else:
            print('向', message['To'], '发送邮件成功')
        finally:
            smtpObj.quit()

if __name__ == '__main__':
    subject = '1953hello world!!!' #主题
    text = 'python smtp1953' #内容
    receivers = '673123924@qq.com' #接收人
    email = SendEmail(subject, text, receivers)
    email.sendMail()
