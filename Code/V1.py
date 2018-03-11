#from pgyp.constants import *\
import pgpy
from pgpy.constants import PubKeyAlgorithm, KeyFlags, HashAlgorithm, SymmetricKeyAlgorithm, CompressionAlgorithm
def getdata(keyfile,PublicKey):
    name=str(input("Name:"))
    _email=str(input("EMail:"))


    key = pgpy.PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, 4096)
    uid = pgpy.PGPUID.new(name,email=_email)

    pk=key.add_uid(uid,usage={KeyFlags.Sign, KeyFlags.EncryptCommunications, KeyFlags.EncryptStorage}, hashes=[HashAlgorithm.SHA256], ciphers=[SymmetricKeyAlgorithm.AES256])
    kf=open(keyfile,"wb")
    kf.write(bytes(key))

    pkf=open(PublicKey,"w")
    pkf.write(str(key.pubkey))
    #print(key.pubkey)
def get_key(name):
      key = pgpy.PGPKey.from_file("{}.asc".format(name))[0]
      return key

i=input("New User?(Y/N)")
if i=="Y" or i=="y":
    getdata("PriKey.asc","Pubkey.txt")
def encrypt(data, key="PriKey"):
    k = get_key(key)
    m = k.pubkey.encrypt(pgpy.PGPMessage.new(data), cipher=SymmetricKeyAlgorithm.AES256)
    return bytes(m)

def decrypt(data, key="PriKey"):
    k = get_key(key)
    m = k.decrypt(pgpy.PGPMessage.from_blob(data))
    return bytes(m._message.contents) if isinstance(m._message.contents, bytearray) else m._message.contents

while(True):
    e=input("Encrypt(E)/Decrypt(D)")

    if e=="E":
        print("data:")
        lin = []
        while True:
            line = input()
            if line:
                lin.append(line)
            else:
                break
        d = '\n'.join(lin)
        ed=encrypt(d)
        open("EncData.asc","wb").write(ed)

    elif e=="D":
        d=open("EncData.asc","rb").read()
        print(str(decrypt(d)))

    else:
        print("ReRead the options")

    if(input("Done(Y/N)")=="Y"):
        break
