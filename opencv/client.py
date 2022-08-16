import socket
import cv2

IP = '127.0.0.1' #IP주소
PORT = 9505

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
flag=0
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    d = frame.flatten()
    s = d.tostring()

    #UDP는 데이터를 한번에 65535 byte까지만 보낼 수 있기 때문에 총 921,600 Byte의 데이터를 20개로 나눠서 전송
    #맨 첫 바이트는 패킷 번호를 붙여 영상 왜곡 방지
    for i in range(20):
        sock.sendto(bytes([i]) + s[i*46080:(i+1)*46080], (IP, PORT))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            flag=1
            break

    if flag==1:
        break
    
cap.release()
sock.close() 