# ubuntu
from socket import *
import _thread

BUFF = 1024
# HOST = '127.0.0.1'
HOST = ''
PORT = 2500

def response(key):
    a=input()
    return a

def handler(clientsock, addr):
    while True:
        clientsock.send(response('').encode())  # 응답 전송

if __name__ == '__main__':
    ADDR = (HOST, PORT)
    serversock = socket(AF_INET, SOCK_STREAM)  # 소겟 생성
    serversock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 재사용 가능
    # TCP 소켓을 생성하고 결합한다, 소켓이 종료된 후 소켓 주소 재사용으로 인한 오류를 방지하기 위해 setsockopt()메소드에서 SO_REUSEADDR로 설정한다.
    serversock.bind(ADDR)  # 종단 간 결합
    serversock.listen(5)  # 대기

    while True:
        print('waiting for connection...')
        clientsock, addr = serversock.accept()
        print('...connected from:', addr)
        _thread.start_new_thread(handler, (clientsock, addr))  # 스레드 생성 실행
