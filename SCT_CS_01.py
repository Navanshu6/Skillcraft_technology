import tkinter as tk
from tkinter import messagebox

# =========================
# Caesar Cipher Functions
# =========================

def encrypt_text(message, shift_amount):
    """
    Encrypts the given message using Caesar Cipher.
    Only letters are shifted; other characters remain unchanged.
    """
    result = ""
    for char in message:
        if char.isalpha():  # Only letters
            ascii_base = 65 if char.isupper() else 97
            # Shift character and wrap around using modulo 26
            shifted_char = chr((ord(char) - ascii_base + shift_amount) % 26 + ascii_base)
            result += shifted_char
        else:
            result += char  # Non-letter characters remain same
    return result

def decrypt_text(message, shift_amount):
    """
    Decrypts the message by using negative shift.
    """
    return encrypt_text(message, -shift_amount)

# =========================
# GUI Functions
# =========================

def handle_encrypt():
    """Triggered when Encrypt button is clicked."""
    text = input_message.get()
    try:
        shift = int(input_shift.get())
        encrypted = encrypt_text(text, shift)
        output_var.set(encrypted)
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be a number!")

def handle_decrypt():
    """Triggered when Decrypt button is clicked."""
    text = input_message.get()
    try:
        shift = int(input_shift.get())
        decrypted = decrypt_text(text, shift)
        output_var.set(decrypted)
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be a number!")

# =========================
# GUI Setup
# =========================

root = tk.Tk()
root.title("Caesar Cipher Tool")

# ----- Input Message -----
tk.Label(root, text="Enter your message:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
input_message = tk.Entry(root, width=50)
input_message.grid(row=0, column=1, padx=5, pady=5)

# ----- Shift Value -----
tk.Label(root, text="Shift value:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
input_shift = tk.Entry(root, width=10)
input_shift.grid(row=1, column=1, padx=5, pady=5, sticky='w')

# ----- Buttons -----
tk.Button(root, text="Encrypt", command=handle_encrypt).grid(row=2, column=0, padx=5, pady=10)
tk.Button(root, text="Decrypt", command=handle_decrypt).grid(row=2, column=1, padx=5, pady=10, sticky='w')

# ----- Output -----
tk.Label(root, text="Result:").grid(row=3, column=0, padx=5, pady=5, sticky='e')
output_var = tk.StringVar()
tk.Entry(root, textvariable=output_var, width=50, state='readonly').grid(row=3, column=1, padx=5, pady=5)

# Run the GUI loop
root.mainloop()
