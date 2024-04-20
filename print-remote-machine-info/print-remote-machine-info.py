import socket
import sys

def remote_machine_info(remotehostname)->str:
    return "The Ip addr of %s is %s"%(remotehostname,socket.gethostbyname(remotehostname))


if __name__ == '__main__':
    print(remote_machine_info(sys.argv[1]))
    