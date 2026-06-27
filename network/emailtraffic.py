from scapy.all import sniff, IP, TCP
import re

def packet_callback(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        payload = packet[TCP].payload
        
        # Check if the packet contains SMTP-related data
        if "SMTP" in str(payload):
            smtp_data = str(payload)
            
            # Extract email addresses from the SMTP data
            email_addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', smtp_data)
            if email_addresses:
                print(f"Source IP: {src_ip}, Destination IP: {dst_ip}")
                print("Email Addresses:", email_addresses)

# Sniff network traffic on the specified interface
iface = "eth0"  # Change this to your network interface
sniff(iface=iface, prn=packet_callback, filter="tcp port 25")  # Capture SMTP traffic on port 25
