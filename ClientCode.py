import socket
import threading
import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar, END
import argparse
from PIL import Image, ImageTk
from InventoryManager import InventoryManager

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
                clients = message.split('\n')[1:]
                for client in clients:
                    users_listbox.insert(END, client)
            elif message.startswith("Connected mobs:"):
                mobs_listbox.delete(0, END)
                mobs = message.split('\n')[1:]
                for mob in mobs:
                    mobs_listbox.insert(END, mob)
            elif "Welcome" in message:  # Handle welcome messages separately
                text_area.config(state=tk.NORMAL)
                text_area.insert(tk.END, f"{message}\n")
                text_area.config(state=tk.DISABLED)
                text_area.see(tk.END)
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

        # Automatically send a login message
        login_message = f"{username}: login"
        send_message(client_socket, message_entry, login_message)

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
        targeted_monster = selected_text
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

    def create_inventory_grid(frame, inventory_manager, username):
        inventory_frame = tk.Frame(frame, relief=tk.RAISED, bd=2)
        inventory_frame.grid(row=4, column=5, columnspan=10, padx=5, pady=5)

        inventory_label = tk.Label(inventory_frame, text="Inventory:")
        inventory_label.grid(row=0, column=0, columnspan=5)

        icons = {}
    
        def add_item_to_inventory(item):
            inventory_manager.add_item(username, item)
            update_inventory_grid()

        def remove_item_from_inventory(item):
            inventory_manager.remove_item(username, item)
            update_inventory_grid()

        def update_inventory_grid():
            for widget in inventory_frame.winfo_children():
                if isinstance(widget, tk.Button):
                    widget.destroy()
                    
            inventory = inventory_manager.view_inventory(username)
            for index, item in enumerate(inventory):
                icon = icons.get(item, None)
                if not icon:
                    # Create a placeholder icon for the item
                    image = Image.new('RGB', (50, 50), color = 'gray')
                    icon = ImageTk.PhotoImage(image)
                    icons[item] = icon

                item_button = tk.Button(inventory_frame, image=icon, command=lambda item=item: remove_item_from_inventory(item))
                item_button.grid(row=(index // 5) + 1, column=index % 5, padx=5, pady=5)

        add_item_button = tk.Button(inventory_frame, text="Add Item", command=lambda: add_item_to_inventory("New Item"))
        add_item_button.grid(row=1, column=6, padx=5, pady=5)

        update_inventory_grid()
    
    # Initialize InventoryManager and create inventory grid
    inventory_manager = InventoryManager()
    create_inventory_grid(frame, inventory_manager, username)
    
    window.mainloop()

# Run the GUI application
if __name__ == "__main__":
    args = parse_arguments()
    create_gui(args.name)