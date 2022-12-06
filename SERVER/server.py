import http.server 
import socketserver
from urllib.parse import urlparse
from urllib.parse import parse_qs
hostName = "localhost"
serverPort = 8080

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)

        self.send_header("Content-type", "text/html")

        self.end_headers()

        html = f"<html><head></head><body><h1>biggest W in the Century ong!</h1></body></html>"

        self.wfile.write(bytes(html, "utf8"))

        return
        

HTTP_OBJ = MyHttpRequestHandler

with socketserver.TCPServer(("", serverPort), HTTP_OBJ) as httpd:
    print("Server started at localhost:" + str(serverPort))
    httpd.serve_forever()

