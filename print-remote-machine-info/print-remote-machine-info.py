import socket
import sys

def remote_machine_info(remotehostname)->str:
    return "The Ip addr of %s is %s"%(remotehostname,socket.gethostbyname(remotehostname))


if __name__ == '__main__':
    try:
        print(remote_machine_info(sys.argv[1]))
    except socket.error as err_msg:
        print("%s: %s"%(sys.argv[1],err_msg))