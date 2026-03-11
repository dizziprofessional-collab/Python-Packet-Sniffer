## Python-Packet-Sniffer
A simple packet sniffer written with python that captures and analyzes live network packets using raw sockets.
## Features
- Captures live packets from the network
- Displays packet length
- Extracts IPv4 Information (First 20)
- Shows source IP and destination IP
- Detects network protocols: ICMP, TCP, UDP
- Extracts TCP/UDP port numbers (ICMP doesn't have them)
## Example Output
Packet Length: 60
Source: 199.172.4.2 -> Destination: 10.2.4.553
Protocol: UDP
Source Port: 26890
Destination Port: 443
## Requirements
- Python 3
- Administrator Privileges (required for raw sockets on Windows)
## Run the Program using: python packet_sniffer.py

### REMEMBER THIS IS FOR EDUCATIONAL PURPOSES ONLY
