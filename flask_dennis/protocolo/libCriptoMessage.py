from Cryptodome.Cipher import AES
from base64 import b64encode, b64decode

class CriptoMessage:
    def __init__(self, sessionk):
        self.sessionk = sessionk
    def gerarMsg(self, msg):
        cipher = AES.new(self.sessionk, AES.MODE_EAX)
        msgc = cipher.encrypt(bytes(ord(m) for m in msg))
        msgc = cipher.nonce + msgc
        return b64encode(msgc)
    def recuperarMsg(self, enc_msg):
        msgc = b64decode(enc_msg)
        nonce = msgc[0:16]
        cipher = AES.new(self.sessionk, AES.MODE_EAX, nonce)
        return str(cipher.decrypt(msgc[16:]))
