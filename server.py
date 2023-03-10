import socket
import argparse
import threading
import time
from os.path import exists

host = "localhost"
port = 4000
recvdata=""
def handle_client(client_socket, addr):
    filename = client_socket.recv(1024) #클라이언트한테 파일이름(이진 바이트 스트림 형태)을 전달 받는다
    print('받은 데이터 : ', filename.decode('utf-8')) #파일 이름을 일반 문자열로 변환한다
    data_transferred = 0
    if not exists(filename):
        print("no file")
    print("파일 %s 전송 시작" %filename)
    try:
        while data: #데이터가 있을 때까지
            recvdata+=data
            data_transferred += len(data)
            data = client_socket.recv(1024) #1024바이트를 받아 온다
    except Exception as ex:
        print(ex)
    print("전송완료 %s, 전송량 %d" %(filename, data_transferred))


def accept_func():
    global server_socket
    #IPv4 체계, TCP 타입 소켓 객체를 생성
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #포트를 사용 중 일때 에러를 해결하기 위한 구문
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #ip주소와 port번호를 함께 socket에 바인드 한다.
    #포트의 범위는 1-65535 사이의 숫자를 사용할 수 있다.
    server_socket.bind((host, port))

    #서버가 최대 5개의 클라이언트의 접속을 허용한다.
    server_socket.listen(5)

    while 1:
        try:
            #클라이언트 함수가 접속하면 새로운 소켓을 반환한다.
            client_socket, addr = server_socket.accept()
        except KeyboardInterrupt:
            server_socket.close()
            print("Keyboard interrupt")

        print("클라이언트 핸들러 스레드로 이동 됩니다.")
        #accept()함수로 입력만 받아주고 이후 알고리즘은 핸들러에게 맡긴다.
        t = threading.Thread(target=handle_client, args=(client_socket, addr))
        t.daemon = True
        t.start()


if __name__ == '__main__':
    #parser와 관련된 메서드 정리된 블로그 : https://docs.python.org/ko/3/library/argparse.html
    #description - 인자 도움말 전에 표시할 텍스트 (기본값: none)
    #help - 인자가 하는 일에 대한 간단한 설명.
    parser = argparse.ArgumentParser(description="\nJoo's server\n-p port\n")
    parser.add_argument('-p', help="port")

    args = parser.parse_args()
    try:
        port = int(args.p)
    except:
        pass
    accept_func()