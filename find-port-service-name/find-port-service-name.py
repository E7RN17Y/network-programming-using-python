import socket
import sys

if sys.version_info.major == 2:
    print('Please upgrade to versionn 3.0 of python because you\'re using version 2 of python')

def find_service_name():
    protocol_name = 'tcp'
    for port in [80,21,25]:
        print("Port %s: => service name: %s"%(port, socket.getservbyport(port,protocol_name)))
    print("Port: %s => service name: %s"%(53, socket.getservbyport(53, 'udp')))
 

if __name__ == '__main__':
    find_service_name()