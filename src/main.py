import http.server, ssl
import os

try:
    SERVER_ADDRESS = os.getenv("SERVER_ADDRESS")
    PORT = os.getenv("PORT")
    DATA_DIRECTORY = os.getenv("DATA_DIRECTORY")
    CERT_FILE= os.getenv("CERT_FILE")
    KEY_FILE = os.getenv("KEY_FILE")
except:
    print("Environment Variable not found closing.")
    exit()

server_address = (SERVER_ADDRESS, int(PORT))
class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DATA_DIRECTORY, **kwargs)
httpd = http.server.HTTPServer(server_address, Handler)
httpd.socket = ssl.wrap_socket(httpd.socket,
                               server_side=True,
                               certfile=CERT_FILE,
                               keyfile=KEY_FILE,
                               ssl_version=ssl.PROTOCOL_TLS)
httpd.serve_forever()
