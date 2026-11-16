class Mahasiswa:
    def __init__(self, nama, nim, prodi):
        self.name = nama
        self.nim = nim
        self.prodi = prodi

    def perkenalan(self):
        return f"Halo, perkenalkan nama saya {self.name}, Prodi {self.prodi}"

    def sapa_balik(self, mahasiswa_lain):
        return f"Halo {mahasiswa_lain.name}! Salam kenal, aku {self.name} dari prodi {self.prodi}."

mahasiswa1 = Mahasiswa("John Doe", 123456, "Informatika")
mahasiswa2 = Mahasiswa("Jane Smith", 789012, "Sistem Informasi")
mahasiswa3 = Mahasiswa("Alice Johnson", 345678, "Teknik Komputer")

print(mahasiswa1.perkenalan())
print(mahasiswa2.sapa_balik(mahasiswa1))