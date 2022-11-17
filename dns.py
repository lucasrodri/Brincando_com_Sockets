import socket
L = int(input())

for i in range(0, L):
    reversed_dns = socket.gethostbyaddr(input())
    print(reversed_dns[0])