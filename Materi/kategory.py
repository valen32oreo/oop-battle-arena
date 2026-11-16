class kategory:
    _nama = ""
    @property
    def nama(self):
        return self._nama

    @nama.setter
    def nama(self, nama):
        if nama == "":
            raise ValueError("Nama tidak boleh kosong")
        self._nama = nama

category1 = kategory()
category1.nama = "Valen"
print(category1.nama)