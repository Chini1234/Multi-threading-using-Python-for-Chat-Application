import socket
import threading

# List to keep track of connected clients
clients = []

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                broadcast(message, client_socket)
            else:
                remove_client(client_socket)
                break
        except:
            continue

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            client.send(message.encode('utf-8'))

def remove_client(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)

def start_server(host='127.0.0.1', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print("Server started and listening...")

    while True:
        client_socket, addr = server_socket.accept()
        clients.append(client_socket)
        print(f"Connection from {addr} established.")
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    start_server()
