import socket, os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.1.200', 9000))
s.listen(128)
Client_socket, Client_addr = s.accept()
data = Client_socket.recv()
if os.path.isfile(data) :
    with open(data, 'rb') as file :
        Client_socket.send(data)
else :
    print('文件不存在')
