import SocketServer
# coding: utf-8

# Copyright 2013 Abram Hindle, Eddie Antonio Santos
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
# Furthermore it is derived from the Python documentation examples thus
# some of the code is Copyright © 2001-2013 Python Software
# Foundation; All Rights Reserved
#
# http://docs.python.org/2/library/socketserver.html
#
# run: python freetests.py

# try: curl -v -X GET http://127.0.0.1:8080/

import os.path

class MyWebServer(SocketServer.BaseRequestHandler):
    
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print(self.data+"\n")
        requestFullData = self.data.splitlines()
        requestData = requestFullData[0].split()
        path = "./www"+requestData[1]
            
        # path is a file, exists
        message = ""
        if (os.path.isfile(path)):
            ctype = path.split(".")[-1]
            message += ("HTTP/1.1 200 OK\n"+
                        "Content-Type: text/"+ctype+"\n\n"+
                        open(path).read())
            
        # path is a directory, index exists
        elif (os.path.isfile(path+"index.html")):
            message += ("HTTP/1.1 200 OK\n"+
                        "Content-Type: text/html\n\n"+
                        open(path+"index.html").read())
            
        # doesn't exist, throw a 404
        else:
            message += ("HTTP/1.1 404 Not Found\n"+
                        "Content-Type: text/html\n\n"+
                        "<!DOCTYPE html>\n"+
                        "<html><body>HTTP/1.1 404 Not Found</body></html>")
        print(message)
        self.request.sendall(message)
                
if __name__ == "__main__":
    HOST, PORT = "localhost", 8080

    SocketServer.TCPServer.allow_reuse_address = True
    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyWebServer)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
