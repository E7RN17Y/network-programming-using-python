import socket

host_name = socket.gethostname()
ip_addr = socket.gethostbyname(host_name)

print("IP Addr:%s"%(ip_addr))