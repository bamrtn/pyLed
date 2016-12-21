import http.server
import ledPatterns

ledPatterns.led.ser = ledPatterns.led.serial.Serial('COM6',250000)
time.sleep(2)
ledPatterns.init()

f = open('led.html','r')
ledHTML = f.read()
f.close()

PORT = 8000

#Handler
class myHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path[0:7]=='/setled':
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            ledPatterns.style = self.path[8:]
            self.wfile.write(bytes("<h1>Led style changed!</h1>","utf-8"))
        elif self.path[0:4]=='/led':
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(bytes(ledHTML,'utf-8'))
        else:
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(bytes("<h1>Hello World!</h1>","utf-8"))

#Starting server
server = http.server.HTTPServer(('0.0.0.0', PORT), myHandler)
print("serving at port", PORT)
server.serve_forever()
