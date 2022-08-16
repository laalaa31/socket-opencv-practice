import socket
from datetime import datetime

host= '127.0.0.1' #ip 주소
port=6789 #포트 번호

print('starting client [{}시 {}분 {}초]'.format(datetime.now().hour, datetime.now().minute,datetime.now().second))
#TCP/IP 기반 소켓 객체 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

#연결 요청
sock.connect((host, port))
message=b"!!!! bird Message !!!!"

#메시지 보내기
sock.sendto(message, (host, port))
print('sending {} [{}시 {}분 {}초]'.format(message, datetime.now().hour, datetime.now().minute,datetime.now().second))

sock.close()