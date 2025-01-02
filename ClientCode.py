import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox
import argparse

# Global variable to control the receive_messages loop
running = True

# Function to handle receiving messages from the server
def receive_messages(client_socket, text_area, clients_display):
    global running
    while running:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message.startswith("Connected clients:"):
                clients_display.config(state=tk.NORMAL)
                clients_display.delete(1.0, tk.END)
                clients_display.insert(tk.END, f"{message}\n")
                clients_display.config(state=tk.DISABLED)
            else:
                text_area.config(state=tk.NORMAL)
                text_area.insert(tk.END, f"{message}\n")
                text_area.config(state=tk.DISABLED)
                text_area.see(tk.END)
        except:
            break
    client_socket.close()

# Function to send messages to the server
def send_message(client_socket, message_entry, username):
    message = message_entry.get()
    if message:
        full_message = f"{username}: {message}"
        client_socket.send(full_message.encode('utf-8'))
        message_entry.delete(0, tk.END)

# Function to start the client and connect to the server
def start_client(host, port, text_area, message_entry, clients_display, username):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        threading.Thread(target=receive_messages, args=(client_socket, text_area, clients_display)).start()
        return client_socket
    except Exception as e:
        messagebox.showerror("Connection Error", str(e))
        return None

# Function to parse command-line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description="Chat Client")
    parser.add_argument('--name', type=str, required=True, help='Username for the chat client')
    return parser.parse_args()

# Create the main application window
def create_gui(username):
    window = tk.Tk()
    window.title("Chat Client")

    frame = tk.Frame(window)
    frame.pack(padx=10, pady=10)

    text_area = scrolledtext.ScrolledText(frame, wrap=tk.WORD, state=tk.DISABLED, width=50, height=15)
    text_area.pack(padx=5, pady=5)

    clients_display = scrolledtext.ScrolledText(frame, wrap=tk.WORD, state=tk.DISABLED, width=50, height=5)
    clients_display.pack(padx=5, pady=5)

    username_label = tk.Label(frame, text=username)
    username_label.pack(side=tk.LEFT, padx=(5, 0), pady=5)

    message_entry = tk.Entry(frame, width=40)
    message_entry.pack(side=tk.LEFT, padx=5, pady=5)

    send_button = tk.Button(frame, text="Send", command=lambda: send_message(client_socket, message_entry, username))
    send_button.pack(side=tk.LEFT, padx=5, pady=5)

    close_button = tk.Button(frame, text="Close", command=window.quit)
    close_button.pack(side=tk.LEFT, padx=5, pady=5)

    message_entry.bind("<Return>", lambda event: send_message(client_socket, message_entry, username))

    host = '127.0.0.1'  # Server IP address
    port = 9999         # Server port

    client_socket = start_client(host, port, text_area, message_entry, clients_display, username)

    def on_closing():
        global running
        running = False
        if client_socket:
            client_socket.close()
        window.quit()

    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()

# Run the GUI application
if __name__ == "__main__":
    args = parse_arguments()
    create_gui(args.name)