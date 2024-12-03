from __future__ import print_function

import socket
bufsize = 1024 

# set these values
target_host = "127.0.0.1"
target_port = 64153

listen_host = "192.168.0.103"
listen_port = 8080

def forward(data, port):
    print("*** Forwarding: '%s' from port %s" % (data, port))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("localhost", port)) # Bind to the port data came in on
    sock.sendto(data, (target_host, target_port))

def listen(host, port):
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    listen_socket.bind((host, port))
    print("*** Listening on %s:%s" % ( host, port ))
    while True:
        data, addr = listen_socket.recvfrom(bufsize)
        forward(data, addr[1]) # data and port

listen(listen_host, listen_port)
