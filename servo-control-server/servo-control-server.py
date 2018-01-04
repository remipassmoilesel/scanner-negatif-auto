#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler

FORWARD_ONE_STRIP = '/forward-one-strip'
BACKWARD_ONE_STRIP = '/backward-one-strip'


class RequestHandler(BaseHTTPRequestHandler):

    def _set_headers(self, responseCode=200):
        self.send_response(responseCode)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

    def do_GET(self):
        if self.path == FORWARD_ONE_STRIP:
            self._set_headers()
            print('Going forward for one strip ...')

        elif self.path == BACKWARD_ONE_STRIP:
            self._set_headers()
            print('Going forward for one strip ...')

        else:
            self._set_headers(500)
            print('Bad command: ', self.path)


def run(server_class=HTTPServer, handler_class=RequestHandler):
    server_address = ('', 8000)
    print('Server started on: ', server_address)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    run()
