from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi
PORT = 8000
GPS = ['fluff coord', 'fluff coord 2']
ENGINE = ['SPEED']

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        
        if self.path.endswith(''):
            self.send_response(200)
            self.send_header("content-type", "text/html")
            self.end_headers()

            output = ''
            output += '<html><body>'
            output += "<h1> <b>Home Page </b></h1>"
            output += '-<img src="images/stevejung.jpg" alt="why is this not showing" style="width:1024px;height:1024px">'
            self.wfile.write(output.encode())
        
        
        if self.path.endswith('/GPS'):
            self.send_response(200)
            self.send_header("content-type", "text/html")
            self.end_headers()
            
            output = ''
            output += '<html><body>'
            output += '<h1>Task List</h1>'
            output += '<h3><a href="/tasklist/APPENDGPS">Enter GPS Data</a></h3>'
            for task in GPS:
                output += task
                output += "<a/ href='/APPENDGPS/%s/remove'>X</a>"
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

            output += '<form method="POST" enctype="multipart/form-data" action="/DATA/new">'
            output += '<input name="task" type="text" placeholder="Add new task">'
            output += '<input type ="submit" value="Add">'
            output += '</form>'
            output += '</body></html>'

            self.wfile.write(output.encode())

        if self.path.endswith('/remove'):
            listIDPath = self.path.split('/')[2]
            print(listIDPath)
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()

            output =''
            output +='<html><body>'
            output += '<h1>Remove task: %s</h1>' % listIDPath.replace('%20', '')
            output +='<h1>Remove task: %s </h1>' % listIDPath.replace('%20', '')
            
            output += '</body></html>'
            self.wfile.write(output.encode())

    def do_POST(self):
        if self.path.endswith('/new'):
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            content_len = int(self.headers.get('Content-length'))
            pdict['CONTENT-LENGTH'] = content_len

            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                new_task = fields.get('task')
                GPS.append(new_task[0])
                

            self.send_response(301)
            self.send_header('content-type', 'text/html')
            self.send_header('Location', '/tasklist')
            self.end_headers()





def main():
    server = HTTPServer(("", PORT), RequestHandler)
    print("Server Running on %s" % PORT)
    server.serve_forever()

if KeyboardInterrupt:
    server = HTTPServer(("", PORT), RequestHandler)
    server.server_close()


if __name__ == "__main__":
    main()