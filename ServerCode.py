import socket
import threading
from datetime import datetime
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from User import User, create_client_data_file  # Import the User class and function
from Monster import add_monster_user  # Import the add_monster_user function

clients = []
client_usernames = {}

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
    username = client_usernames.pop(client_socket, None)
    clients.remove(client_socket)
    broadcast_clients()

# Function to broadcast messages to all clients, including the sender
def broadcast_message(message, sender_socket):
    for client in clients:
        try:
            client.send(message.encode('utf-8'))
        except:
            client.close()
            clients.remove(client)

# Function to broadcast the list of connected clients
def broadcast_clients():
    clients_list = ["Connected clients:"]
    clients_list.extend([user.username for user in client_usernames.values()])
    clients_list_message = "\n".join(clients_list)
    for client in clients:
        try:
            client.send(clients_list_message.encode('utf-8'))
        except:
            client.close()
            clients.remove(client)

# Update the GUI with new messages
def update_gui(message):
    text_box.config(state=tk.NORMAL)
    text_box.insert(tk.END, message + '\n')
    text_box.config(state=tk.DISABLED)
    text_box.yview(tk.END)

# Function to start the server
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 9999))  # Bind to all interfaces on port 9999
    server_socket.listen(5)  # Listen for incoming connections

    print("Server listening on port 9999...")
    update_gui("Server listening on port 9999...")

    while True:
        client_socket, addr = server_socket.accept()
        clients.append(client_socket)
        print(f"Accepted connection from {addr}")
        update_gui(f"Accepted connection from {addr}")

        # Receive the username from the client
        username_data = client_socket.recv(1024).decode('utf-8')
        username, message = username_data.split(':', 1)  # Split into username and message parts
        user = User(username)
        client_usernames[client_socket] = user
        
        # Create and initialize client data file
        create_client_data_file(user)

        broadcast_clients()

        # Send a welcome message
        welcome_message = f"Welcome {username}!"
        client_socket.send(welcome_message.encode('utf-8'))
        update_gui(welcome_message)
        
        # Send the message after the username
        client_socket.send(message.encode('utf-8'))

        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

# Create the GUI window
root = tk.Tk()
root.title("Server Messages")

text_box = ScrolledText(root, state=tk.DISABLED, wrap=tk.WORD)
text_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Add button to add a monster user
add_monster_button = tk.Button(root, text="Add Monster User", command=lambda: add_monster_user(client_usernames, broadcast_clients, update_gui))
add_monster_button.pack(padx=10, pady=10)

# Start the server in a separate thread
server_thread = threading.Thread(target=start_server)
server_thread.daemon = True
server_thread.start()

# Start the GUI main loop
root.mainloop()