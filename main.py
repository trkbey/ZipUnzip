from tkinter import Tk, Canvas, Button, PhotoImage, filedialog
from zipfile import *
from os import *

def make_zip():

    window.withdraw()

    file_path = filedialog.askdirectory(title="dosya seç")

    window.after(2000, window.deiconify)

    parent_dir = path.dirname(path.normpath(file_path))
    dir_name = path.basename(path.normpath(file_path))
    zip_path = path.join(parent_dir, f"{dir_name}.zip")

    with ZipFile(zip_path, 'w', ZIP_DEFLATED) as zipf:
        for root, dirs, files in walk(file_path):
            for file in files:
                file_way = path.join(root, file)
                zipf.write(file_way, path.relpath(file_way, file_path))

def unzip():

    window.withdraw()

    file_path = filedialog.askopenfilename(title="ZIP seç")

    window.deiconify()
    parent_dir = path.dirname(path.normpath(file_path))
    zip_name = path.basename(file_path)
    dir_name = path.splitext(zip_name)[0]
    output_path = path.join(parent_dir, dir_name)
    makedirs(output_path, exist_ok=True)

    with ZipFile(file_path, 'r') as zipf:
        zipf.extractall(output_path)


window = Tk()

window.geometry("540x360")
window.configure(bg = "#202020")


canvas = Canvas(
    window,
    bg = "#202020",
    height = 360,
    width = 540,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
zip_img = PhotoImage(
    file="assets/frame0/zip.png")
zip_button = Button(
    bg="#202020",
    activebackground="#202020",
    image=zip_img,
    borderwidth=0,
    highlightthickness=0,
    command=make_zip,
    relief="flat"
)
zip_button.place(
    x=77.0,
    y=103.0,
    width=380.0,
    height=50.0
)

unzip_img = PhotoImage(
    file="assets/frame0/unzip.png")
unzip_button = Button(
    bg="#202020",
    image=unzip_img,
    activebackground="#202020",
    borderwidth=0,
    highlightthickness=0,
    command=unzip,
    relief="flat"
)
unzip_button.place(
    x=77.0,
    y=209.0,
    width=380.0,
    height=50.0
)
window.resizable(False, False)
window.mainloop()