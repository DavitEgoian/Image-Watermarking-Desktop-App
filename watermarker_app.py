import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from PIL import Image, ImageDraw, ImageFont

class WatermarkerApp:
    def __init__(self, master):
        self.master = master
        self.img_path = None
        self.logo_path = None
        self.text = None

        # Buttons
        tk.Button(master, text="Select Image", command=self.select_image).pack(pady=5)
        tk.Button(master, text="Select Logo (optional)", command=self.select_logo).pack(pady=5)
        tk.Button(master, text="Enter Watermark Text", command=self.enter_text).pack(pady=5)
        tk.Button(master, text="Apply & Save", command=self.apply_and_save).pack(pady=5)

    def select_image(self):
        path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")]
        )
        if path:
            self.img_path = path
            messagebox.showinfo("Selected", f"Image: {path}")

    def select_logo(self):
        path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")]
        )
        if path:
            self.logo_path = path
            messagebox.showinfo("Selected", f"Logo: {path}")

    def enter_text(self):
        text = simpledialog.askstring("Watermark Text", "Enter watermark text:")
        if text:
            self.text = text

    def apply_and_save(self):
        if not self.img_path:
            messagebox.showerror("Error", "No input image selected.")
            return

        base = Image.open(self.img_path).convert("RGBA")
        width, height = base.size

        watermark_layer = Image.new("RGBA", base.size, (0,0,0,0))
        draw = ImageDraw.Draw(watermark_layer)

        if self.logo_path:
            logo = Image.open(self.logo_path).convert("RGBA")
            logo_ratio = logo.width / logo.height
            logo_width = int(width * 0.1)
            logo_height = int(logo_width / logo_ratio)
            logo = logo.resize((logo_width, logo_height), Image.ANTIALIAS)
            pos = (width - logo_width - 10, height - logo_height - 10)
            watermark_layer.paste(logo, pos, logo)

        if self.text:
            font_size = int(width / 20)
            try:
                font = ImageFont.truetype("arial.ttf", font_size)
            except IOError:
                font = ImageFont.load_default()
            text_width, text_height = draw.textsize(self.text, font=font)
            text_pos = (width - text_width - 10, height - text_height - 10)
            draw.text(text_pos, self.text, font=font, fill=(255,255,255,128))

        result = Image.alpha_composite(base, watermark_layer).convert("RGB")
        save_path = filedialog.asksaveasfilename(
            defaultextension=".jpg",
            filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")]
        )
        if save_path:
            result.save(save_path)
            messagebox.showinfo("Saved", f"Watermarked image saved to {save_path}")