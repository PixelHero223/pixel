import customtkinter as ctk
import subprocess
import sys

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.title("Меню")

        self.menu_width = 0
        self.menu_expanded = False

        self.side_menu = ctk.CTkFrame(self, width=0, height=300)
        self.side_menu.place(x=0, y=0)

        self.menu_button = ctk.CTkButton(self, text="▶️", width=40, command=self.toggle_menu)
        self.menu_button.place(x=0, y=0)

        self.name_entry = ctk.CTkEntry(self.side_menu, placeholder_text="Введіть назву програми", width=180)
        self.name_entry.place(x=10, y=50)

        self.launch_button = ctk.CTkButton(self.side_menu, text="Відкрити", command=self.launch_project, width=180)
        self.launch_button.place(x=10, y=100)

        label = ctk.CTkLabel(self.side_menu, text="Назви програм:\n- калькулятор\n- редактор\n- пароль\n- арт",justify="left")
        label.place(x=10, y=150)

    def toggle_menu(self):
        self.menu_expanded = not self.menu_expanded
        self.menu_button.configure(text="◀️" if self.menu_expanded else "▶️")
        self.animate_menu()

    def animate_menu(self):
        target_width = 200 if self.menu_expanded else 0
        step = 10 if self.menu_expanded else -10

        def step_animation():
            nonlocal step
            self.menu_width += step
            if (self.menu_expanded and self.menu_width >= target_width) or \
               (not self.menu_expanded and self.menu_width <= target_width):
                self.menu_width = target_width
                self.side_menu.configure(width=self.menu_width)
                return
            self.side_menu.configure(width=self.menu_width)
            self.after(10, step_animation)

        step_animation()

    def launch_project(self):
        name = self.name_entry.get().strip().lower()

        if name == "калькулятор":
            self.destroy()
            subprocess.call([sys.executable, "калькулятор.py"])
        elif name == "редактор":
            self.destroy()
            subprocess.call([sys.executable, "Easy Editor.py"])
        elif name == "пароль":
            self.destroy()
            subprocess.call([sys.executable, "генератор.py"])
        elif name == "арт":
            self.destroy()
            subprocess.call([sys.executable, "арт.py"])
        else:
            print("Невідомий проєкт:", name)


if __name__ == "__main__":
    app = App()
    app.mainloop()