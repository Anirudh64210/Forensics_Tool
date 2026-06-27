import psutil

def get_network_connections():
    connections = psutil.net_connections(kind="inet")
    connection_details = []

    for conn in connections:
        connection_details.append({
            "family": conn.family.name,
            "type": conn.type.name,
            "local_address": f"{conn.laddr.ip}:{conn.laddr.port}",
            "remote_address": f"{conn.raddr.ip}:{conn.raddr.port}",
            "status": conn.status,
            "pid": conn.pid
        })

    return connection_details

network_connections = get_network_connections()

for conn in network_connections:
    print(conn)

#pip install psutil
#we are using psutil
