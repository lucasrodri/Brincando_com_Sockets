import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind(('', 12000)) #tupla

while True:
    msg_byte, endereco_ip_cliente = servidor.recvfrom(2048)
    msg_resp = msg_byte.decode().upper()
    servidor.sendto(msg_resp.encode(), endereco_ip_cliente)
    print(f"chegou: {msg_byte.decode('utf-8', 'ignore')}")
    print(f"voltou: {msg_resp}")








