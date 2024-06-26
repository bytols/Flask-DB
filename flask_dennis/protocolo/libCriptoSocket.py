from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
from libCriptoMessage import CriptoMessage
from base64 import b64encode, b64decode
import socket as s, random as r,datetime as d
from socketserver import  ThreadingTCPServer,StreamRequestHandler

# Cliente Conecta
# Servidor envia Pubk
# Cliente retorna SessionK encriptada com Pubk
# Servidor recupera SessionK e decripta com PrivK

# Envio e Recepção -> SessionK

class CriptoSocket:
    def __init__(self, ip, porta):
        self.sock = s.socket(s.AF_INET, s.SOCK_STREAM)
        self.sock.connect((ip, porta))
        pubk = self.sock.recv(2048)
        sessionk = bytes(r.randint(0, 255) for i in range(16))
        self.cm = CriptoMessage(sessionk)
        print(sessionk)
        cipher_rsa = PKCS1_OAEP.new(RSA.import_key(pubk))
        enc_session_key = b64encode(cipher_rsa.encrypt(sessionk))
        self.sock.send(enc_session_key+b"\n")
    def enviar(self, msg):
        self.sock.sendall(self.cm.gerarMsg(msg)+b"\n")
    def receber(self):
        enc_msg = self.sock.recv(1024)
        return self.cm.recuperarMsg(enc_msg)
    def terminar(self):
        self.sock.close()

class ServerTask(StreamRequestHandler):
    def handle(self):
        addr = self.client_address
        print(f'Connected: {addr[0]}:{addr[1]}')
        sessionk = self.adquirirChave()
        self.cm = CriptoMessage(sessionk)
        while True:
            msgc = self.rfile.readline()
            if not msgc:
                print(f'Disconnected: {addr[0]}:{addr[1]}')
                break # exits handler, framework closes socket
            msg = self.cm.recuperarMsg(msgc)
            print(f'Received: {msg}')
            data_hora = d.datetime.now()
            data_hora_str = data_hora.strftime('%d/%m/%Y, %H:%M:%S')
            ret = self.cm.gerarMsg(f"Recebido pelo servidor em {data_hora_str}")
            self.wfile.write(ret)
            self.wfile.flush()
    def adquirirChave(self):
        self.wfile.write(self.server.pubk)
        self.wfile.flush()
        enc_session_key = self.rfile.readline()
        cipher_rsa = PKCS1_OAEP.new(RSA.importKey(self.server.privk))
        sessionk = cipher_rsa.decrypt(b64decode(enc_session_key))
        print(sessionk)
        return sessionk #depois tiro o debug
        

class CriptoServerSocket:
    def __init__(self, host, porta):
        key = RSA.generate(2048)
        self.sock_s = ThreadingTCPServer((host, porta), ServerTask)
        self.sock_s.privk = key.exportKey()
        self.sock_s.pubk = key.publickey().export_key()
    def executar(self):
        self.sock_s.serve_forever()
