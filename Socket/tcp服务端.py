import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.1.3',9000))
s.listen(128)
c,x=s.accept()
date=c.recv(1024)

# (<socket.socket fd=316, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0,
#  laddr=('192.168.1.3', 9000),
# raddr=('192.168.1.200', 51510)>, ('192.168.1.200', 51510))
print(date)