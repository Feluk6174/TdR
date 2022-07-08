def manage_new_node(connection, address, conn_info):
    global connections, get_suposed_connected
    n_connected = len(connections)
    n_nodes = len("SELECT * FROM ips;")
    n_suposed_connections = get_suposed_connected(n_nodes)

    if n_connected < n_suposed_connections and not check_if_connected(conn_info["ip"]):
        connection.send("OK".encode("utf-8"))
        connections.append((conn_info["ip"], connection, address[0]+":"+str(address[1])))
        thread = threading.Thread(target=node_main_loop, args=(connection, conn_info["ip"], address[0]+":"+str(address[1])))
        thread.start()