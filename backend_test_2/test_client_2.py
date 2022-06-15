import socket
import threading


HOST = "127.0.0.1"
PORT = 42069

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

username = input("Enter your username: ")

def recieve_messages():
    global username
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            if message == "@username":
                client.send(username.encode("utf-8"))
            else:
                print(message)
        except:
            print("<ERROR>")
            client.close()
            break

    
def write_messages():
    global username
    while True:
        message = f"{username}: {input('')}"
        client.send(message.encode("utf-8"))


if __name__ == "__main__":
    recive_thead = threading.Thread(target=recieve_messages)
    recive_thead.start()

    write_thread = threading.Thread(target=write_messages)
    write_thread.start()
