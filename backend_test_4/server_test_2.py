import socket
import threading
import database
import time

HOST = "127.0.0.1"
PORT = int(input("Input port: "))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

db = database.connection()

connections = []
ips = ["127.0.0.1:22222", "127.0.0.1:33333", "127.0.0.1:44444"]

def mainloop(connection):
    global connections, HOST, PORT
    while True:
        try:
            connection.send(f"{HOST}:{PORT}: {len(connections)}".encode("utf-8"))
        
            res = connection.recv(1024)
    
            print(res)
            
            #time.sleep(0.1)
                
        except socket.error as e:
            print(e)
            connections.remove(connection)
            break

def connect(num:int):
    global connections, client
    if num == 3:
        return

    address = ips[num].split(":")
    
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.connect((address[0], int(address[1])))
    
    connections.append(connection)
    
    #if not num == 3:
    connection.send(str(num+1).encode("utf-8"))

    thread = threading.Thread(target=mainloop, args=(connection,))
    thread.start()

def main():
    global connections, server 
    while True:
        connection, address = server.accept()

        print(f"connected by {address}")

        connections.append(connection)
        #ips.append(address)
        
        t = int(connection.recv(1028).decode("utf-8"))
        print(t)
        connect(t)

        thread = threading.Thread(target=mainloop, args=(connection,))
        thread.start()


if __name__ == "__main__":
    main()
