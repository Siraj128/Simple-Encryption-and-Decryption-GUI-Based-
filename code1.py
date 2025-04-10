import random
import string
import json
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk 

# File to store encryption mapping
MAPPING_FILE = "mapping.json"

# Function to load existing mapping or create a new one
def load_or_generate_mapping():
    try:
        with open(MAPPING_FILE, "r") as f:
            data = json.load(f)
            return data["current_msg"], data["Logic_msg"]
    except (FileNotFoundError, json.JSONDecodeError):
        # Generate new mapping if file doesn't exist
        current_msg = " " + string.punctuation + string.digits + string.ascii_letters
        current_msg = list(current_msg)
        Logic_msg = current_msg.copy()
        random.shuffle(Logic_msg)

        # Save mapping to file
        with open(MAPPING_FILE, "w") as f:
            json.dump({"current_msg": current_msg, "Logic_msg": Logic_msg}, f)

        return current_msg, Logic_msg

# Load or generate encryption mapping
current_msg, Logic_msg = load_or_generate_mapping()

# Encryption function
def encrypt():
    text = entry_encrypt.get()
    encrypt_msg = ""

    try:
        for i in text:
            index = current_msg.index(i)
            encrypt_msg += Logic_msg[index]
        entry_encrypted.config(state=tk.NORMAL)
        entry_encrypted.delete(0, tk.END)
        entry_encrypted.insert(0, encrypt_msg)
        entry_encrypted.config(state=tk.DISABLED)
    except ValueError:
        messagebox.showerror("Error", "Invalid characters in input!")

# Decryption function
def decrypt():
    encrypted_text = entry_decrypt.get()
    decrypt_msg = ""

    try:
        for j in encrypted_text:
            index = Logic_msg.index(j)
            decrypt_msg += current_msg[index]
        entry_decrypted.config(state=tk.NORMAL)
        entry_decrypted.delete(0, tk.END)
        entry_decrypted.insert(0, decrypt_msg)
        entry_decrypted.config(state=tk.DISABLED)
    except ValueError:
        messagebox.showerror("Error", "Invalid characters in input!")

# Create GUI window
root = tk.Tk()
root.title("Encryption & Decryption Tool")
root.geometry("600x400")

# Setting background image
bg_image = Image.open("background.jpg")  # Replace with your own image
bg_image = bg_image.resize((700, 500), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)  # Set background image

frame = tk.Frame(root, bg="white", padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Encrypt Section
tk.Label(frame, text="Enter message to encrypt:", font=("Arial", 12), bg="white").pack(pady=5)
entry_encrypt = tk.Entry(frame, width=50, font=("Arial", 12))
entry_encrypt.pack()

tk.Button(frame, text="Encrypt", command=encrypt, font=("Arial", 12, "bold"), bg="blue", fg="white", padx=10, pady=5).pack(pady=5)

tk.Label(frame, text="Encrypted message:", font=("Arial", 12), bg="white").pack()
entry_encrypted = tk.Entry(frame, width=50, font=("Arial", 12), state=tk.DISABLED)
entry_encrypted.pack()

# Decrypt Section
tk.Label(frame, text="Enter message to decrypt:", font=("Arial", 12), bg="white").pack(pady=5)
entry_decrypt = tk.Entry(frame, width=50, font=("Arial", 12))
entry_decrypt.pack()

tk.Button(frame, text="Decrypt", command=decrypt, font=("Arial", 12, "bold"), bg="green", fg="white", padx=10, pady=5).pack(pady=5)

tk.Label(frame, text="Decrypted message:", font=("Arial", 12), bg="white").pack()
entry_decrypted = tk.Entry(frame, width=50, font=("Arial", 12), state=tk.DISABLED)
entry_decrypted.pack()

root.mainloop()