import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

# Function to handle receiving messages from the server
def receive_messages(client_socket, text_area):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                text_area.config(state=tk.NORMAL)
                text_area.insert(tk.END, f"Server: {message}\n")
                text_area.config(state=tk.DISABLED)
                text_area.see(tk.END)
            else:
                break
        except:
            break
    client_socket.close()

# Function to send messages to the server
def send_message(client_socket, message_entry):
    message = message_entry.get()
    if message:
        client_socket.send(message.encode('utf-8'))
        message_entry.delete(0, tk.END)

# Function to start the client and connect to the server
def start_client(host, port, text_area, message_entry):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        threading.Thread(target=receive_messages, args=(client_socket, text_area)).start()
        return client_socket
    except Exception as e:
        messagebox.showerror("Connection Error", str(e))
        return None

# Create the main application window
def create_gui():
    window = tk.Tk()
    window.title("P2P Chat Client")

    frame = tk.Frame(window)
    frame.pack(padx=10, pady=10)

    text_area = scrolledtext.ScrolledText(frame, wrap=tk.WORD, state=tk.DISABLED, width=50, height=20)
    text_area.pack(padx=5, pady=5)

    message_entry = tk.Entry(frame, width=40)
    message_entry.pack(side=tk.LEFT, padx=5, pady=5)
    message_entry.bind("<Return>", lambda event: send_message(client_socket, message_entry))

    send_button = tk.Button(frame, text="Send", command=lambda: send_message(client_socket, message_entry))
    send_button.pack(side=tk.LEFT, padx=5, pady=5)

    host = '127.0.0.1'  # Server IP address
    port = 9999         # Server port

    client_socket = start_client(host, port, text_area, message_entry)

    window.protocol("WM_DELETE_WINDOW", lambda: window.quit() if client_socket else None)
    window.mainloop()

# Run the GUI application
if __name__ == "__main__":
    create_gui()