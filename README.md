# mass_email_by_python
python基于smtplib实现的群发邮件，能够实现邮件密送，密送可能能够解决无效邮件导致的发送失败问题，已经在学校教育邮箱证明可行，但还是得视具体邮箱而定。


运行环境: win10 + python 3.6.7 

运行办法：
1.将待群发的邮件地址存入csv文件，通过代码读入即可；
2.python send_email.py执行代码。

帮同学通过邮件群发调查问卷，研究了一下smtplib群发邮件，解决了群发密送和学校邮箱因无效邮箱而发送失败的问题（可以通过改为密送解决）。
具体说明参考博客：https://blog.csdn.net/yfreedomliTHU/article/details/88196631
