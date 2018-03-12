from Code.V1 import getdata,get_key,encrypt,decrypt
import os, errno

def makedir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

for i in ['Sender','Reciever']:
    makedir(i)
    print(i+" Input:")
    getdata('{}/{}key.asc'.format(i,i),'{}/{}.asc'.format(i,i))


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

print("Data Encrypted , Data Sent to Reciever")
open('Reciever/Endata.asc','wb').write(en)

d=open('Reciever/Endata.asc','rb').read()
print('Encrypted Data:\n'+str(d))

print("Decrypting data:")

print(str(decrypt(d,'Reciever/Recieverkey')))
