from scapy.all import sniff

def packet_callback(packet):
    if packet.haslayer('TCP'):
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        payload = packet[TCP].payload
        if payload:
            if src_port == 80 or dst_port == 80:  # HTTP traffic
                if packet[TCP].flags & 0x02:  # SYN flag (upload)
                    print(f"Upload: {payload}")
                elif packet[TCP].flags & 0x10:  # ACK flag (download)
                    print(f"Download: {payload}")

# Sniff network traffic on the specified interface
sniff(iface="eth0", prn=packet_callback, filter="tcp")  # Change "eth0" to your network interface
