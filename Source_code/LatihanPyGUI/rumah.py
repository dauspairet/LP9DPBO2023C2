from hunian import Hunian

class Rumah(Hunian):
    # Constructor
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar):
        super().__init__("Rumah", jml_penghuni, jml_kamar)
        self.nama_pemilik = nama_pemilik

    # Dokumen
    def get_dokumen(self):
        return "Izin Mendirikan Bangunan (IMB) a/n " + self.nama_pemilik

    # Nama
    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    # Rincian
    def get_detail(self):
        return "\nPemilik : \n" + self.nama_pemilik + "\n\nJumlah Kamar : \n" + str(self.jml_kamar) + "\n"