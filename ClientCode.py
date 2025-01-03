import socket
import threading
import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar, END
import argparse

# Global variables
running = True
targeted_monster = None

# Function to handle receiving messages from the server
def receive_messages(client_socket, text_area, users_listbox, mobs_listbox):
    global running
    while running:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message.startswith("Connected clients:"):
                users_listbox.delete(0, END)
                mobs_listbox.delete(0, END)
                clients = message.split('\n')[1:]
                for client in clients:
                    if "is_user=1" in client:
                        users_listbox.insert(END, client)
                    elif "is_user=0" in client:
                        mobs_listbox.insert(END, client)
            else:
                text_area.config(state=tk.NORMAL)
                text_area.insert(tk.END, f"{message}\n")
                text_area.config(state=tk.DISABLED)
                text_area.see(tk.END)
        except:
            break
    client_socket.close()

# Function to send messages to the server
def send_message(client_socket, message_entry, message):
    if message:
        client_socket.send(message.encode('utf-8'))
        message_entry.delete(0, tk.END)

# Function to start the client and connect to the server
def start_client(host, port, text_area, message_entry, users_listbox, mobs_listbox, username):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        threading.Thread(target=receive_messages, args=(client_socket, text_area, users_listbox, mobs_listbox)).start()
        return client_socket
    except Exception as e:
        messagebox.showerror("Connection Error", str(e))
        return None

# Function to parse command-line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description="Chat Client")
    parser.add_argument('--name', type=str, required=True, help='Username for the chat client')
    return parser.parse_args()

# Function to update the targeted monster display
def update_targeted_monster_display(targeted_monster_label):
    global targeted_monster
    targeted_monster_label.config(text=f"Targeted Monster: {targeted_monster if targeted_monster else 'None'}")

# Function to handle selecting a monster from the mobs listbox
def select_monster(event, mobs_listbox, targeted_monster_label):
    global targeted_monster
    try:
        selected_text = mobs_listbox.get(mobs_listbox.curselection())
        if "monster_" in selected_text:
            targeted_monster = selected_text.split(":")[1].strip()
            update_targeted_monster_display(targeted_monster_label)
    except tk.TclError:
        messagebox.showinfo("Selection Error", "Please select a monster from the list.")

# Create the main application window
def create_gui(username):
    window = tk.Tk()
    window.title("Chat Client")

    frame = tk.Frame(window)
    frame.grid(padx=10, pady=10)
    
    text_area = tk.Text(frame, wrap=tk.WORD, state=tk.DISABLED, width=50, height=15)
    text_area.grid(row=0, column=0, columnspan=10, padx=5, pady=5)

    users_listbox = Listbox(frame, width=20, height=15)
    users_listbox.grid(row=0, column=10, padx=5, pady=5, sticky='n')
    users_scrollbar = Scrollbar(frame, orient="vertical", command=users_listbox.yview)
    users_scrollbar.grid(row=0, column=11, sticky='ns')
    users_listbox.config(yscrollcommand=users_scrollbar.set)

    mobs_listbox = Listbox(frame, width=20, height=15)
    mobs_listbox.grid(row=0, column=12, padx=5, pady=5, sticky='n')
    mobs_scrollbar = Scrollbar(frame, orient="vertical", command=mobs_listbox.yview)
    mobs_scrollbar.grid(row=0, column=13, sticky='ns')
    mobs_listbox.config(yscrollcommand=mobs_scrollbar.set)

    targeted_monster_label = tk.Label(frame, text="Targeted Monster: None")
    targeted_monster_label.grid(row=1, column=0, columnspan=10, padx=5, pady=5)

    username_label = tk.Label(frame, text=username)
    username_label.grid(row=2, column=0, padx=(5, 0), pady=5)

    message_entry = tk.Entry(frame, width=40)
    message_entry.grid(row=2, column=1, columnspan=4, padx=5, pady=5)

    send_button = tk.Button(frame, text="Send", command=lambda: send_message(client_socket, message_entry, f"{username}: {message_entry.get()}"))
    send_button.grid(row=2, column=5, padx=5, pady=5)

    # Add 10 Use Skill buttons
    for i in range(10):
        use_skill_button = tk.Button(frame, text=f"Use Skill {i+1}", command=lambda i=i: send_message(client_socket, message_entry, f"use_skill_{i+1}"))
        use_skill_button.grid(row=3 + i // 5, column=i % 5, padx=5, pady=5)

    mobs_listbox.bind("<Double-Button-1>", lambda event: select_monster(event, mobs_listbox, targeted_monster_label))

    message_entry.bind("<Return>", lambda event: send_message(client_socket, message_entry, f"{username}: {message_entry.get()}"))

    host = '127.0.0.1'  # Server IP address
    port = 9999         # Server port

    client_socket = start_client(host, port, text_area, message_entry, users_listbox, mobs_listbox, username)

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