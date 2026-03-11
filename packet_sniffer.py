import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
s.bind((socket.gethostbyname(socket.gethostname()), 0))
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
while True:
    packet = s.recv(65535)
    print("Packet length:", len(packet))
    ip_header = packet[0:20]
    iph = struct.unpack('!BBHHHBBH4s4s', ip_header)
    
    source_ip = socket.inet_ntoa(iph[8])
    dest_ip = socket.inet_ntoa(iph[9])
    protocol = iph[6]

    if protocol == 1:
        protocol_name = "ICMP"
    elif protocol == 6:
        protocol_name = "TCP"
    elif protocol == 17:
        protocol_name = "UDP"
    else:
        protocol_name = "Other"
    print("Source:", source_ip, "-> Destination:", dest_ip)
    print("Protocol:", protocol_name)
    
    if protocol == 6 or protocol == 17:
        tcp_udp_header = packet[20:24]
        src_port, dest_port = struct.unpack('!HH', tcp_udp_header)
        print("Source Port:", src_port)
        print("Destination Port:", dest_port)
        print()