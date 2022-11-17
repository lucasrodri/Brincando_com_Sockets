import socket

n = int(input())

for i in range(n):
    endereco = input()
    endereco = socket.gethostbyaddr(endereco)
    print(endereco[0])
