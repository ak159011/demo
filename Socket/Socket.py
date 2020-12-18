import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('192.168.1.3', 9000))
s.sendto('12y1938129'.encode('utf8'), ('192.168.1.200', 9000))
date, addr = s.recvfrom(1024)
print('{}从{}端口给你发了{}'.format(addr[0], addr[1], date.decode('utf8')))
s.close()

