import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import Separate_Pictures as sp

filetypes = [
        ("AV1 Image File Format", "*.avif"),
        ("Windows Bitmap", "*.bmp *.dib"),
        ("CompuServe Graphics Interchange Format", "*.gif"),
        ("JPEG", "*.jpg *.jpeg *.jpe *.jfif"),
        ("JPEG 2000", "*.jp2 *.j2k *.jpc *.jpf *.jpx *.j2c"),
        ("Portable Network Graphics", "*.png"),
        ("WebP", "*.webp"),
        ("Tagged Image File Format", "*.tiff *.tif"),
        ("Portable Pixmap", "*.pbm *.pgm *.ppm *.pnm"),
        ("Targa", "*.tga"),
        ("PC Paintbrush", "*.pcx"),
        ("SGI Image File", "*.sgi *.rgb *.rgba *.bw"),
        ("Sun Raster File", "*.ras"),
        ("Encapsulated PostScript", "*.eps *.ps"),
        ("DirectDraw Surface", "*.dds"),
        ("Blizzard Texture Format", "*.blp"),
        ("FITS", "*.fit *.fits"),
        ("Flexible Image Transport System", "*.fts"),
        ("GRIB", "*.grib"),
        ("HDF5", "*.h5 *.hdf"),
        ("ICO (Windows Icon)", "*.ico"),
        ("ICNS (macOS Icon)", "*.icns"),
        ("IM Image", "*.im"),
        ("IPTC/NAA", "*.iim"),
        ("JPEG XR", "*.jxr *.hdp *.wdp"),
        ("MCIDAS Area File", "*.mcidas"),
        ("Microsoft Paint", "*.msp"),
        ("Multi Picture Object", "*.mpo"),
        ("Palm Image", "*.palm"),
        ("PDF", "*.pdf"),
        ("Photoshop Document", "*.psd"),
        ("QOI (Quite OK Image)", "*.qoi"),
        ("SPIDER", "*.spi"),
        ("Truevision TGA", "*.tga"),
        ("X Bitmap", "*.xbm"),
        ("X PixMap", "*.xpm"),
        ("XV Thumbnail Image", "*.xv"),
        ("BUFR", "*.bufr"),
        ("CUR (Windows Cursor)", "*.cur"),
        ("DCX", "*.dcx"),
        ("FLI/FLC Animation", "*.fli *.flc"),
        ("FPX (FlashPix)", "*.fpx"),
        ("GBR (GIMP Brush)", "*.gbr"),
        ("GD", "*.gd"),
        ("IMT", "*.imt"),
        ("IPTC", "*.iptc"),
        ("MPEG Thumbnail", "*.mpeg"),
        ("PIXAR", "*.pxr"),
        ("Walnut Creek MAP", "*.map"),
        ("Portable Float Map", "*.pfm"),
        ("All Files", "*.*")
    ]
filename = ""

def populate_window(window):
    window.rowconfigure(0, weight = 1)
    window.rowconfigure(1, weight = 1)
    window.columnconfigure(0, weight = 1)

    filename = ""
    select_file_button = ttk.Button(window, text="Select File", command=select_file)
    select_file_button.grid(column=0, row=0, sticky=tk.EW, padx=5, pady=5)

    run_button = ttk.Button(window, text="Run!", command=run)
    run_button.grid(column=0, row=1, sticky=tk.EW, padx=5, pady=5)

def select_file():
    global filename
    filename = filedialog.askopenfilename(filetypes=filetypes)

def run():
    global filename
    cropped_images = sp.crop_image(filename)
    sp.show_images(cropped_images)

window = tk.Tk()
window.title("Pictures Separators")
populate_window(window)


window.mainloop()