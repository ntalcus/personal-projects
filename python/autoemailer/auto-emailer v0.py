import smtplib
import csv

server = smtplib.SMTP('smtp.gmail.com', 587)
sever.starttls()
server.login('shesec@bsc.coop', '') #add password

class Resident(object): #this is to store the resident info as a class to be accessed later

    def __init__(self, name, email, room):
        self.name = str(name)
        self.email = str(email)
        self.room = int(room)

email_list =

for resident in email_list:
    msg = "{0.name}, room {0.room}, you have mail/packages.".format(resident)
    server.sendmail("shesec@bsc.coop", resident.email, msg
server.quit()
