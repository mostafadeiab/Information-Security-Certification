import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Host = '192.168.1.104'
host = socket.gethostname()
port = 444

# Binding to Socket
serversocket.bind((host,port)) # host will be replaced/subbed with IP, if changed and not running on host

# Starting TCP Listener
serversocket.listen(3)

while True:
    # Starting the Connection
    clientsocket, addr = serversocket.accept()

    print(f"Connection Established: \nClient{clientsocket} \nAddress{addr}")

    clientsocket.send("Recieved Connection\n.".encode('ASCII'))
    clientsocket.close()
