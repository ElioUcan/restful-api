#!/usr/bin/python3
"""Simple HTTP server using http.server module."""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class RequestHandler(BaseHTTPRequestHandler):
    """Custom HTTP request handler for simple API endpoints."""

    def do_GET(self):
        """Handle GET requests for defined endpoints."""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            payload = {"name": "John", "age": 30, "city": "New York"}
            json_bytes = json.dumps(payload).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json_bytes)

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            payload = {
                "version": "1.0",
                "description": "A simple API built with http.server",
            }
            json_bytes = json.dumps(payload).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json_bytes)

        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run(host="localhost", port=8000):
    """Start the HTTP server on specified host and port."""
    server = HTTPServer((host, port), RequestHandler)
    print(f"Servidor corriendo en http://{host}:{port}/")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor detenido.")
        server.server_close()


if __name__ == "__main__":
    run()
