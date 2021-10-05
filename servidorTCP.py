import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('localhost', 15000)) #tupla
servidor.listen()
conn, addr = servidor.accept()
while True:
    msg_byte = conn.recv(2048)
    teste = msg_byte.decode('utf8')
    if teste == "sair\r\n" or teste == "sair":
        break
    msg_resp = msg_byte.decode('utf8').upper()
    conn.sendall(msg_resp.encode())
    print(f"chegou: {msg_byte.decode('utf8')}")
    print(f"voltou: {msg_resp}")
conn.close()








