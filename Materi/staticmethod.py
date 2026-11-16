# class matematika:
#     def __init__(self, angka_1, angka_2):
#         self.angka_1 = angka_1
#         self.angka_2 = angka_2

#     def tambah(self):
#         return self.angka_1 + self.angka_2

# mtk = matematika(10, 5)

# print(mtk.tambah())




class matematika:
    @staticmethod
    def tambah(angka_1, angka_2):
        return angka_1 + angka_2

print(matematika.tambah(10, 5))