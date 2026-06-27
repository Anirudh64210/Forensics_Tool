import time
from scapy.all import sniff, IP, TCP

previous_connection_count = 0

def packet_callback(packet):
    global previous_connection_count

    if packet.haslayer(IP) and packet.haslayer(TCP):
        connection_count = len(sniffed_packets)  # Update this to your method of counting active connections
        
        if connection_count != previous_connection_count:
            print(f"Change detected! Connection count: {connection_count}")
            previous_connection_count = connection_count

# Sniff network traffic on the specified interface
iface = "eth0"  # Change this to your network interface
sniffed_packets = []

while True:
    sniffed_packets = sniff(iface=iface, count=100, timeout=5)  # Capture packets for 5 seconds
    packet_callback(None)
    time.sleep(60)  # Wait for 60 seconds before the next capture
