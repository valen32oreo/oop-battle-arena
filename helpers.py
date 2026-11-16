import random

class GameHelper:
    # Static Method (Materi/staticmethod.py)
    @staticmethod
    def cek_critical(peluang=0.3):
        """Menentukan apakah serangan mendapatkan Critical Hit berdasarkan peluang (default 30%)."""
        return random.random() < peluang

    @staticmethod
    def hitung_exp(level_lawan):
        """Kalkulasi poin EXP yang didapat setelah mengalahkan musuh."""
        return level_lawan * 50

    @staticmethod
    def format_header(judul):
        """Membuat tampilan header ASCII yang rapi di terminal."""
        garis = "=" * 45
        return f"\n{garis}\n{judul.center(45)}\n{garis}"