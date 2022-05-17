# python server example for spider trap
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<body>", "utf-8"))

        ################################################################# 

        link=self.path.replace("/","")
        if(link==""):
            x=1
        else:
            x=int(link)

        link1=str(x*2)
        link2=str(x*2+1)
        self.wfile.write(bytes("<a href=%s>Link - %s</a>" % (link1, x),"utf-8"))
        self.wfile.write(bytes("<br>", "utf-8"))
        self.wfile.write(bytes("<a href=%s>Link - %s</a>" % (link2, x+1),"utf-8"))

        ##################################################################

        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")