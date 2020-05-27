#
# MicroPython http_server_simplistic.py example
#
# This example shows how to write the smallest possible HTTP
# server in MicroPython. With comments and convenience code
# removed, this example can be compressed literally to ten
# lines. There's a catch though - read comments below for
# details, and use this code only for quick hacks, preferring
# http_server.py for "real thing".
#
try:
    import usocket as socket
except:
    import socket

from led import LED

CONTENT = b"""\
HTTP/1.0 200 OK

Hello #%d from MicroPython!
"""
class WebServer(object):

    def __init__(self):
        pass

    def start(self):
        led = LED()

        s = socket.socket()
        ai = socket.getaddrinfo("0.0.0.0", 8080)
        print("Bind address info:", ai)
        addr = ai[0][-1]

        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        s.bind(addr)
        s.listen(5)
        print("Listening, connect your browser to http://<this_host>:8080/")

        counter = 0
        while True:
            res = s.accept()
            client_s = res[0]
            client_addr = res[1]
            print("Client address:", client_addr)
            print("Client socket:", client_s)

            req = client_s.recv(4096)
            arr = req.decode().split('\n')
            dic = {}
            for line in arr:
                if line.startswith('GET /?'):
                    print(line)
                    queryString = line.split(' ')[1][2:]
                    print('queryString=', queryString)
                    params =  queryString.split('&')
                    for param in params:
                        p = param.split('=')
                        print(p)
                        dic[p[0]] = int(p[1])

                    led.set(dic)

            print(dic)

            client_s.send(CONTENT % counter)
            client_s.close()
            counter += 1
            print()
