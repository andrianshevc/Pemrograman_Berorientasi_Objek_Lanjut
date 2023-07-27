import tkinter as tk
from tkinter import *
from tkinter import Menu
from tkinter import messagebox
from FrmAnggota import *
from FrmPetugas import *
from FrmBuku import *
from FrmPeminjaman import *
from FrmPengembalian import *


# root window
root = tk.Tk()
root.title('APLIKASI PERPUSTAKAAN')
root.geometry("900x600")
root.configure(bg='#fff')


# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create a menu
file_menu = Menu(menubar)
pengguna_menu = Menu(menubar)
buku_menu = Menu(menubar)
peminjaman_menu   = Menu(menubar)

# add a menu item to the menu
file_menu.add_command(
    label='File Open', command=root.destroy
)

file_menu.add_command(
    label='Exit', command=root.destroy
)
#Menu Pengguna
pengguna_menu.add_command(
    label='Data Anggota', command= lambda: new_window("Data Anggota",FrmAnggota)
)
pengguna_menu.add_command(
    label='Data Petugas', command= lambda: new_window("Data Petugas",FrmPetugas)
)

# Menu Buku
buku_menu.add_command(
    label='App Data Buku', command= lambda: new_window("Data Buku", FrmBuku)
)

# Menu Peminjaman
peminjaman_menu.add_command(
    label='App Data Peminjaman', command= lambda: new_window("Peminjaman", FrmPeminjaman)
)
peminjaman_menu.add_command(
    label='App Data Pengembalian', command= lambda: new_window("Pengembalian", FrmPengembalian)
)

# gambar = PhotoImage(file="D:\\Pythonn\\Aplikasi perpustakaan\\library.png")

# Text = Label(root,text="Hallo", fg = "white", compound =BOTTOM, image=gambar).pack(side="top")

def new_window( number, _class):
    new = tk.Toplevel()
    _class(new, number)

# add the File menu to the menubar
menubar.add_cascade(
    label="File", menu=file_menu
)
menubar.add_cascade(
    label="Pengguna", menu=pengguna_menu
)
menubar.add_cascade(
    label="Buku", menu=buku_menu
)
menubar.add_cascade(
    label="Peminjaman", menu=peminjaman_menu
)


root.mainloop()
