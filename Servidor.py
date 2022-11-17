import socketserver
import http.server
def HTTPserver(host, port):
    global httpd
    Handler = http.server.SimpleHTTPRequestHandler
    Handler.extensions_map.update({
        '.webapp': 'application/x-web-app-manifest+json',
    });

    httpd = socketserver.TCPServer(("", PORT), Handler)
    httpd.serve_forever()

import threading
import sys
import random
import time 
import socket
import os

PORT = int(random.randint(2222, 65535))
sys.stderr = open('err%d.txt'%(PORT), 'w')
try:
    x = threading.Thread(target=HTTPserver, args=('',PORT,))
    x.start()
    host="localhost"
    time.sleep(0.1)
    try:
        HTTPclient(host,PORT)
    except Exception as e:
        print("Unexpected error:", e, " - ", sys.exc_info()[0])
    if httpd is not None:
        httpd.shutdown()
        httpd.server_close()
    x.join()
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except Exception as e:
    print(e)
except:
    print("Unexpected error:", sys.exc_info()[0])


os.remove('err%d.txt'%(PORT))