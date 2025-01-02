import socket
import threading
from datetime import datetime

clients = []

# Function to handle client connections
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                message_with_timestamp = f"[{timestamp}] {message}"
                print(f"Client: {message_with_timestamp}")
                broadcast_message(message_with_timestamp, client_socket)
            else:
                break
        except:
            break
    client_socket.close()
    clients.remove(client_socket)

# Function to broadcast messages to all clients, including the sender
def broadcast_message(message, sender_socket):
    for client in clients:
        try:
            client.send(message.encode('utf-8'))
        except:
            client.close()
            clients.remove(client)

# Create a socket for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 9999))  # Bind to all interfaces on port 9999
server_socket.listen(5)  # Listen for incoming connections

print("Server listening on port 9999...")

while True:
    client_socket, addr = server_socket.accept()
    clients.append(client_socket)
    print(f"Accepted connection from {addr}")
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()