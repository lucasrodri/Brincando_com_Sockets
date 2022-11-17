import http.client

conn = http.client.HTTPConnection("localhost", 9999)
content = input()
conn.request("GET",content)
r1 = conn.getresponse()
if(r1.status != 404):        
    data1 = r1.getheaders()# This will return the headers
    for field in data1:
        if field[0].lower() == "content-type":
            if field[1].lower() == "audio/mpeg":
                print("Playing audio: %s"%(content))
            elif field[1].lower() == "text/html":
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
