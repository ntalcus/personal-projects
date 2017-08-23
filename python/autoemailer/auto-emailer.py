import csv
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

class Resident(object):

    def __init__(self, name, email, room):
        self.name = name
        self.email = email
        self.room = room

file_name = sys.argv[1]

with open(file_name, 'rU') as f:
    reader = csv.reader(f)
    lst = []
    for row in reader:
        sublst = []
        for value in row:
            sublst += [value]
        lst += [sublst]

resident_dict = {}
i = 0

for resident in lst:
    key = (lst[i][0][0:3] + "_" + lst[i][2]).lower() #takes the first three + last character of residents name
    name = lst[i][0].upper()
    email = lst[i][1]
    room = lst[i][2].upper()

    resident_dict[key] = Resident(name, email, room)
    i += 1



resident_dict['momo'] = Resident("Mo", "mmadrigalavina@berkeley.edu", "FUCK YOU")

email_list = ['noa_i', 'momo'] #this should be changed everytime

def send_emails(email_list): #takes in a list of names of residents with mail, names should be first 3 letters + last letter of names


    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('shesec@bsc.coop', 'prospect2250')

    for resident_name in email_list:
        resident = resident_dict[resident_name]

        #complex email
        toaddr = str(resident.email)

        #this is where the email is composed
        msg = MIMEMultipart()
        msg['From'] = 'shesec@bsc.coop'

        msg['To'] = toaddr

        msg['Subject'] = str("You've got mail! {0}".format(str(time.strftime("%c"))))

        body = (
        "{0.name}, \r\n"
        "\r\n"
        "You've got mail in the mailbox {0.room}. \r\n"
        "\r\n"
        "Best, \r\n"
        "Ogre Mail-bot \r\n"
        "DISCLAIMER: This action is scripted. If you would like to no longer receive these notifications, please send an email to shesec@bsc.coop."
        ).format(resident)

        msg.attach(MIMEText(str(body), 'plain'))

        # simple text notification
        # msg = "{0.name}, room {0.room}, you have mail/packages.".format(resident).upper()

        server.sendmail("shesec@bsc.coop", toaddr, str(msg))

    server.quit()
