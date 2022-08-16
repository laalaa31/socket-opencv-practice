import socket
from datetime import datetime

host="localhost" #ip 주소
port=6789 #포트 번호

print('starting server[{}시 {}분 {}초]'.format(datetime.now().hour, datetime.now().minute,datetime.now().second))
#TCP/IP 기반 소켓 객체 생성
parent = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

#ip 주소와 포트번호 연동 
parent.bind((host, port))

#3단계 연결 설정에 따라 동작하는 TCP 클라이언트로부터 연결 요청 기다림
#5대 동시접속 가능
parent.listen(5)

#연결 accept 후 소켓객체 child와 주소 반환
(child, address) = parent.accept()

#데이터 수신
data = child.recv(1000)
print('received {} from {} [{}시 {}분 {}초]'.format(data, address, datetime.now().hour, datetime.now().minute,datetime.now().second))

child.close()
parent.close()