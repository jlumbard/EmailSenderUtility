import requests
import smtplib


class EmailSenderUtility:

    @staticmethod
    def send_email( recipient, subject, body):
        gmail_user = ""; #FILLINHERE
        gmail_pwd = ""; #FILLINHERE
        FROM = gmail_user
        TO = recipient 
        SUBJECT = subject
        TEXT = body

        
        # Prepare actual message
        BODY = '\r\n'.join(['To: %s' % TO,
                        'From: %s' % gmail_user,
                        'Subject: %s' % SUBJECT,
                        '', TEXT])
        
        
        try:
            server = smtplib.SMTP('smtp.gmail.com:587') #start smtp server on port 587
            server.ehlo()
            server.starttls()
            server.login(gmail_user, gmail_pwd) #login to gmail server
            server.sendmail(FROM, TO, BODY) #actually perform sending of mail
            server.quit() #end server
            print ('[+]Successfully sent email notification') #alert user mail was sent
        except:
            print ("[-]Failed to send notification email, ")
