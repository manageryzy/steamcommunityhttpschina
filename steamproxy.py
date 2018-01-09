#!/usr/bin/python
import sys
import port_forward
import threading
if sys.version_info >= (3, 0):
    from http.server import SimpleHTTPRequestHandler
    from http.server import HTTPServer
else:
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    from SocketServer import TCPServer as HTTPServer

# forward all https tcp packages


class https_proxy(object):
    def __init__(self, target_host='104.122.255.229', source_port=443, target_port=443):
        self.__source_port = source_port

        self.__target_host = target_host
        self.__target_port = target_port

    def run(self):
        t = threading.Thread(target=port_forward.server, args=(
            [self.__source_port, self.__target_host, self.__target_port]))
        t.start()
        return t


class http_handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(301)
        self.send_header('Location', 'https://steamcommunity.com' + self.path)
        self.end_headers()


class http_proxy(object):
    def __init__(self, port=80):
        self.__port = port

    def run(self):
        httpd = HTTPServer(("", self.__port), http_handler)

        t = threading.Thread(target=httpd.serve_forever)
        t.start()
        return t


if __name__ == '__main__':
    httpd = http_proxy()
    httpsd = https_proxy()

    t1 = httpd.run()
    t2 = httpsd.run()
