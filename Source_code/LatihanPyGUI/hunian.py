class Hunian():
    # Constructor
    def __init__(self, jenis, jml_penghuni = 1, jml_kamar = 1):
        self.jenis = jenis
        self.jml_penghuni = jml_penghuni
        self.jml_kamar = jml_kamar

    # Jenis
    def get_jenis(self):
        return self.jenis

    # Jumlah Penghuni
    def get_jml_penghuni(self):
        return self.jml_penghuni

    # Jumlah Kamar
    def get_jml_kamar(self):
        return self.jml_kamar

    # Dokumen
    def get_dokumen(self):
        pass

    # Ringkasan
    def get_summary(self):
        return "Hunian "+ self.jenis +", ditempati oleh " + str(self.jml_penghuni) + " orang."