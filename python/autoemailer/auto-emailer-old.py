import csv
import smtplib
import sys

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

for resident in lst:
    name = lst[i][0][0:3] + "_" + lst[i][0][-1] #takes the first three + last character of residents name
    email = lst[i][1]
    room = lst[i][2]

    resident_dict[name] = Resident(name, email, room)

email_list = [noa_s] #this should be changed everytime

def send_emails(email_list): #takes in a list of names of residents with mail, names should be first 3 letters + last letter of names

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('shesec@bsc.coop', 'prospect2250')

    for resident_name in email_list:
        msg = "{0.name}, room {0.room}, you have mail/packages.".format(resident_dict[resident_name])
        server.sendmail("shesec@bsc.coop", resident.email, msg)

    server.quit()
