import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

ip_addr = input("Enter the IP Address For Scanning: ")
port = int(input("Enter the Port Number For Scanning: "))

def portScanner(port):
    if s.connect_ex((ip_addr,port)):
        print(f"Port {port} is closed.")
    else: print(f"Port {port} is open.")

portScanner(port)