import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('127.0.0.1', 8888))
print('set UDP on 6666...')
while True:
    data, addr = s.recvfrom(1024)


    print('Received from %s:%s' % addr)
    s.sendto(b'Welcom! %s' % data, addr)


