from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from socket import fromshare
from pathlib import Path

acc = 'katyhudson1025@gmail.com'
passwords = 'telittcsxsevcvox'


msg = MIMEMultipart()
msg.attach(MIMEText("Warning!! Here comes a stranger!!")) # 郵件內文
msg.attach(MIMEImage(Path("C://Users//mnetlab//Downloads//ccproj//12.jpg").read_bytes()))# 加入圖片
msg['Subject'] = '門禁警告'            # 郵件標題
msg['From'] = 'Door'                  # 暱稱或是 email
msg['To'] = 'perrylin315@gapp.nthu.edu.tw'   # 收件人 email

#msg['Cc'] = 'oxxo.studio@gmail.com, XXX@gmail.com'   # 副本收件人 email ( 開頭的 C 大寫 )
#msg['Bcc'] = 'oxxo.studio@gmail.com, XXX@gmail.com'  # 密件副本收件人 email


smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()
smtp.login(acc,passwords)
status = smtp.send_message(msg) 

if status == {}:
    print('Email sent successfully')
else:
    print('Email sent failed')
smtp.quit()



