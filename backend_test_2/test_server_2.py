import socket
import threading


HOST = "127.0.0.1"
PORT = 42069

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("=====SERVER RUNNING ON {HOST}:{PORT}=====")

clients = []
usernames = []

def broadcast(message, sending_client):
    global clients
    for client in clients:
        if not client == sending_client:
            client.send(message)

def handle_messages(client):
    global clients, usernames
    while True:
        try:
            message = client.recv(1024)
            braodcast(message, client)
        except:
            index = clients.index(client)
            username = usernames[index]
            broadcast(f"[SERVER] User {username} disconected".encode("utf-8"))
            clients.remove(client)
            usernames.remove(client)
            client.close()

def receive_connections():
    global usernames, clients
    while True:
        client, address = server.accept()
?!?jedi=0, ?!?                   (*_*data: bytes*_*, flags: int=...) ?!?jedi?!?
        client.send("@username".encode("utf-8"))
        username = client.recv(1024).decode("utf-8")
    
        clients.append(client)
        usernames.append(username)


        print(f"{username} ({str(address)}) connected")
    
        broadcast(f"[SERVER] User {username} connected".encode("utf-8"), client)

        client.send("Connected to server".encode("utf-8"))
        thread = threading.Thread(target=handle_messages, args=(client,))
        thread.start()

if __name__ == "__main__":
    receive_connections()
