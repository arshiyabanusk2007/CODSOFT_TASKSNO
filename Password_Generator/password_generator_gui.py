
import tkinter as tk
from tkinter import messagebox
import secrets
import string

# Main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("500x600")
root.resizable(False, False)
root.configure(bg="#101827")

# Title
tk.Label(
    root,
    text="PASSWORD GENERATOR",
    font=("Arial", 22, "bold"),
    fg="white",
    bg="#101827"
).pack(pady=(35, 8))

tk.Label(
    root,
    text="Create a strong and secure password",
    font=("Arial", 11),
    fg="#AAB5C5",
    bg="#101827"
).pack(pady=(0, 30))

# Password display
password_var = tk.StringVar()

password_entry = tk.Entry(
    root,
    textvariable=password_var,
    font=("Consolas", 15),
    justify="center",
    bg="#202C3D",
    fg="#FFFFFF",
    insertbackground="white",
    bd=0,
    readonlybackground="#202C3D",
    state="readonly"
)
password_entry.pack(fill="x", padx=35, ipady=15)

# Password length
tk.Label(
    root,
    text="Password Length",
    font=("Arial", 13, "bold"),
    fg="white",
    bg="#101827"
).pack(pady=(30, 8))

length_var = tk.IntVar(value=12)

length_display = tk.Label(
    root,
    text="12",
    font=("Arial", 16, "bold"),
    fg="#20D99A",
    bg="#101827"
)
length_display.pack()

def update_length(value):
    length_display.config(text=str(int(float(value))))

length_slider = tk.Scale(
    root,
    from_=8,
    to=32,
    orient="horizontal",
    variable=length_var,
    command=update_length,
    bg="#101827",
    fg="white",
    troughcolor="#20D99A",
    highlightthickness=0,
    bd=0,
    length=400
)
length_slider.pack(pady=5)

# Character options
tk.Label(
    root,
    text="Include Characters",
    font=("Arial", 13, "bold"),
    fg="white",
    bg="#101827"
).pack(pady=(20, 10))

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
number_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)

options = [
    ("Uppercase (A-Z)", upper_var),
    ("Lowercase (a-z)", lower_var),
    ("Numbers (0-9)", number_var),
    ("Symbols (!@#$)", symbol_var)
]

for text, variable in options:
    tk.Checkbutton(
        root,
        text=text,
        variable=variable,
        font=("Arial", 11),
        fg="white",
        bg="#101827",
        activebackground="#101827",
        activeforeground="#20D99A",
        selectcolor="#202C3D"
    ).pack(anchor="w", padx=65, pady=2)

# Generate password
def generate_password():
    characters = ""

    if upper_var.get():
        characters += string.ascii_uppercase
    if lower_var.get():
        characters += string.ascii_lowercase
    if number_var.get():
        characters += string.digits
    if symbol_var.get():
        characters += string.punctuation

    if not characters:
        messagebox.showwarning(
            "Warning",
            "Please select at least one character type!"
        )
        return

    length = length_var.get()

    # Ensure every selected character type appears
    selected_groups = []

    if upper_var.get():
        selected_groups.append(string.ascii_uppercase)
    if lower_var.get():
        selected_groups.append(string.ascii_lowercase)
    if number_var.get():
        selected_groups.append(string.digits)
    if symbol_var.get():
        selected_groups.append(string.punctuation)

    if length < len(selected_groups):
        messagebox.showwarning(
            "Warning",
            "Password length is too short for selected options!"
        )
        return

    password_chars = [
        secrets.choice(group) for group in selected_groups
    ]

    password_chars += [
        secrets.choice(characters)
        for _ in range(length - len(password_chars))
    ]

    secrets.SystemRandom().shuffle(password_chars)

    password_var.set("".join(password_chars))


# Copy password
def copy_password():
    password = password_var.get()

    if not password:
        messagebox.showwarning(
            "Warning",
            "Generate a password first!"
        )
        return

    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Copied", "Password copied successfully!")


# Buttons
tk.Button(
    root,
    text="GENERATE PASSWORD",
    command=generate_password,
    font=("Arial", 12, "bold"),
    bg="#20D99A",
    fg="#101827",
    activebackground="#17B886",
    bd=0,
    cursor="hand2"
).pack(fill="x", padx=35, pady=(25, 10), ipady=13)

tk.Button(
    root,
    text="COPY PASSWORD",
    command=copy_password,
    font=("Arial", 11, "bold"),
    bg="#26364B",
    fg="white",
    activebackground="#34465D",
    bd=0,
    cursor="hand2"
).pack(fill="x", padx=35, ipady=12)

tk.Label(
    root,
    text="Stay Safe • Use Strong Passwords",
    font=("Arial", 9),
    fg="#8190A5",
    bg="#101827"
).pack(pady=20)

root.mainloop()
