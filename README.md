# Image Watermarking Desktop App
A simple desktop program for uploading images and adding a flexible watermark (text or logo).

## 🚀 Features

- **Select Base Image** via file dialog (supports PNG, JPEG, BMP).
- **Optional Logo Overlay**: automatically resizes (10% of image width using LANCZOS resampling) and positions your logo in the bottom‑right corner, with graceful fallback if the logo can’t be loaded.
- **Text Watermark**: enter custom text, auto‑scaled to ~5% of image width (minimum 12px), with built‑in fallback font if your chosen TTF is unavailable.
- **Dynamic Text Color**: image is analyzed to compute average brightness—light backgrounds get semi‑transparent black text, dark backgrounds get semi‑transparent white text.
- **Adjustable Opacity**: all text and logo overlays use semi‑transparency (alpha=128) for professional, non‑intrusive watermarks.
- **Error Handling**: friendly dialogs catch image/load/save errors instead of crashing.
- **Compatibility**: fully compatible with Pillow 10+ (detects and uses the correct resampling constant).
- **Save As** JPEG or PNG to any folder of your choice.

## ⚙️ Usage

1. Click **Select Image** and choose your file.
2. (Optional) Click **Select Logo** to overlay a graphic watermark.
3. Click **Enter Watermark Text** to type in your watermark.
4. Click **Apply & Save**, then choose output format and destination.

## 📦 Project Structure

```
.
├── main.py               # Launches the Tkinter GUI window
└── watermarker_app.py    # Core watermarking logic and GUI controls
```

- **main.py**: Initializes the Tkinter root window and starts the app.
- **watermarker_app.py**:
  - `select_image()` – File dialog for base image.
  - `select_logo()` – Optional file dialog for logo image.
  - `enter_text()` – Prompt for watermark text.
  - `apply_and_save()` –
    - Opens and converts images to RGBA.
    - Computes average brightness for dynamic text coloring.
    - Resizes logo with LANCZOS resampling and applies it.
    - Scales and draws text with fallback font and correct opacity.
    - Composites watermark layer and saves result with error checks.

## ✏️ Customization

- **Watermark Position & Size**: edit the `logo_w = int(width * 0.1)` and `font_size = max(12, int(width / 20))` lines in `apply_and_save()`.
- **Fonts**: swap out `"arial.ttf"` for any TTF path, or modify the fallback in the exception block.
- **Opacity & Color**: change the alpha channel in `fill=(R, G, B, alpha)` or adjust the brightness threshold (default 127) for text color.
- **Error Messages**: customize the `messagebox` text for more context.

---

