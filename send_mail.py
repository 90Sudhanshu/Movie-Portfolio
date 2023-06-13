import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "kesharwani.sudhanshu1990@gmail.com"
password = "rhbhiefkrkbpohgo"
receiver = "kesharwani.sudhanshu1990@gmail.com"
context = ssl.create_default_context()

msg = '''\
Subject: Sample Movie Portfolio mail
Hi Team,

I hope all is well with you.

PFB details as required.

Thanks!
'''

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, msg)