import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('192.168.1.200', 9000))
s.sendto('adhabhjak'.encode('uft8'), ('192.168.1.3', 9000))
s.close()
