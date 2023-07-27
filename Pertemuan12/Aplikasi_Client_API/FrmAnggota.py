import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Anggota import *
class FrmAnggota:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("750x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='KODE_ANGGOTA:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NAMA_ANGGOTA:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='JK_ANGGOTA:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='PRODI_ANGGOTA:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='ALAMAT_ANGGOTA:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtKode_anggota = Entry(mainFrame) 
        self.txtKode_anggota.grid(row=0, column=1, padx=5, pady=5)
        self.txtKode_anggota.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtNama_anggota = Entry(mainFrame) 
        self.txtNama_anggota.grid(row=1, column=1, padx=5, pady=5)
        # Combo Box
        self.txtJk_anggota = StringVar()
        Cbo_jk_anggota = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtJk_anggota) 
        Cbo_jk_anggota.grid(row=2, column=1, padx=5, pady=5)
        # Adding jk_anggota combobox drop down list
        Cbo_jk_anggota['values'] = ('L','P')
        Cbo_jk_anggota.current()
        # Combo Box
        self.txtProdi_anggota = StringVar()
        Cbo_prodi_anggota = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtProdi_anggota) 
        Cbo_prodi_anggota.grid(row=3, column=1, padx=5, pady=5)
        # Adding prodi_anggota combobox drop down list
        Cbo_prodi_anggota['values'] = ('TIF','IND','PET')
        Cbo_prodi_anggota.current()
        # Textbox
        self.txtAlamat_anggota = Entry(mainFrame) 
        self.txtAlamat_anggota.grid(row=4, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('id_anggota','kode_anggota','nama_anggota','jk_anggota','prodi_anggota','alamat_anggota')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id_anggota', text='ID_ANGGOTA')
        self.tree.column('id_anggota', width="80")
        self.tree.heading('kode_anggota', text='KODE_ANGGOTA')
        self.tree.column('kode_anggota', width="100")
        self.tree.heading('nama_anggota', text='NAMA_ANGGOTA')
        self.tree.column('nama_anggota', width="150")
        self.tree.heading('jk_anggota', text='JK_ANGGOTA')
        self.tree.column('jk_anggota', width="100")
        self.tree.heading('prodi_anggota', text='PRODI_ANGGOTA')
        self.tree.column('prodi_anggota', width="150")
        self.tree.heading('alamat_anggota', text='ALAMAT_ANGGOTA')
        self.tree.column('alamat_anggota', width="150")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtKode_anggota.delete(0,END)
        self.txtKode_anggota.insert(END,"")
        self.txtNama_anggota.delete(0,END)
        self.txtNama_anggota.insert(END,"")
        self.txtJk_anggota.set("")
        self.txtProdi_anggota.set("")
        self.txtAlamat_anggota.delete(0,END)
        self.txtAlamat_anggota.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data anggota
        obj = Anggota()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id_anggota"],d["kode_anggota"],d["nama_anggota"],d["jk_anggota"],d["prodi_anggota"],d["alamat_anggota"]))
    def onCari(self, event=None):
        kode_anggota = self.txtKode_anggota.get()
        obj = Anggota()
        a = obj.get_by_kode_anggota(kode_anggota)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        kode_anggota = self.txtKode_anggota.get()
        obj = Anggota()
        res = obj.get_by_kode_anggota(kode_anggota)
        self.txtKode_anggota.delete(0,END)
        self.txtKode_anggota.insert(END,obj.kode_anggota)
        self.txtNama_anggota.delete(0,END)
        self.txtNama_anggota.insert(END,obj.nama_anggota)
        self.txtJk_anggota.set(obj.jk_anggota)
        self.txtProdi_anggota.set(obj.prodi_anggota)
        self.txtAlamat_anggota.delete(0,END)
        self.txtAlamat_anggota.insert(END,obj.alamat_anggota)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        kode_anggota = self.txtKode_anggota.get()
        nama_anggota = self.txtNama_anggota.get()
        jk_anggota = self.txtJk_anggota.get()
        prodi_anggota = self.txtProdi_anggota.get()
        alamat_anggota = self.txtAlamat_anggota.get()
        # create new Object
        obj = Anggota()
        obj.kode_anggota = kode_anggota
        obj.nama_anggota = nama_anggota
        obj.jk_anggota = jk_anggota
        obj.prodi_anggota = prodi_anggota
        obj.alamat_anggota = alamat_anggota
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_kode_anggota(kode_anggota)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        kode_anggota = self.txtKode_anggota.get()
        obj = Anggota()
        obj.kode_anggota = kode_anggota
        if(self.ditemukan==True):
            res = obj.delete_by_kode_anggota(kode_anggota)
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
    aplikasi = FrmAnggota(root2, "Aplikasi Data Anggota")
    root2.mainloop()
