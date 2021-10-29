import sys
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import pandas as pd

sys.path.append("..")
from mapper.readData import readData
from config.appConfig import asciiText

AES_LENGTH = 16

class prpcrypt():
    def __init__(self, key):
        self.key = key
        self.mode = AES.MODE_ECB
        self.cryptor = AES.new(self.pad_key(self.key).encode(), self.mode)

    def pad(self,text):
        while len(text) % AES_LENGTH != 0:
            text += ' '
        return text

    def pad_key(self,key):
        while len(key) % AES_LENGTH != 0:
            key += ' '
        return key

    def encrypt(self, text):
        self.ciphertext = self.cryptor.encrypt(self.pad(text).encode())
        return b2a_hex(self.ciphertext)

if __name__ == '__main__':
    pc = prpcrypt('abcdef') 
    path_orgin = '../data/user-origin.csv'
    path_encrypt = '../data/user.csv'
    df=pd.DataFrame(readData(path_orgin))

    print(asciiText)
    print("Encrypt Usernames, Passwords And Email:")

    for idx in range(1,len(df.values)):
        username,passwd,email = df.values[idx,0],df.values[idx,1],df.values[idx,2]
        df.values[idx,0],df.values[idx,1],df.values[idx,2] =  pc.encrypt(username).decode('utf-8'),pc.encrypt(passwd).decode('utf-8'),pc.encrypt(email).decode('utf-8')
        print("["+str(idx)+"]",username,passwd,email,"=>",df.values[idx,0],df.values[idx,1],df.values[idx,2])

    # write to file
    df.to_csv(path_encrypt,header=False, index=False)

    print("Encrypt Success!")