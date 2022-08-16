import socket
from datetime import datetime

host= '127.0.0.1' #ip 주소
port=9503 #포트 번호

print('starting client [{}시 {}분 {}초]'.format(datetime.now().hour, datetime.now().minute,datetime.now().second))
#UDP/IP 기반 소켓 객체 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

message=b"!!!! bird Message !!!!"

#메시지 보내기
sock.sendto(message, (host, port))
print('sending {} [{}시 {}분 {}초]'.format(message, datetime.now().hour, datetime.now().minute,datetime.now().second))

sock.close()