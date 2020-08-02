import smtplib 
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login("pagaregaurav2019@gmail.com", "9225121626#gbp")
# message to be sent
message = "Your website is not working properly please check your code"    
# sending the mail
s.sendmail("pagaregaurav2019@gmail.com","gauravpagare2001@gmail.com", message)
# terminating the session
s.quit()
