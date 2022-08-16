import socket
from datetime import datetime

host="localhost" #ip 주소
port=9503 #포트 번호

print('starting server[{}시 {}분 {}초]'.format(datetime.now().hour, datetime.now().minute,datetime.now().second))
#UDP/IP 기반 소켓 객체 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

#ip 주소와 포트번호 연동 
sock.bind((host, port))

#4096 버퍼 용량의 데이터 수신
(data, address) = sock.recvfrom(4096)
print('received {} from {} [{}시 {}분 {}초]'.format(data, address, datetime.now().hour, datetime.now().minute,datetime.now().second))

sock.close()
