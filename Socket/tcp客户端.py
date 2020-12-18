import socket

# 第二个参数socket.SOCK_STREAM表示tcp的socket连接，socket.SOCK_DGRAM表示udp连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.3', 9000))
s.send('你好'.encode('utf8'))

s.close()
