#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime
import smtplib
import time
from email.mime.text import MIMEText
from email.utils import formataddr


#用法：
# mail  = MailUtil()
# ret = mail.setUser('596552206@qq.com').setTitle('nihaowa!').setContent('zheshicontent!').send()
# print('Success' if ret else 'Error')


class MailUtil:
    __my_sender = '3340333414@qq.com'  # 发件人邮箱账号
    __my_pass = 'cyqamwgwljorchea'  # 发件人邮箱密码
    __title = ''
    __content = ''
    __user = ''
    __html = '''
    <table class="body" style="width: 100%; background-color: #fff;" width="100%" bgcolor="#fff"><tbody><tr>
    <td style="vertical-align: top;" valign="top"></td>
    <td class="container" style="vertical-align: top; display: block; max-width: 580px; width: 580px; margin: 0 auto; padding: 24px;" width="580" valign="top">
      <div class="content" style="display: block; max-width: 580px; margin: 0 auto;">
		
		<div class="header" style="width: 100%; padding-top: 8px; padding-bottom: 8px; margin-bottom: 16px; border-bottom-width: 1px; border-bottom-color: #eee; border-bottom-style: solid;">
  			<table style="width: 100%;" width="100%">
   				<tbody>
   					<tr>
      				<td style="vertical-align: top;" valign="top">
        				<a href="https://chng.fun" style="color: #0d1740; text-decoration: none;" rel="noopener" target="_blank">
          				<h2>CHNG · 小柏</h2>
        				</a>
      				</td>
    				</tr>
  				</tbody>
  			</table>
		</div>

		<div class="mb-2" style="margin-bottom: 8px !important;">
		  <div class="h2 lh-condensed" style="font-size: 24px !important; font-weight: 600 !important; line-height: 1.25 !important;">
		    {}
		  </div>
		</div>

		<div class="pb-2" style="padding-bottom: 8px !important;">
		  <div class="mb-3" style="margin-bottom: 16px !important;">
		    <p>{}</p>
		  </div>
		</div>

        <div class="footer" style="clear: both; width: 100%;">
          <hr class="footer-hr" style="height: 0; overflow: visible; margin-top: 24px; border-top-color: #e1e4e8; border-top-style: solid; color: #959da5; font-size: 12px; line-height: 18px; margin-bottom: 30px; border-width: 1px 0 0;">
          <p class="footer-text" style="font-weight: normal; color: #959da5; font-size: 12px; line-height: 18px; margin: 0 0 15px;">不要回复！不要回复！不要回复！</p>
        </div>

     </div>
   </td>
   <td style="vertical-align: top;" valign="top"></td>
</tr></tbody></table>
    
    '''


    def setTitle(self,title):
        self.__title = title;
        return self


    def setContent(self,content):
        self.__content = content
        return self


    def setUser(self,user):
        self.__user = user
        return self


    def send(self):
        if self.__user == '':
            return False
        if self.__title == '':
            return False
        if self.__content == '':
            self.__content = self.__title
        ret = True
        try:
            msg = MIMEText(self.__html.format(self.__title,self.__content), 'html', 'utf-8')
            msg['From'] = formataddr(["小柏", self.__my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To'] = formataddr(["亲爱的陌生人", self.__user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = self.__title  # 邮件的主题，也可以说是标题
            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
            server.login(self.__my_sender, self.__my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(self.__my_sender, [self.__user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            ret = False
        return ret