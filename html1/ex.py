import http.client
def HTTPclient(host,port):
    L = int(input())
    conn = http.client.HTTPConnection(host, port)
    for i in range(L):
        conn.request("GET",input())
        r1 = conn.getresponse()
        print(r1.read().decode())

HTTPclient("localhost", 9999)