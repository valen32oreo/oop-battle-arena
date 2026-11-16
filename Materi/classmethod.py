class mahasiswa:
    jumlah_mahasiswa = 0
    nilai_ipk = 0.0

    def __init__(self, nama, nim, ipk):
        self.nama = nama
        self.nim = nim
        self.ipk = ipk
        mahasiswa.jumlah_mahasiswa += 1
        mahasiswa.nilai_ipk += float (ipk)

    @classmethod
    def jumlah(cls):
        return cls.jumlah_mahasiswa

    @classmethod
    def rata(cls):
        if cls.jumlah_mahasiswa == 0:
            return 0
        return cls.nilai_ipk / cls.jumlah_mahasiswa

riko = mahasiswa("Riko", 123456, 3.5)
dika = mahasiswa("Dika", 123457, 3.8)

print("Jumlah Mahasiswa:", mahasiswa.jumlah())
print("Rata-rata IPK:", mahasiswa.rata())