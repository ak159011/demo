import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.200', 9000))
filename = input('请输入文件名称:')
s.send(filename.encode('utf8'))
with open(filename, 'wb') as file :
    while True :
        con = s.recv(1024)
        if not con :
            break
        file.write(con)
s.close()
