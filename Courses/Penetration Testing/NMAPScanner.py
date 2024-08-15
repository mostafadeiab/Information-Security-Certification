import nmap

scanner = nmap.PortScanner()

print("Simple NMAP Automation Tool")
print("<------------------------->")

ip_addr = input("Enter the IP Address For Scanning: ")
print(f"Scanning IP Address: {ip_addr}")
type(ip_addr)

resp = input("""\nEnter Type of Scan: 
             1) SYN ACK Scan 
             2) UDP Scan 
             3) Comprehensive Scan\n""")
print(f"Seleteced Option: {resp}")

if resp == '1':
    print(f"NMAP Version: {scanner.nmap_version()}")
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print(f"IP Status: {scanner[ip_addr].state()}")
    print(scanner[ip_addr].all_protocols())
    print(f"Open Ports: {scanner[ip_addr]['tcp'].keys()}")
elif resp == '2':
    print(f"NMAP Version: {scanner.nmap_version()}")
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print(f"IP Status: {scanner[ip_addr].state()}")
    print(scanner[ip_addr].all_protocols())
    print(f"Open Ports: {scanner[ip_addr]['udp'].keys()}")
elif resp == '3':
    print(f"NMAP Version: {scanner.nmap_version()}")
    scanner.scan(ip_addr, '1-1024', '-v -sV -sC -A -O')
    print(scanner.scaninfo())
    print(f"IP Status: {scanner[ip_addr].state()}")
    print(scanner[ip_addr].all_protocols())
    print(f"Open Ports: {scanner[ip_addr]['tcp'].keys()}")
else:
    print("Invaild Option")
    exit()