import re
from scapy.all import sniff
from http import HTTPStatus
import requests

def packet_callback(packet):
    if packet.haslayer('TCP') and packet.haslayer('Raw'):
        raw_data = packet[Raw].load.decode(errors='ignore')
        if 'GET' in raw_data or 'POST' in raw_data:  # Identify HTTP requests
            urls = re.findall(r'(https?://[^\s]+)', raw_data)  # Extract URLs
            for url in urls:
                print(f"Detected URL: {url}")
                if 'download' in url:  # Example: Check if URL indicates a download link
                    response = requests.get(url)
                    filename = url.split('/')[-1]  # Extract filename from URL
                    with open(filename, 'wb') as f:
                        f.write(response.content)
                    print(f"Downloaded: {filename}")

# Sniff network traffic on the specified interface
sniff(iface="eth0", prn=packet_callback, filter="tcp port 80")  # Change "eth0" to your network interface

# Note: This example is simplified and might not cover all scenarios and cases.
