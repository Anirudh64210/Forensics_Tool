from scapy.all import sniff, IP, TCP

def packet_callback(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        connection_status = "OPEN" if packet[TCP].flags == 2 else "CLOSED"
        
        connection_info = {
            "src_ip": src_ip,
            "src_port": src_port,
            "dst_ip": dst_ip,
            "dst_port": dst_port,
            "status": connection_status
        }
        print(connection_info)

# Sniff network traffic on the specified interface
sniff(iface="eth0", prn=packet_callback, filter="tcp")  # Change "eth0" to your network interface
