import http.server


class CachingHandler(http.server.BaseHTTPRequestHandler):
    cache = {}

    def do_GET(self):
        if self.path in self.cache:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(self.cache[self.path])
            print("Using cached response", self.path)
        else:
            self.send_response(200)
            self.end_headers()
            message = f"Hello {self.path}!".encode('utf-8')
            self.cache[self.path] = message
            self.wfile.write(message)
            print("Generated response", self.path)


def main():
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, CachingHandler)
    print(f"Serving on port {server_address[1]}...")

    # Serve in the background until a key is pressed
    import threading
    server_thread = threading.Thread(target=httpd.serve_forever)
    server_thread.daemon = True
    server_thread.start()

    input("Press any key to stop the server.")
    httpd.shutdown()
    print("Server stopped.")


main()
