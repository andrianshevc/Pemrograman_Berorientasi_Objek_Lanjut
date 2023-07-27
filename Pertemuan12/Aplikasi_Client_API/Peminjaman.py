
import requests
import json
class Peminjaman:
    def __init__(self):
        self.__id=None
        self.__kode_peminjaman = None
        self.__tgll_pinjam = None
        self.__tanggal_kembali = None
        self.__kode_buku = None
        self.__kode_anggota = None
        self.__kode_petugas = None
        self.__url = "http://localhost/Myperpustakaan/peminjaman_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def kode_peminjaman(self):
        return self.__kode_peminjaman
        
    @kode_peminjaman.setter
    def kode_peminjaman(self, value):
        self.__kode_peminjaman = value
    @property
    def tgll_pinjam(self):
        return self.__tgll_pinjam
        
    @tgll_pinjam.setter
    def tgll_pinjam(self, value):
        self.__tgll_pinjam = value
    @property
    def tanggal_kembali(self):
        return self.__tanggal_kembali
        
    @tanggal_kembali.setter
    def tanggal_kembali(self, value):
        self.__tanggal_kembali = value
    @property
    def kode_buku(self):
        return self.__kode_buku
        
    @kode_buku.setter
    def kode_buku(self, value):
        self.__kode_buku = value
    @property
    def kode_anggota(self):
        return self.__kode_anggota
        
    @kode_anggota.setter
    def kode_anggota(self, value):
        self.__kode_anggota = value
    @property
    def kode_petugas(self):
        return self.__kode_petugas
        
    @kode_petugas.setter
    def kode_petugas(self, value):
        self.__kode_petugas = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_kode_peminjaman(self, kode_peminjaman):
        url = self.__url+"?kode_peminjaman="+kode_peminjaman
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id_peminjaman']
            self.__kode_peminjaman = item['kode_peminjaman']
            self.__tgll_pinjam = item['tgll_pinjam']
            self.__tanggal_kembali = item['tanggal_kembali']
            self.__kode_buku = item['kode_buku']
            self.__kode_anggota = item['kode_anggota']
            self.__kode_petugas = item['kode_petugas']
        return data
    def simpan(self):
        payload = {
            "kode_peminjaman":self.__kode_peminjaman,
            "tgll_pinjam":self.__tgll_pinjam,
            "tanggal_kembali":self.__tanggal_kembali,
            "kode_buku":self.__kode_buku,
            "kode_anggota":self.__kode_anggota,
            "kode_petugas":self.__kode_petugas
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_kode_peminjaman(self, kode_peminjaman):
        url = self.__url+"?kode_peminjaman="+kode_peminjaman
        payload = {
            "kode_peminjaman":self.__kode_peminjaman,
            "tgll_pinjam":self.__tgll_pinjam,
            "tanggal_kembali":self.__tanggal_kembali,
            "kode_buku":self.__kode_buku,
            "kode_anggota":self.__kode_anggota,
            "kode_petugas":self.__kode_petugas
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_kode_peminjaman(self,kode_peminjaman):
        url = self.__url+"?kode_peminjaman="+kode_peminjaman
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
