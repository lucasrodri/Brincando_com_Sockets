import socket
L = int(input())

for i in range(0, L):
    dns = socket.gethostbyname(input())
    print(dns)