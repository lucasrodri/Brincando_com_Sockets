
import os
import socketserver
import http.server

#https://stackoverflow.com/questions/39801718/how-to-run-a-http-server-which-serves-a-specific-path
web_dir = os.path.join(os.path.dirname(__file__), '/home/lucas/Redes/Projeto/brincando_com_sockets/servidor')
os.chdir(web_dir)

Handle = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", 17853), Handle)
httpd.serve_forever()

