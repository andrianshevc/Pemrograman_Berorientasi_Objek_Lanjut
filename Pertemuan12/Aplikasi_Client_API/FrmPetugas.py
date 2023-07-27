import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Petugas import *
class FrmPetugas:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x400")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='KODE_PETUGAS:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NAMA_PETUGAS:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='JABATAN_PETUGAS:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtKode_petugas = Entry(mainFrame) 
        self.txtKode_petugas.grid(row=0, column=1, padx=5, pady=5)
        self.txtKode_petugas.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtNama_petugas = Entry(mainFrame) 
        self.txtNama_petugas.grid(row=1, column=1, padx=5, pady=5)
        # Combo Box
        self.txtJabatan_petugas = StringVar()
        Cbo_jabatan_petugas = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtJabatan_petugas) 
        Cbo_jabatan_petugas.grid(row=2, column=1, padx=5, pady=5)
        # Adding jabatan_petugas combobox drop down list
        Cbo_jabatan_petugas['values'] = ('K.Perpus','Admin','Kasir')
        Cbo_jabatan_petugas.current()
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('id_petugas','kode_petugas','nama_petugas','jabatan_petugas')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id_petugas', text='ID_PETUGAS')
        self.tree.column('id_petugas', width="80")
        self.tree.heading('kode_petugas', text='KODE_PETUGAS')
        self.tree.column('kode_petugas', width="100")
        self.tree.heading('nama_petugas', text='NAMA_PETUGAS')
        self.tree.column('nama_petugas', width="125")
        self.tree.heading('jabatan_petugas', text='JABATAN_PETUGAS')
        self.tree.column('jabatan_petugas', width="120")
        # set tree position
        self.tree.place(x=0, y=150)
        
    def onClear(self, event=None):
        self.txtKode_petugas.delete(0,END)
        self.txtKode_petugas.insert(END,"")
        self.txtNama_petugas.delete(0,END)
        self.txtNama_petugas.insert(END,"")
        self.txtJabatan_petugas.set("")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data petugas
        obj = Petugas()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id_petugas"],d["kode_petugas"],d["nama_petugas"],d["jabatan_petugas"]))
    def onCari(self, event=None):
        kode_petugas = self.txtKode_petugas.get()
        obj = Petugas()
        a = obj.get_by_kode_petugas(kode_petugas)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        kode_petugas = self.txtKode_petugas.get()
        obj = Petugas()
        res = obj.get_by_kode_petugas(kode_petugas)
        self.txtKode_petugas.delete(0,END)
        self.txtKode_petugas.insert(END,obj.kode_petugas)
        self.txtNama_petugas.delete(0,END)
        self.txtNama_petugas.insert(END,obj.nama_petugas)
        self.txtJabatan_petugas.set(obj.jabatan_petugas)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        kode_petugas = self.txtKode_petugas.get()
        nama_petugas = self.txtNama_petugas.get()
        jabatan_petugas = self.txtJabatan_petugas.get()
        # create new Object
        obj = Petugas()
        obj.kode_petugas = kode_petugas
        obj.nama_petugas = nama_petugas
        obj.jabatan_petugas = jabatan_petugas
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_kode_petugas(kode_petugas)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        kode_petugas = self.txtKode_petugas.get()
        obj = Petugas()
        obj.kode_petugas = kode_petugas
        if(self.ditemukan==True):
            res = obj.delete_by_kode_petugas(kode_petugas)
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        
        self.onClear()
            
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root2 = tk.Tk()
    aplikasi = FrmPetugas(root2, "Aplikasi Data Petugas")
    root2.mainloop()
