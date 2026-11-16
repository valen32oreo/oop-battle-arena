class Karakter:
    # 1. Class Attributes (classmethod.py)
    total_karakter = 0
    total_pertarungan = 0

    def __init__(self, nama: str, hp_awal: int, attack: int, armor: int):
        # 2. Constructor Validation (constructor.py / tugas1.py)
        if not nama.strip():
            raise ValueError("Nama karakter tidak boleh kosong!")
        if hp_awal <= 0:
            raise ValueError("HP awal harus lebih dari 0!")
        if attack < 0 or armor < 0:
            raise ValueError("Attack dan Armor tidak boleh negatif!")

        self.nama = nama
        self._hp = hp_awal            # Protected attribute
        self.hp_max = hp_awal
        self.attack = attack
        self.armor = armor

        Karakter.total_karakter += 1

    # 3. Property & Setter dengan Validasi (kategory.py)
    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, nilai):
        if nilai < 0:
            self._hp = 0
        elif nilai > self.hp_max:
            self._hp = self.hp_max
        else:
            self._hp = nilai

    # 4. Special Method __str__ (constructor.py / tugas1.py)
    def __str__(self):
        return f"{self.nama} (HP: {self.hp}/{self.hp_max} | ATK: {self.attack} | ARMOR: {self.armor})"

    # 5. Interaksi Antar Objek (game.py & class_object.py)
    def serang(self, lawan, is_critical=False):
        Karakter.total_pertarungan += 1
        damage_dasar = self.attack * 2 if is_critical else self.attack
        damage_diterima = lawan.diserang(damage_dasar)
        return damage_diterima

    def diserang(self, damage_masuk):
        damage_bersih = max(1, damage_masuk - self.armor)
        self.hp -= damage_bersih
        return damage_bersih

    def heal(self, jumlah=20):
        """Memulihkan HP dan mengembalikan jumlah HP yang benar-benar pulih."""
        hp_sebelum = self.hp
        self.hp += jumlah             # setter membatasi HP agar tidak melebihi hp_max
        return self.hp - hp_sebelum

    # 6. Class Method (classmethod.py)
    @classmethod
    def info_global(cls):
        return f"Total Karakter: {cls.total_karakter} | Total Pertarungan: {cls.total_pertarungan}"