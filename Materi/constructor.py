# class mahasiswa:
#     def __init__(self, nama, nim, jurusan):
#         self.nama = nama
#         self.nim = nim
#         self.jurusan = jurusan

#     def tampilkan_info(self):
#         print(f"Nama: {self.nama}")
#         print(f"NIM: {self.nim}")
#         print(f"Jurusan: {self.jurusan}")

# mahasiswa1 = mahasiswa("Budi", 123456, "Informatika")

# class mahasiswa:
#     def __init__(self, nama, nim, jurusan):
#         self.nama = nama
#         self.nim = nim
#         self.jurusan = jurusan

#     def __str__(self):
#         return f"Nama: {self.nama}\nNIM: {self.nim}\nJurusan: {self.jurusan}"

# mahasiswa1 = mahasiswa("Budi", 123456, "Informatika")
# mahasiswa2 = mahasiswa("Ani", 654321, "Sistem Informasi")

# print(mahasiswa1)
# print()
# print(mahasiswa2)





class BankAccount:
    def __init__(self, no, saldo =0):
        if saldo < 0:
            raise ValueError("Saldo tidak boleh negatif.")
        self.no = no
        self.saldo = saldo

valen = BankAccount (123456, 1000000)
reno = BankAccount (654321, 1500000)

print(valen.saldo)
print()
print(reno.saldo)