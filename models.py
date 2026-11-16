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

    # 4. Special Method __str__ (constructor.py)
    def __str__(self):
        return f"{self.nama:<15} | HP: {self.hp:>3}/{self.hp_max:<3} | ATK: {self.attack:>2} | ARMOR: {self.armor:>2}"

    # 5. Interaksi Antar Objek (game.py & class_object.py)
    def serang(self, lawan, is_critical=False):
        Karakter.total_pertarungan += 1
        print(f"\n⚔️  {self.nama} menyerang {lawan.nama}!")
        
        damage_dasar = self.attack * 2 if is_critical else self.attack
        if is_critical:
            print("💥 CRITICAL HIT! Damage berlipat ganda!")

        lawan.diserang(damage_dasar)

    def diserang(self, damage_masuk):
        damage_bersih = max(1, damage_masuk - self.armor)
        self.hp -= damage_bersih
        print(f"🛡️  {self.nama} menerima {damage_bersih} damage (setelah terpotong armor).")
        print(f"❤️  Sisa HP {self.nama}: {self.hp}")

    # 6. Class Method (classmethod.py)
    @classmethod
    def jumlah_karakter(cls):
        return cls.total_karakter

    @classmethod
    def info_global(cls):
        return f"=== STATISTIK GLOBAL GAME ===\nTotal Karakter Dibuat : {cls.total_karakter}\nTotal Ronde Pertarungan : {cls.total_pertarungan}"