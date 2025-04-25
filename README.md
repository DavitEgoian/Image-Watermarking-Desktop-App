# Image-Watermarking-Desktop-App
A Desktop program where you can upload images and add a watermark.

## 🚀 Features

- **Select Base Image** via file dialog (supports PNG, JPEG, BMP).  
- **Optional Logo Overlay**: automatically resizes and positions your logo in the bottom-right corner.  
- **Text Watermark**: choose custom text, auto-scaled to image width, with built-in fallback font.  
- **Adjustable Opacity**: semi-transparent text watermark for professional results.  
- **Save As** JPEG or PNG to any location.

## ⚙️ Usage

 - Click **Select Image** and choose your file.  
 - (Optional) **Select Logo** to overlay a graphic watermark.  
 - Click **Enter Watermark Text** to add a semi-transparent label.  
 - Click **Apply & Save**, choose output format and location.

## 📦 Project Structure

```
.
├── main.py               # Launches the Tkinter window
└── watermarker_app.py    # Core watermarking logic and GUI controls
```

- **main.py**: Initializes the Tkinter root window and starts the app.  
- **watermarker_app.py**:  
  - `select_image()` – Opens file dialog to pick the base image.  
  - `select_logo()` – Opens file dialog to pick an optional logo.  
  - `enter_text()`  – Prompts for watermark text.  
  - `apply_and_save()` – Composites watermark over image and saves result.

## ✏️ Customization

- **Watermark Position & Size**: Modify logo scaling factor (default 10% of image width) and text font-size divisor in `apply_and_save()`.  
- **Fonts**: Change `"arial.ttf"` to any TTF font file or adjust fallback in the exception block.  
- **Opacity & Color**: Adjust the RGBA tuple for `draw.text(..., fill=(255,255,255,128))` to tweak transparency or color.  
3. Commit your changes (`git commit -m "Add amazing watermark options"`).  
4. Push to the branch (`git push origin feature/YourFeature`).  
5. Open a Pull Request and describe your enhancements.

---
