import os,errno
from pathlib import Path
import getpass
from Code.V1 import getdata,get_key,encrypt,decrypt
#----------------------PREREQUISITE--------------------------------
def makedir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
makedir('Reciever')
Rec=Path('Reciever/Reciever.asc')
if not Rec.is_file():
    print("import Reciever PGP Key")
#-----------------------ENCRYPTING DATA-----------------------------------
print("Email data:")
lin = []
while True:
    line = input()
    if line:
        lin.append(line)
    else:
        break
d = '\n'.join(lin)

print("Encrypting using Pubkey of Reciever")
en=encrypt(d,'Reciever/Reciever')
open('Reciever/Endata.asc','wb').write(en)
#------------------------DONE---------------------------

#--------------------------FIGURE OUT SMTP PART-----------------------------------------

usr=input("From:")
pswd = getpass.getpass('Password:')
to=input("To:")
sub=input("Subject:")
def send_email(user,pasw,recv,sub,body):

    import smtplib

    _message="""From:%s\nTo:%s\nSubject:%s\n\n%s"""%(user,recv,sub,body)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pasw)
        server.sendmail(user,recv, message)
        server.close()
        print('successfully sent the mail')
    except:
        print("failed to send mail")

send_email(usr,pswd,to,sub,str(open('Reciever/Endata.asc','rb').read()))
