import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            raise ValueError("Length too short.")
    except:
        messagebox.showerror("Invalid Input", "Enter a number (min 4).")
        return

    categories = []
    if var_upper.get():
        categories.append(string.ascii_uppercase)
    if var_lower.get():
        categories.append(string.ascii_lowercase)
    if var_digits.get():
        categories.append(string.digits)
    if var_symbols.get():
        categories.append(string.punctuation)

    if not categories:
        messagebox.showwarning(" No Selection", "Select at least one character type.")
        return

    password = [random.choice(group) for group in categories]

    all_chars = ''.join(categories)
    while len(password) < length:
        password.append(random.choice(all_chars))

    random.shuffle(password)
    final_password = ''.join(password)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, final_password)

def copy_password():
    pwd = password_entry.get()
    if pwd:
        root.clipboard_clear()
        root.clipboard_append(pwd)
        messagebox.showinfo("Copied", "Password copied to clipboard.")
    else:
        messagebox.showwarning("No Password", "Nothing to copy.")

root = tk.Tk()
root.title(" Mystic Password Generator")
root.geometry("450x520")
root.configure(bg="#0a043c") 


FONT_TITLE = ("Verdana", 16, "bold")
FONT_LABEL = ("Verdana", 11)
COLOR_ACCENT = "#9d00ff" 
COLOR_BTN = "#00c9a7"        


tk.Label(root, text=" Mystic Password Generator", font=FONT_TITLE,
         fg=COLOR_ACCENT, bg="#0a043c").pack(pady=20)


tk.Label(root, text="Password Length:", font=FONT_LABEL, fg="white", bg="#0a043c").pack()
length_entry = tk.Entry(root, font=("Courier", 13), justify="center", bg="#1f1f2e", fg="white", width=10)
length_entry.pack(pady=8)

var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=False)

options_frame = tk.Frame(root, bg="#0a043c")
options_frame.pack(pady=10)

tk.Checkbutton(options_frame, text="Uppercase A-Z",variable=var_upper, font=FONT_LABEL,
          bg="#0a043c", fg="#9d00ff", activebackground="#1f1f2e").pack(anchor='w')
tk.Checkbutton(options_frame, text="Lowercase a-z" ,variable=var_lower, font=FONT_LABEL,
               bg="#0a043c", fg="#9d00ff", activebackground="#1f1f2e").pack(anchor='w')
tk.Checkbutton(options_frame, text="Numbers 0-9", variable=var_digits, font=FONT_LABEL,
               bg="#0a043c", fg="#9d00ff", activebackground="#1f1f2e").pack(anchor='w')
tk.Checkbutton(options_frame, text="Symbols !@#", variable=var_symbols, font=FONT_LABEL,
               bg="#0a043c", fg="#9d00ff", activebackground="#1f1f2e").pack(anchor='w')

tk.Button(root, text="🔮 Generate Password", command=generate_password,
          font=FONT_LABEL, bg=COLOR_BTN, fg="black", width=25).pack(pady=20)

password_entry = tk.Entry(root, font=("Courier New", 14), bg="#1f1f2e", fg="#33ffcc",
                          justify="center", width=30, relief=tk.FLAT)
password_entry.pack(pady=10)


tk.Button(root, text="📋 Copy to Clipboard", command=copy_password,
          font=FONT_LABEL, bg=COLOR_ACCENT, fg="white", width=25).pack(pady=10)


tk.Label(root, text="Developed with in Python", bg="#0a043c", fg="#606060",
         font=("Arial", 9)).pack(side="bottom", pady=10)

root.mainloop()
