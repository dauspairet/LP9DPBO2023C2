from hunian import Hunian

class Apartemen(Hunian):
    # Constructor
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar):
        super().__init__("Apartemen", jml_penghuni, jml_kamar)
        self.nama_pemilik = nama_pemilik

    # Dokumen
    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik + "."

    # Pemilik
    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    # Rincian
    def get_detail(self):
        return "\nPemilik : \n" + self.nama_pemilik + "\n\nJumlah Kamar : \n" + str(self.jml_kamar) + "\n"