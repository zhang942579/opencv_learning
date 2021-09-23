import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


for data in [b'TOM', b'Jerry', b'Spike', "张三".encode("utf-8")]:
    s.sendto(data, ('127.0.0.1', 8888))
    print(s.recv(1024).decode('utf-8'))

s.close()

