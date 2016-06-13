'''
How to send email use python?
'''
def send_email():
    import smtplib
    server = smtplib.SMTP('localhost')
    fromEmail = 'fjqp@Outlook.com'
    toEmail = 'fjqp@outlook.com'
    msg = 'I love you baby'
    server.sendmail(fromEmail,toEmail,msg)


