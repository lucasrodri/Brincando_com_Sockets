import http.client

def HTTPclient(host,port):
    # Read https://tools.ietf.org/html/rfc7231#section-3.1.1.5
    L = int(input())
    conn = http.client.HTTPConnection(host, port)
    for i in range(0,L):
        content = input()
        conn.request("GET",content)
        r1 = conn.getresponse()
        if(r1.status != 404):        
            data1 = r1.getheaders()# This will return the headers
            print(data1)
            for field in data1:
                if field[0].lower() == "content-type":
                    print(field[1].lower())
                    if field[1].lower() == "audio/mpeg":
                        print("Playing audio: %s"%(content))
                    elif field[1].lower().startswith("text/html"):
                        print("Browsing: %s"%(content))
                    elif field[1].lower() == "video/x-msvideo":
                        print("Playing media: %s"%(content))
                    elif field[1].lower() == "application/json":
                        print("Processing JSON: %s"%(content))
                    else:
                        
                        print("Unknown file/media: %s-%s"%(field[1],content))
        else:
            print("Content not found")            
    conn.close()

HTTPclient("localhost",8888)