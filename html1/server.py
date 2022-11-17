import socketserver
import http.server
import sys
import os

HOST = "localhost"
PORT = 9999
httpd = None

try:
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer((HOST, PORT), Handler)
    httpd.serve_forever()
except Exception as e:
    if httpd is not None:
        httpd.shutdown()
        httpd.server_close()
    raise
