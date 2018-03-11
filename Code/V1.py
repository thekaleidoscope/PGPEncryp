#from pgyp.constants import *\
import pgpy
from pgpy.constants import PubKeyAlgorithm, KeyFlags, HashAlgorithm, SymmetricKeyAlgorithm, CompressionAlgorithm
def getdata(keyfile,PublicKey):
    name=str(input("Name:"))
    _email=str(input("EMail:"))


    key = pgpy.PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, 4096)
    uid = pgpy.PGPUID.new(name,email=_email)

    pk=key.add_uid(uid,usage={KeyFlags.Sign}, hashes=[HashAlgorithm.SHA256], ciphers=[SymmetricKeyAlgorithm.AES256])
    kf=open(keyfile,"w")
    kf.write(str(key))
    pkf=open(PublicKey,"w")
    pkf.write(str(uid)+"\n"+str(key.pubkey))
    #print(key.pubkey)
i=input("New User?(Y/N)")
if i=="Y" or i=="y":
    getdata("PriKey.txt","Pubkey.txt")
def encrypt(data, key):
    k = Encryption.get_key(key)
    m = k.pubkey.encrypt(pgpy.PGPMessage.new(data), cipher=SymmetricKeyAlgorithm.AES256)
    return str(m)

def decrypt(data, key):
    k = Encryption.get_key(key)
    m = k.decrypt(pgpy.PGPMessage.from_blob(data))
    return bytes(m._message.contents) if isinstance(m._message.contents, bytearray) else m._message.contents
while(True):
    e=input("Encrypt(E)/Decrypt(D)")
    
    print("Key:",)
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    k = '\n'.join(lines)

    d=input("data:")
    if e=="E":
        encrypt(data,key)
    elif e=="D":
        decrypt(data,key)

    else:
        print("ReRead the options")

    if(input("Done(Y/N)")=="Y"):
        break
