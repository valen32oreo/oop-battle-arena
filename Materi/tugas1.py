# 1. CONSTRUCTOR DASAR
class Mobil:
    def __init__(self, merk, tahun):
        self.merk = merk
        self.tahun = tahun

# 2. CONSTRUCTOR WITH SPECIAL METHOD (__str__ & __repr__)
class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
    
    # Special method buat kustomisasi output print
    def __str__(self):
        return f"Buku '{self.judul}' karya {self.penulis}"

# 3. CONSTRUCTOR WITH VALIDATION
class AkunBank:
    def __init__(self, pemilik, saldo_awal):
        if saldo_awal < 0:
            raise ValueError("Saldo awal tidak boleh negatif!")
        self.pemilik = pemilik
        self.saldo = saldo_awal


# Uji Coba
m = Mobil("Toyota", 2022)
b = Buku("Pemrograman Python", "Guido van Rossum")
a = AkunBank("Valen", 500000)

print(m.merk)
print(b)
print(a.saldo)