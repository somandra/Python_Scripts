import smtplib
import config

def send_email(subject, message):
        try:
                server = smtplib.SMTP('smtp.gmail.com',587)
                server.ehlo()
                server.starttls()
                server.login(config.email_add,config.pass_word)
                message = 'Subject:{}\n\n{}'.format(subject,message)
                server.sendmail(config.email_add,config.email_add,message)
                server.quit()
                print("Email successfully sent!!")
        except:
                print("OOPS!! something went wrong\nError in sending Email")




subject = input("enter subject of your message::        ")
message = input("Enter mesaage you want to send::       ")

send_email(subject,message)
