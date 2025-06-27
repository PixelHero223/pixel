import customtkinter as ctk
from tkinter import filedialog
from PIL import ImageFilter, ImageTk, ImageEnhance, Image
import subprocess
import sys

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class SimpleImageEditor(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Редактор зображень")
        self.geometry("900x650")  # трішки збільшив висоту

        self.image = None
        self.display_image = None
        self.original_image = None

        # Ліва панель з кнопками
        self.controls_frame = ctk.CTkFrame(self, width=200)
        self.controls_frame.pack(side="left", fill="y", padx=10, pady=10)

        self.open_button = ctk.CTkButton(self.controls_frame, text="Відкрити зображення", command=self.open_image)
        self.open_button.pack(pady=10)

        self.rotate_button = ctk.CTkButton(self.controls_frame, text="Повернути 90°", command=self.rotate_image)
        self.rotate_button.pack(pady=10)

        self.gray_button = ctk.CTkButton(self.controls_frame, text="Чорно-білий", command=self.convert_to_grayscale)
        self.gray_button.pack(pady=10)

        self.blur_button = ctk.CTkButton(self.controls_frame, text="Розмиття", command=self.blur_image)
        self.blur_button.pack(pady=10)

        self.contrast_slider = ctk.CTkSlider(self.controls_frame, from_=0.5, to=2.0, number_of_steps=30, command=self.adjust_contrast)
        self.contrast_slider.set(1.0)
        self.contrast_slider.pack(pady=20)
        ctk.CTkLabel(self.controls_frame, text="Контрастність").pack()

        # Мітка для зображення
        self.image_label = ctk.CTkLabel(self, text="")
        self.image_label.pack(side="right", padx=20, pady=20, expand=True)

        # Нижня панель для кнопки Назад
        self.bottom_frame = ctk.CTkFrame(self)
        self.bottom_frame.pack(side="bottom", fill="x", pady=5)

        back_btn = ctk.CTkButton(self.bottom_frame, text="◀️ Назад до меню", command=self.go_back)
        back_btn.pack(pady=5)

    def go_back(self):
        self.destroy()
        subprocess.call([sys.executable, "menu.py"])

    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Images", "*.png *.jpg *.jpeg *.bmp *.gif")])
        if file_path:
            self.image = Image.open(file_path).convert("RGB")
            self.original_image = self.image.copy()
            self.display_image_on_label()

    def display_image_on_label(self):
        if self.image:
            resized = self.image.resize((500, 500), Image.Resampling.LANCZOS)
            self.display_image = ImageTk.PhotoImage(resized)
            self.image_label.configure(image=self.display_image)
            self.image_label.image = self.display_image

    def rotate_image(self):
        if self.image:
            self.image = self.image.rotate(-90, expand=True)
            self.display_image_on_label()

    def convert_to_grayscale(self):
        if self.image:
            self.image = self.image.convert("L").convert("RGB")
            self.display_image_on_label()

    def blur_image(self):
        if self.image:
            self.image = self.image.filter(ImageFilter.BLUR)
            self.display_image_on_label()

    def adjust_contrast(self, value):
        if self.image and self.original_image:
            enhancer = ImageEnhance.Contrast(self.original_image)
            self.image = enhancer.enhance(float(value))
            self.display_image_on_label()

if __name__ == "__main__":
    app = SimpleImageEditor()
    app.mainloop()