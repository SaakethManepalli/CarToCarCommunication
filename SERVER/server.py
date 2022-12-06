from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8000

class MyServer(BaseHTTPRequestHandler)
def do_GET(self):
    self.