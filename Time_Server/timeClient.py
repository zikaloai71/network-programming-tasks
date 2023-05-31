from socket import *

S = socket(AF_INET, SOCK_STREAM)

S.connect(('localhost', 1025))

while True:
    data = S.recv(1024)
    print(data.decode())
    if not data:
        break