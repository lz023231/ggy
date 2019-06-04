import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart


def sendMail(Path, name):
    smtp_server = 'smtp.163.com'
    from_mail = '15227001093@163.com'
    mail_pass = "zhao023231"

    to_mail = 'zhaozelei@rdc.gnway.com'

    # 构造MIMEMultipart对象做为根容器
    msg = MIMEMultipart()

    # 邮件的发件人、收件人和主题
    msg["From"] = from_mail
    msg["To"] = to_mail
    msg["Subject"] = Header("自动化测试报告请查收", 'utf-8').encode()

    '''
    #创建正文
    content = MIMEText('测试报告：','txt','utf-8')
    msg.attach(content)
    '''

    # 创建附件对象
    HtmlPart = MIMEApplication(open(Path, 'rb').read())
    HtmlPart.add_header('Content-Disposition', 'attachment', filename=name)
    msg.attach(HtmlPart)

    smtp = smtplib.SMTP_SSL(smtp_server, 465)
    smtp.connect(smtp_server)
    smtp.login(from_mail, mail_pass)
    smtp.sendmail(from_mail, to_mail, msg.as_string())
    smtp.quit()
