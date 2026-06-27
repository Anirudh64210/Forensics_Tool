from scapy.all import *

# Read the captured pcap file
pcap_file = "capture.pcap"
packets = rdpcap(pcap_file)

# Process packets
for packet in packets:
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        print(f"Source IP: {src_ip}, Destination IP: {dst_ip}")


#tshark -i eth0 -w capture.pcap  run this code first to capture network traffic
