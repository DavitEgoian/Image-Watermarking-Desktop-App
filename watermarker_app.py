import os
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

        # Open base image
        try:
            base = Image.open(self.img_path).convert("RGBA")
        except Exception as e:
            messagebox.showerror("Error", f"Could not open image:\n{e}")
            return

        width, height = base.size

        # Prepare watermark layer
        watermark_layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(watermark_layer)

        # Determine average brightness for text color
        grayscale = base.convert("L")
        hist = grayscale.histogram()
        total_pixels = sum(hist)
        avg_brightness = sum(i * count for i, count in enumerate(hist)) / total_pixels
        # If image is mostly light, use black text; else use white text
        text_color = (0, 0, 0, 128) if avg_brightness > 127 else (255, 255, 255, 128)

        # Paste logo if provided
        if self.logo_path:
            try:
                logo = Image.open(self.logo_path).convert("RGBA")
            except Exception as e:
                messagebox.showwarning("Warning", f"Could not open logo, skipping:\n{e}")
            else:
                try:
                    resample = Image.Resampling.LANCZOS
                except AttributeError:
                    resample = Image.LANCZOS

                logo_ratio = logo.width / logo.height
                logo_w = int(width * 0.1)
                logo_h = int(logo_w / logo_ratio)
                logo = logo.resize((logo_w, logo_h), resample)

                pos = (width - logo_w - 10, height - logo_h - 10)
                watermark_layer.paste(logo, pos, logo)

        # Draw text if provided
        if self.text:
            font_size = max(12, int(width / 20))
            try:
                font = ImageFont.truetype("arial.ttf", font_size)
            except IOError:
                font = ImageFont.load_default()

            # Measure text size
            try:
                bbox = draw.textbbox((0, 0), self.text, font=font)
                text_w = bbox[2] - bbox[0]
                text_h = bbox[3] - bbox[1]
            except AttributeError:
                text_w, text_h = draw.textsize(self.text, font=font)

            text_pos = (width - text_w - 10, height - text_h - 10)
            draw.text(text_pos, self.text, font=font, fill=text_color)

        # Composite and save
        result = Image.alpha_composite(base, watermark_layer).convert("RGB")
        save_path = filedialog.asksaveasfilename(
            defaultextension=".jpg",
            filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")],
        )
        if save_path:
            try:
                result.save(save_path)
                messagebox.showinfo("Saved", f"Watermarked image saved to:\n{save_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save image:\n{e}")
