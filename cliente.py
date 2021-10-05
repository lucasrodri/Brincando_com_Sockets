import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    msg = input("Digite a mensagem: ")
    cliente.sendto(msg.encode(), ('', 12000))
    msg_bytes, endereco_ip = cliente.recvfrom(2048)
    print(msg_bytes.decode())



