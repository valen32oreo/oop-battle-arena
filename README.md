# Identitas Developer
Nama  : Krisna Valencia Hidayat
NIM   : 14012500046
Kelas : 3A-KOM

# ⚔️ OOP Battle Arena (GUI Desktop Game)

Projek game pertarungan interaktif berbasis GUI (Graphical User Interface) menggunakan **Tkinter** dengan tema modern *Dark Slate*. Projek ini dibangun untuk mengimplementasikan seluruh materi Pemrograman Berbasis Objek (OOP) Pertemuan 1–7.

---

## 📌 Pemetaan Materi OOP pada Kode

| No | Konsep OOP | Implementasi Kode | Materi Asal | Berkas |
|---|---|---|---|---|
| 1 | **Class & Instance Object** | Instansiasi `player` dan `monster` dari class `Karakter` | `class_object.py` | `models.py`, `main.py` |
| 2 | **Constructor & Validation** | Penetapan atribut awal dengan pengecekan `raise ValueError`, errornya ditangkap dengan `try/except` di GUI | `constructor.py`, `tugas1.py` | `models.py`, `main.py` |
| 3 | **Special Method (`__str__`)** | `__str__` dipakai untuk menampilkan status awal karakter di log pertarungan | `constructor.py`, `tugas1.py` | `models.py`, `main.py` |
| 4 | **Encapsulation (`@property`)** | Penggunaan `@property` dan `@setter` pada atribut `hp` (HP otomatis dibatasi 0 sampai `hp_max`) | `kategory.py` | `models.py` |
| 5 | **Class Attribute & Class Method** | Melacak `total_karakter` & `total_pertarungan` via `@classmethod info_global()` | `classmethod.py` | `models.py`, `main.py` |
| 6 | **Static Method (`@staticmethod`)** | Utilitas critical hit, hitung EXP, dan format header via `GameHelper` | `staticmethod.py` | `helpers.py`, `main.py` |
| 7 | **Object Interaction** | Method `serang()` memanggil `diserang()` pada objek lawan sehingga HP lawan berkurang | `game.py`, `class_object.py` | `models.py` |

---

## 📁 Struktur Berkas

* `models.py`: Logika utama backend OOP (class `Karakter`, `@property`, `__str__`, `@classmethod`).
* `helpers.py`: Fungsi utilitas game berbasis `@staticmethod` (class `GameHelper`).
* `main.py`: Antarmuka grafis (GUI Tkinter) dengan *custom HP Bar* & log berwarna.
* `README.md`: Dokumentasi projek dan pemetaan materi.

Berkas latihan pertemuan 1–7 (`class_object.py`, `constructor.py`, `tugas1.py`, `kategory.py`, `classmethod.py`, `staticmethod.py`, `game.py`) adalah materi dasar yang dikembangkan menjadi projek ini.

---

## 🚀 Cara Menjalankan Game

1. Pastikan Python 3.x telah terinstal di perangkat.
2. Buka terminal VSCode di dalam folder projek.
3. Jalankan perintah berikut:
   ```bash
   python main.py
   ```