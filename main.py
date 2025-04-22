import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from PIL import Image, ImageDraw, ImageFont

root = tk.Tk()
    root.title("Watermarker")
    root.geometry("300x200")

    app = WatermarkerApp(root)
    root.mainloop()