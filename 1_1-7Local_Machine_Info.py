#!/usr/bin/env python
import socket
from binascii import hexlify

def print_machine_info():
    host_name = socket.gethostname()
    ip = socket.gethostbyname(host_name)
    print "Host Name: %s" % host_name
    print "IP address: %s" % ip

def convert_ip4_address():
    for ip_addr in ['127.0.0.1','192.168.0.1']:
        packed_ip_addr = socket.inet_aton(ip_addr)
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
        print("IP Address: %s => Packed: %s, unpacked: %s" %(ip_addr,hexlify(packed_ip_addr),unpacked_ip_addr))

def find_service_name():
    protocolname = 'tcp'
    for port in [80,25]:
        print "Port: %d => service name: %s" %(port, socket.getservbyport(port,protocolname))
    print "Port: %d => service name: %s" % (53,socket.getservbyport(53,'udp'))

def test_socket_timeout():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print "Default socket timeout : %s" %s.gettimeout()
    s.settimeout(100)
    print "Current socket timeout : %s" % s.gettimeout()
if __name__ == "__main__":
    print_machine_info()
    convert_ip4_address()
    find_service_name()
    test_socket_timeout()