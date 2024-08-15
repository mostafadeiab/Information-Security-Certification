import socket

def banner(ip, port):
    s = socket.socket()
    s.connect((ip,int(port)))
    print(str(s.recv(1024)).strip('b'))

def main():
    ip_addr = input("Enter the IP Address: ")
    port = input("Enter the Port Number: ")
    banner(ip_addr,port)

main()