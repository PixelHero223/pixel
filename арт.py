import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageEnhance, ImageFilter
import subprocess
import sys

ctk.set_appearance_mode("system")

class ArtPixelLab(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Art Pixel Lab")
        self.geometry("1100x600")
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)

        ctk.CTkButton(self, text="Вибрати файл", command=self.load_from_file).grid(row=0, column=0, padx=5)

        self.original_label = ctk.CTkLabel(self, text="Оригінал")
        self.original_label.grid(row=1, column=0, padx=10, pady=10)

        self.minecraft_label = ctk.CTkLabel(self, text="Minecraft")
        self.minecraft_label.grid(row=1, column=1, padx=10, pady=10)

        self.popart_label = ctk.CTkLabel(self, text="Pop Art")
        self.popart_label.grid(row=1, column=2, padx=10, pady=10)

        self.embroidery_label = ctk.CTkLabel(self, text="Вишивка")
        self.embroidery_label.grid(row=1, column=3, padx=10, pady=10)

        back_btn = ctk.CTkButton(self, text="◀️ Назад до меню", command=self.go_back)
        back_btn.grid(row=2, column=0, columnspan=4, pady=20)

    def load_from_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            img = Image.open(file_path)
            self.show_styles(img)

    def show_styles(self, img):
        img = img.convert("RGB")
        resized = img.resize((256, 256))

        original_tk = ImageTk.PhotoImage(resized)
        self.original_label.configure(image=original_tk)
        self.original_label.image = original_tk

        pixel = resized.resize((16, 16), resample=Image.NEAREST)
        pixelated = pixel.resize((256, 256), Image.NEAREST)
        pixel_tk = ImageTk.PhotoImage(pixelated)
        self.minecraft_label.configure(image=pixel_tk)
        self.minecraft_label.image = pixel_tk

        enhancer1 = ImageEnhance.Color(resized).enhance(2.5)
        enhancer2 = ImageEnhance.Contrast(enhancer1).enhance(1.8)
        popart_tk = ImageTk.PhotoImage(enhancer2)
        self.popart_label.configure(image=popart_tk)
        self.popart_label.image = popart_tk

        embroidery = resized.filter(ImageFilter.CONTOUR)
        embroidery_tk = ImageTk.PhotoImage(embroidery)
        self.embroidery_label.configure(image=embroidery_tk)
        self.embroidery_label.image = embroidery_tk

    def go_back(self):
        self.destroy()
        subprocess.call([sys.executable, "menu.py"])

if __name__ == "__main__":
    app = ArtPixelLab()
    app.mainloop()