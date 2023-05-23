from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *
from PIL import Image, ImageTk

# Data
data_hunians = [
    Apartemen("Nelly Joy", 3, 3),
    Rumah("Sekar MK", 5, 2),
    Indekos("Bp. Romi", "Cahya"),
    Rumah("Satria", 1, 4)
]

# List
hunians = []

# Halaman root
root = Tk()
root.title("Praktikum DPBO Python")
root.withdraw()

# Halaman Welcome Page
welcome_page = Toplevel(root)
welcome_page.title("Welcome")

# Untuk membuka halaman root
def move_to_root():
    welcome_page.destroy()
    root.deiconify()

# Untuk menampilkan gambar
def display_image(page, image_path, w, h):
    # Load the image
    welcome_image = Image.open(image_path)
    welcome_image = welcome_image.resize((w, h))  # Adjust the size of the image as needed
    photo = ImageTk.PhotoImage(welcome_image)

    # Create a label to display the image
    image_label = Label(page)
    image_label.image = photo  # Store the image reference as an attribute of the label
    image_label.configure(image=photo)
    image_label.pack()

def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    # Gambar detail
    display_image(top, "./LatihanPyGUI/asset/fine.jpg", 300, 300)

    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)
    
    # Jika Apartemen atau Rumah
    if isinstance(hunians[index], (Apartemen, Rumah)):
        d_summary = Label(d_frame, text="Summary:\n" + hunians[index].get_detail() + "\nKeterangan:\n" + hunians[index].get_summary() + "\n\nDokumen:\n" + hunians[index].get_dokumen() , anchor="w", justify=LEFT)
    # Jika Indekos
    else:
        d_summary = Label(d_frame, text="Summary:\n " + hunians[index].get_summary(), anchor="w")

    d_summary.grid(row=0, column=0, sticky="w")

    # Button Close
    btn = LabelFrame(top, padx=0, pady=0)
    btn.pack(padx=10, pady=10)
    b_close = Button(btn, text="Close", command=top.destroy)
    b_close.grid(row=0, column=0)
    
    # Watermark Copyright
    canvas = Canvas(top, width=400, height=200)
    canvas.pack()
    canvas.create_text(275, 100, text="Ini Watermark ┗|｀O′|┛")

# Delete data penghuni
def delete(index):
    hunians.pop(index)
    update_tabel()

# Me-reset data kembali seperti awal
def reset():
    hunians.clear()
    hunians.extend(data_hunians)
    update_tabel()

# Update tabel
def update_tabel():
    # Menghapus frame
    for widget in frame.winfo_children():
        widget.destroy()

    # Susunan data
    for index, h in enumerate(hunians):
        idx = Label(frame, text=str(index + 1), width=5, borderwidth=1, relief="solid")
        idx.grid(row=index, column=0)

        type_label = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
        type_label.grid(row=index, column=1)

        # Jika Apartemen atau Rumah
        if isinstance(h, (Apartemen, Rumah)):
            name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
        # Jika Indekos
        else:
            name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")

        name.grid(row=index, column=2)

        # Detail
        b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
        b_detail.grid(row=index, column=3)

        # Delete
        b_delete = Button(frame, text="Delete ", command=lambda index=index: delete(index))
        b_delete.grid(row=index, column=4)

    # Tampilan tombol reset
    if hunians:
        # Jika masih ada data tersisa
        b_reset.configure(state=DISABLED)
    else:
        # Jika data sudah tidak tersisa
        b_reset.configure(state=NORMAL)

# Welcome Page
title_label = Label(welcome_page, text="Hello", font=("", 24, "bold"))
title_label.pack(pady=50)

# Gambar Welcome Page
display_image(welcome_page, "./LatihanPyGUI/asset/chuckles-im-in-danger.jpg", 300, 300)

# Button Welcome Page
access_button = Button(welcome_page, text="Lets Go", command=move_to_root, font=("", 16, "bold"))
access_button.pack(pady=30)

# Root 

# Gambar Root
display_image(root, "./LatihanPyGUI/asset/Naruto.jpg", 300, 300)

# Tabel residen
frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
frame.pack(padx=10, pady=10)

opts = LabelFrame(root, padx=10, pady=10)
opts.pack(padx=10, pady=10)

# Button

# Button Add
b_add = Button(opts, text="Add Data", state=DISABLED)
b_add.grid(row=0, column=0)

# Button Exit
b_exit = Button(opts, text="Exit", command=root.quit)
b_exit.grid(row=0, column=1)

# Button Reset
b_reset = Button(opts, text="Reset", command=reset, state=DISABLED)
b_reset.grid(row=0, column=2)

# Reset Tampilan tabel
reset()

root.mainloop()
