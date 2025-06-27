from customtkinter import *
import math
import subprocess
import sys

set_appearance_mode("dark")
set_default_color_theme("blue")

app = CTk()
app.title("Calculator")
app.geometry("320x285")

entry = CTkEntry(app, width=320, height=60, font=("Arial", 24), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=1, pady=1)

def button_click(symbol):
    entry.insert("end", symbol)

def calculate_result():
    try:
        expression = entry.get()
        expression = expression.replace("^", "**")
        expression = expression.replace("%", "/100")
        result = eval(expression, {"__builtins__": None}, {"sqrt": math.sqrt,"pow": pow})
        entry.delete(0, "end")
        entry.insert(0, str(result))

    except:
        entry.delete(0, "end")
        entry.insert(0, "Error")

def clear_entry():
    entry.delete(0, "end")

def go_back():
    app.destroy()
    subprocess.call([sys.executable, "menu.py"])

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("√", 4, 2), ("+", 4, 3),
    ("%", 5, 0), ("^", 5, 1), ("(", 5, 2), (")", 5, 3),
    ("=", 6, 0)
]

for (text, row, col) in buttons:
    if text == "=":
        btn = CTkButton(app, text=text, width=100, height=25, command=calculate_result)
        btn.grid(row=row, column=col, columnspan=4, sticky="we", padx=1, pady=1)
    elif text == "√":
        btn = CTkButton(app, text=text, width=75, height=25, command=lambda: button_click("sqrt("))
        btn.grid(row=row, column=col, padx=1, pady=1, ipadx=1, ipady=1)
    else:
        btn = CTkButton(app, text=text, width=75, height=25, command=lambda t=text: button_click(t))
        btn.grid(row=row, column=col, padx=1, pady=1, ipadx=1, ipady=1)

clear_btn = CTkButton(app, text="C", command=clear_entry, fg_color="red", hover_color="darkred", width=100, height=25,)
clear_btn.grid(row=8, column=0, columnspan=4, sticky="we", padx=1, pady=1)

back_btn = CTkButton(app, text="◀️ Назад до меню", command=go_back)
back_btn.grid(row=7, column=0, columnspan=4, sticky="we", padx=1, pady=1)

app.mainloop()