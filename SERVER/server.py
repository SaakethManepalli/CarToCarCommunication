from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi

DATA = ["Task One", "Task Two", "Take Three"]

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('/tasklist'):
            self.send_response(200)
            self.send_header("content-type", "text/html")
            self.end_headers()
            
            output = ''
            output += '<html><body>'
            output += '<h1>Task List</h1>'
            output += '<h3><a href="/tasklist/new">Add New Task</a></h3>'
            for task in DATA:
                output += task
                output += '</br>'
            output += '</body></html>'
            self.wfile.write(output.encode())

        if self.path.endswith('/new'):
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()

            output =''
            output += '<html><body>'
            output += '<h1> Add New Data </h1>'

            output += '<form method="POST" enctype="multipart/form-data" action="/tasklist/new">'
            output += '<input name="task" type="text" placeholder="Add new task">'
            output += '<input type ="submit" value="Add">'
            output += '</form>'
            output += '</body></html>'

            self.wfile.write(output.encode())


    def do_POST(self):
        if self.path.endswith('/new'):
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                new_task = fields.get('task')
                DATA.append(new_task) # Could Add Time Element Here

            self.send_response(301)
            self.send_header('content-type', 'text/html')
            self.send_header('Location', '/tasklist')
            self.end_headers()





def main():
    PORT = 8000
    server = HTTPServer(("", PORT), RequestHandler)
    print("Server Running on %s" % PORT)
    server.serve_forever()


if __name__ == "__main__":
    main()