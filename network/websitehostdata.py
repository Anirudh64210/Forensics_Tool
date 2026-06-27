import socket
from ipwhois import IPWhois

def get_host_details(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        ipwhois = IPWhois(ip_address)
        result = ipwhois.lookup_rdap()
        
        host_details = {
            "domain": domain,
            "ip_address": ip_address,
            "network_name": result["asn_description"],
            "country": result["asn_country_code"],
            "registrant": result["entities"][0]["name"]
        }
        
        return host_details
    except Exception as e:
        print("Error:", e)
        return None

website_domain = "example.com"  # Replace with the domain you want to query
host_details = get_host_details(website_domain)

if host_details:
    print("Website Host Details:")
    print("Domain:", host_details["domain"])
    print("IP Address:", host_details["ip_address"])
    print("Network Name:", host_details["network_name"])
    print("Country:", host_details["country"])
    print("Registrant:", host_details["registrant"])
