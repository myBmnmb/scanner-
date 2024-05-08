#!/usr/bin/python3

import socket

target_host= input("Enter Your IP: ")
target_ports= range(1, 1025) #Scan Ports

for port in target_ports:
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)

    result= sock.connect_ex((target_host, port))
    if result == 0:
        print(f"Port {port} is open")
       
        sock.close()