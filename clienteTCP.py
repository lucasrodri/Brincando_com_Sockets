import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('', 15000))
while True:
    msg = input("Digite a mensagem: ")
    if msg == "":
        break
    status = cliente.send(msg.encode())
    if status > 0:
        msg_bytes = cliente.recv(2048)
        print(msg_bytes.decode())
        #print("Recebeu", repr(msg_bytes))
cliente.close()



