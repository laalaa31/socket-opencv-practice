import socket
import numpy
import cv2

IP = '127.0.0.1' #IP 주소
PORT = 9505

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORT))

#'\xff' 46080*20개 공간 생성
s = [b'\xff' * 46080 for x in range(20)]
flag=0

while True:
    picture = b''

    data, addr = sock.recvfrom(46081)

    #보낼 때 패킷 번호 붙여서 보내줬음
    #data[0]=패킷 번호
    #data[1:46081] 데이터만 슬라이싱
    s[data[0]] = data[1:46081]

    if data[0] >= 19:
        for i in range(20):
            picture += s[i]

        frame = numpy.fromstring(picture, dtype=numpy.uint8)
        frame = frame.reshape(480, 640, 3)
        cv2.imshow("frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            flag=1
            break

    if flag==1:
        break

sock.close()

