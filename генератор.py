import string
from tkinter import messagebox
from customtkinter import *
import random
import subprocess
import sys

set_appearance_mode("dark")
set_default_color_theme("blue")

app = CTk()
app.title("Генератор паролів")
app.geometry("400x500")

def generate_password():
    length = int(slider.get())
    use_lower = lower_var.get()
    use_upper = upper_var.get()
    use_digits = digits_var.get()
    use_special = special_var.get()

    characters = ""

    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    if not characters:
        messagebox.showerror("Помилка", "Оберіть хоча б одну категорію символів!")
        return

    password = "".join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, 'end')
    password_entry.insert(0, password)
    length_label.configure(text=f"Довжина: {len(password)}")

def copy_password():
    password = password_entry.get()
    if password:
        app.clipboard_clear()
        app.clipboard_append(password)
        messagebox.showinfo("Скопійовано", "Пароль скопійовано в буфер обміну!")

def go_back():
    app.destroy()
    subprocess.call([sys.executable, "menu.py"])

password_entry = CTkEntry(app, width=300, height=40, font=("Arial", 16))
password_entry.pack(pady=20)

lower_var = IntVar(value=1)
upper_var = IntVar(value=1)
digits_var = IntVar(value=1)
special_var = IntVar(value=0)

checkbox_frame = CTkFrame(app)
checkbox_frame.pack(pady=10)

lower_cb = CTkCheckBox(checkbox_frame, text="Малі літери (a-z)", variable=lower_var)
lower_cb.grid(row=0, column=0, sticky="w", padx=10, pady=5)

upper_cb = CTkCheckBox(checkbox_frame, text="Великі літери (A-Z)", variable=upper_var)
upper_cb.grid(row=1, column=0, sticky="w", padx=10, pady=5)

digits_cb = CTkCheckBox(checkbox_frame, text="Цифри (0-9)", variable=digits_var)
digits_cb.grid(row=2, column=0, sticky="w", padx=10, pady=5)

special_cb = CTkCheckBox(checkbox_frame, text="Спецсимволи (!@#$...)", variable=special_var)
special_cb.grid(row=3, column=0, sticky="w", padx=10, pady=5)

CTkLabel(app, text="Довжина пароля:").pack(pady=(10, 0))
slider = CTkSlider(app, from_=4, to=64, number_of_steps=60, orientation="horizontal")
slider.set(12)
slider.pack(pady=10)

length_label = CTkLabel(app, text="Довжина: 12")
length_label.pack()

generate_btn = CTkButton(app, text="Згенерувати", command=generate_password)
generate_btn.pack(pady=10)

copy_btn = CTkButton(app, text="📋 Копіювати", command=copy_password)
copy_btn.pack(pady=5)

back_btn = CTkButton(app, text="◀️ Назад до меню", command=go_back)
back_btn.pack(pady=15)

app.mainloop()