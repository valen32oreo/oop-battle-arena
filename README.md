# Identitas Developer
Nama  : Krisna Valencia Hidayat
NIM   : 14012500046
Kelas : 3A-KOM

# ⚔️ OOP Battle Arena (Text-Based RPG)

Projek sederhana berupa game pertarungan berbasis Teks (CLI) yang dibangun mengimplementasikan seluruh materi Pemrograman Berbasis Objek (OOP) Pertemuan 1–7.

---

## 📌 Pemetaan Materi OOP pada Kode

| No | Konsep OOP | Implemetasi Kode | Berkas |
|---|---|---|---|
| 1 | **Class & Instance Object** | Instansiasi `player` dan `monster` dari class `Karakter` | `models.py`, `main.py` |
| 2 | **Constructor & Validation** | Penetapan atribut awal dengan pengecekan `raise ValueError` | `models.py` |
| 3 | **Special Method (`__str__`)** | Kustomisasi output status karakter saat di-`print()` | `models.py` |
| 4 | **Encapsulation (`@property`)** | Penggunaan `@property` dan `@setter` pada atribut `hp` | `models.py` |
| 5 | **Class Attribute & Method** | Melacak `total_karakter` & `total_pertarungan` via `@classmethod` | `models.py` |
| 6 | **Static Method (`@staticmethod`)** | Utilitas acak critical hit & hitung EXP via `GameHelper` | `helpers.py` |
| 7 | **Object Interaction** | Method `serang()` memanipulasi HP pada objek lawan | `models.py` |

---

## 🚀 Cara Menjalankan Game

1. Clone repositori ini atau unduh berkasnya.
2. Buka terminal di folder projek.
3. Jalankan perintah:
   ```bash
   python main.py