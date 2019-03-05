import smtplib
from email.header import Header
from email.mime.text import MIMEText
import csv
import pandas as pd 

# SMTP Service
mail_host = "smtp.qq.com"               # SMTP server, take QQ as example
mail_user = "1029639150@qq.com"         # user
mail_pass = "rywtxizulcqibeci"             # note:Authorization Code，not password

sender = "1029639150@qq.com"                   # sender email

#get receiver email from cvs file
def get_email():
    with open('test.csv','r') as csvfile:
        reader = csv.reader(csvfile)
        row1 = [row for row in reader]
        data = row1[0]
    print(data)
    print(len(data))
    return data

#write the content and title of your email here! 
def email_content():
    
    title = 'python_email_test'  # title
    content = 'Test success!'    # content of your email
    return title,content



def sendEmail():

    title,content = email_content()
    #receiver = get_email()
    bcc = get_email()  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱,加入bcc实现群发单显

    message = MIMEText(content, 'plain', 'utf-8')  # content, format, encoding
    message['From'] = "{}".format(sender)
    #message['To'] = ",".join(receiver)                 #To:收件人，Cc:抄送，Bcc:密送，不显示地址
    message['Bcc'] = ",".join(bcc)
    message['Subject'] = title

    try:
        smtp_Obj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtp_Obj.login(mail_user, mail_pass)  # 登录验证
        #smtp_Obj.sendmail(sender, receiver, message.as_string())  # 发送
        smtp_Obj.sendmail(sender, bcc, message.as_string())
        print("email send success!")
    except smtplib.SMTPException as e:
        print(e)
        print("error!email send failed!")


if __name__ == '__main__':

    sendEmail()
