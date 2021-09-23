import socket
import threading
import time


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


s.bind(('127.0.0.1', 8888))

s.listen(5)
print('Wait for connection...')

def tcp(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Success!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break


        sock.send(('Welcom! %s!' % data.decode('utf-8')).encode('utf-8'))

    sock.close()
    print('Connection from %s:%s closed.' % addr)

while True:

    sock, addr = s.accept()

    t = threading.Thread(target=tcp, args=(sock, addr))

    t.start()


