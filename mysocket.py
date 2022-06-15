from http.client import ImproperConnectionState
import socket
import cv2

bind_ip = "140.114.233.91"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)
print('server start at: %s:%s' % (bind_ip, bind_port))

while True:
    client, addr = server.accept()
    data = client.recv(1024).decode()
    if data == "other" or data == "NO face":
        print("Who you are")
        img = cv2.imread('C:\\Users\\User\\Downloads\\no_enter1.jpg')
        cv2.imshow('C:\\Users\\User\\Downloads\\no_enter1.jpg',img)
        cv2.waitKey(10000)
        cv2.destroyAllWindows()
    elif data == "Yu ming":
        print("Hi master")
        img = cv2.imread('C:\\Users\\User\\Downloads\\opened1.jpg')
        cv2.imshow('C:\\Users\\User\\Downloads\\opened1.jpg',img)
        cv2.waitKey(10000)
        cv2.destroyAllWindows()
    client.close


