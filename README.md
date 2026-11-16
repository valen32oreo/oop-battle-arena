# Identitas Developer
Nama  : Krisna Valencia Hidayat
NIM   : 14012500046
Kelas : 3A-KOM

# ⚔️ OOP Battle Arena (GUI Desktop Game)

Projek game pertarungan interaktif berbasis GUI (Graphical User Interface) menggunakan **Tkinter** dengan tema modern *Dark Slate*. Projek ini dibangun untuk mengimplementasikan seluruh materi Pemrograman Berbasis Objek (OOP) Pertemuan 1–7.

---

## 📌 Pemetaan Materi OOP pada Kode

| No | Konsep OOP | Implementasi Kode | Berkas |
|---|---|---|---|
| 1 | **Class & Instance Object** | Instansiasi `player` dan `monster` dari class `Karakter` | `models.py`, `main.py` |
| 2 | **Constructor & Validation** | Penetapan atribut awal dengan pengecekan `raise ValueError` | `models.py` |
| 3 | **Special Method (`__str__`)** | Kustomisasi string status karakter | `models.py` |
| 4 | **Encapsulation (`@property`)** | Penggunaan `@property` dan `@setter` pada atribut `hp` | `models.py` |
| 5 | **Class Attribute & Method** | Melacak `total_karakter` & `total_pertarungan` via `@classmethod` | `models.py` |
| 6 | **Static Method (`@staticmethod`)** | Utilitas acak critical hit & hitung EXP via `GameHelper` | `helpers.py` |
| 7 | **Object Interaction** | Method `serang()` memanipulasi HP pada objek lawan | `models.py` |

---

## 📁 Struktur Berkas

* `models.py`: Berisi logika utama backend OOP (Class `Karakter`, `@property`, `@classmethod`).
* `helpers.py`: Berisi fungsi utilitas game berbasis `@staticmethod` (`GameHelper`).
* `main.py`: Berisi antarmuka grafis (GUI Tkinter) dengan *custom HP Bar* & log warna.
* `README.md`: Dokumentasi projek dan pemetaan materi.

---

## 🚀 Cara Menjalankan Game

1. Pastikan Python 3.x telah terinstal di perangkat.
2. Buka terminal / PowerShell di dalam folder projek.
3. Jalankan perintah berikut:
   ```bash
   python main.py