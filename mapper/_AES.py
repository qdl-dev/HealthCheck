from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

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

    def decrypt(self, text):
        plain_text = self.cryptor.decrypt(a2b_hex(text)).decode()
        return plain_text.rstrip(' ')

if __name__ == '__main__':
    pass