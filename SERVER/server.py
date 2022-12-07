from http.server import HTTPServer, BaseHTTPRequestHandler

tasklist = ["Task One", "Task Two", "Take Three"]

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type", "text/html")
        self.end_headers()
        
        output = ''
        output += '<html><body>'
        output += '<h1>Task List</h1>'
        for task in tasklist:
            output += task
            output += '</br>'
        output += '</body></html>'
        self.wfile.write(output.encode())





def main():
    PORT = 8000
    server = HTTPServer(("", PORT), RequestHandler)
    print("Server Running on %s" % PORT)
    server.serve_forever()


if __name__ == "__main__":
    main()