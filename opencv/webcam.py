import cv2

capture = cv2.VideoCapture(0) #노트북 웹캠 연결(숫자 바꾸면 외장 웹캠)
#화면 크기 지정
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)

if capture.isOpened():
    while True:
        ret, frame = capture.read()     # 카메라로부터 frame 읽기, 잘 받았다면 ret에 true 반환
        if ret:
            cv2.imshow("camera", frame)   # 이미지 표시 
            if cv2.waitKey(1) == ord('q'):  # 키보드의 q 를 누르면 중지
                break
        else:
            print('no frame')
            break
else:
    print("카메라를 열 수 없습니다.")

capture.release()                   # 캡처 객체를 release
cv2.destroyAllWindows()             # 모든 영상 창 닫기