import psutil

def get_connections(direction="all"):
    connections = psutil.net_connections(kind="inet")
    filtered_connections = []

    for conn in connections:
        if direction == "all" or (direction == "outward" and conn.status == psutil.CONN_ESTABLISHED) or (direction == "inward" and conn.status == psutil.CONN_LISTEN):
            filtered_connections.append({
                "family": conn.family.name,
                "type": conn.type.name,
                "local_address": f"{conn.laddr.ip}:{conn.laddr.port}",
                "remote_address": f"{conn.raddr.ip}:{conn.raddr.port}",
                "status": conn.status,
                "pid": conn.pid
            })

    return filtered_connections

# Change "direction" to "all", "outward", or "inward"
direction = "all"
connections = get_connections(direction)

for conn in connections:
    print(conn)
