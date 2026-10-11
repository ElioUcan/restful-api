#!/usr/bin/python3

from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path = '/info':
            dic = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            data = json.dumps(dic)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_header("Content-lenght", str(len(data)))
            self.wfile.write(data)
        elif self.path = '/data':
            dic = {
                "name": "Jhon",
                "age":30,
                "city": "New York"
            }
            data = json.dumps(dic)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-lenght", str(len(data)))
            self.wfile.write(data)
        else:
                error_payload = {"error": "Endpoint not found", "path": self.path}
                json_bytes = json.dumps(error_payload)
                self.send_response(404)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(json_bytes)))
                self.end_headers()





