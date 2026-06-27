import psutil
import time

# Store the current network connections as a dictionary
def get_network_connections():
    connections = psutil.net_connections(kind="inet")
    connection_data = {}

    for conn in connections:
        connection_data[conn.fd] = {
            "family": conn.family.name,
            "type": conn.type.name,
            "local_address": f"{conn.laddr.ip}:{conn.laddr.port}",
            "remote_address": f"{conn.raddr.ip}:{conn.raddr.port}",
            "status": conn.status,
            "pid": conn.pid
        }

    return connection_data

# Compare the current and previous snapshots to identify changes
def detect_connection_changes(prev_connections, current_connections):
    added_connections = [conn for conn in current_connections if conn not in prev_connections]
    removed_connections = [conn for conn in prev_connections if conn not in current_connections]
    return added_connections, removed_connections

previous_connections = {}
while True:
    current_connections = get_network_connections()
    added, removed = detect_connection_changes(previous_connections, current_connections)
    
    if added:
        print("Added connections:")
        for conn in added:
            print(current_connections[conn])
    
    if removed:
        print("Removed connections:")
        for conn in removed:
            print(previous_connections[conn])
    
    previous_connections = current_connections
    time.sleep(5)  # Check for changes every 5 seconds
