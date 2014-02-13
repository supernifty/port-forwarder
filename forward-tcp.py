import socket
import sys
import thread

listen_host = "192.168.0.100"
listen_port = 8080

target_host = "127.0.0.1"
target_port = 64153

def main():
    thread.start_new_thread(server, () )
    lock = thread.allocate_lock()
    lock.acquire()
    lock.acquire()

def server(*settings):
    try:
        dock_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dock_socket.bind((listen_host, listen_port)) # listen
        dock_socket.listen(5)
        print "*** listening on %s:%i" % ( listen_host, listen_port )
        while True:
            client_socket, client_address = dock_socket.accept()
            print "*** from %s:%i to %s:%i" % ( client_address, listen_port, target_host, target_port )
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.connect((target_host, target_port))
            thread.start_new_thread(forward, (client_socket, server_socket, "client -> server" ))
            thread.start_new_thread(forward, (server_socket, client_socket, "server -> client" ))
    finally:
        thread.start_new_thread(server, () )

def forward(source, destination, description):
    data = ' '
    while data:
        data = source.recv(1024)
        print "*** %s: %s" % ( description, data )
        if data:
            destination.sendall(data)
        else:
            source.shutdown(socket.SHUT_RD)
            destination.shutdown(socket.SHUT_WR)

if __name__ == '__main__':
    main()
