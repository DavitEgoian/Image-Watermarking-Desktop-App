import tkinter as tk
from watermarker_app import WatermarkerApp

def main():
    root = tk.Tk()
    root.title("Watermarker")
    root.geometry("300x200")

    app = WatermarkerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()