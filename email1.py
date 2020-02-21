import smtplib

conn = smtplib.SMTP('mail.aksun-tracking.com', 465)
conn.ehlo()
conn.starttls()
conn.login('info@aksun-tracking.com', 'esrakin2002')
