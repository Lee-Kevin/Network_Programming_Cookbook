#!/usr/bin/env python

import sys
import socket
import argparse

def main():
    # setup argument parsing
    parser = argparse.ArgumentParser(description='Socket Error Examples')
    parser.add_argument('--host',action="store",dest="host",required=False)
    parser.add_argument('--port',action="store",dest="port",type=int, required=False)
    parser.add_argument('--file',action="store",dest="file",required=False)
    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port
    filename = given_args.file

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error,e:
        print "Error creating socket: %s" % e
        sys.exit(1)
    try:
        s.connect((host,port))
    except socket.gaierror,e:
        print("Address-related error connecting to server: %s" % e)
        exit(1)

    try:
        s.sendall("GET %s HTTP/1.0\r\n\r\n" % filename)
    except socket.error,e:
        print("Error send data %s" % e)
        sys.exit(1)

    while True:
        try:
            buf = s.recv(2048)
        except socket.error,e:
            print("Error reciving data %s" % e)
            sys.exit(1)
        if not len(buf):
            break
        # write the recived data
        sys.stdout.write(buf)
SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096
def modify_buff_size():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    bufsize = sock.getsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF)
    print("Buffere size [Before]: %d" %bufsize)
    sock.setsockopt(socket.SOL_TCP,socket.TCP_NODELAY,1)

    sock.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_SNDBUF,
        SEND_BUF_SIZE
    )

    sock.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_RCVBUF,
        SEND_BUF_SIZE
    )
    bufsize = sock.getsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF)
    print("Buffer size [After]: %d" %bufsize)

if __name__ == "__main__":
#    main()
    modify_buff_size()



