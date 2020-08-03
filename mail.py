  
import smtplib 
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login("sender_email", "password")
# message to be sent
message = "Your website is not working properly please check your code"    
# sending the mail
s.sendmail("sender_email","recivers_email", message)
# terminating the session
s.quit()
