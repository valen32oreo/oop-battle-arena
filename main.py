import tkinter as tk
from tkinter import ttk, messagebox
from models import Karakter, GameHelper

class BattleArenaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("⚔️ OOP Battle Arena GUI")
        self.root.geometry("600x550")
        self.root.resizable(False, False)

        # Inisialisasi Objek Game (Constructor & Validation)
        try:
            self.player = Karakter("Knight Valen", hp_awal=100, attack=25, armor=8)
            self.monster = Karakter("Shadow Demon", hp_awal=90, attack=22, armor=4)
        except ValueError as e:
            messagebox.showerror("Error Inisialisasi", str(e))
            self.root.destroy()
            return

        self.setup_ui()
        self.update_status()

    def setup_ui(self):
        # Style Konfigurasi
        style = ttk.Style()
        style.theme_use('clam')

        # Header Title
        lbl_title = tk.Label(self.root, text="⚔️ OOP BATTLE ARENA ⚔️", font=("Helvetica", 16, "bold"), fg="#2C3E50")
        lbl_title.pack(pady=10)

        # Container Frame Karakter
        frame_karakter = tk.Frame(self.root)
        frame_karakter.pack(pady=10, fill="x", px=20)

        # Panel Player (Kiri)
        frame_player = tk.LabelFrame(frame_karakter, text=" Hero Player ", font=("Helvetica", 11, "bold"), padx=10, pady=10)
        frame_player.pack(side="left", expand=True, fill="both", padx=5)

        # Menggunakan Special Method __str__ pada Label Header Player
        self.lbl_player_info = tk.Label(frame_player, text=str(self.player), font=("Helvetica", 9), wraplength=220, justify="left")
        self.lbl_player_info.pack(anchor="w")

        self.bar_player_hp = ttk.Progressbar(frame_player, length=200, mode='determinate')
        self.bar_player_hp.pack(pady=8)

        # Panel Monster (Kanan)
        frame_monster = tk.LabelFrame(frame_karakter, text=" Enemy Monster ", font=("Helvetica", 11, "bold"), padx=10, pady=10)
        frame_monster.pack(side="right", expand=True, fill="both", padx=5)

        # Menggunakan Special Method __str__ pada Label Header Monster
        self.lbl_monster_info = tk.Label(frame_monster, text=str(self.monster), font=("Helvetica", 9), wraplength=220, justify="left")
        self.lbl_monster_info.pack(anchor="w")

        self.bar_monster_hp = ttk.Progressbar(frame_monster, length=200, mode='determinate')
        self.bar_monster_hp.pack(pady=8)

        # Log Aktivitas Pertarungan
        frame_log = tk.LabelFrame(self.root, text=" Log Pertarungan ", font=("Helvetica", 10, "bold"), padx=10, pady=5)
        frame_log.pack(pady=10, fill="both", expand=True, px=20)

        self.txt_log = tk.Text(frame_log, height=10, state="disabled", font=("Consolas", 9), bg="#F8F9F9")
        self.txt_log.pack(fill="both", expand=True)

        # Container Tombol Aksi
        frame_btn = tk.Frame(self.root)
        frame_btn.pack(pady=10)

        self.btn_attack = tk.Button(frame_btn, text="⚔️ Serang", font=("Helvetica", 10, "bold"), bg="#E74C3C", fg="white", width=12, command=self.aksi_serang)
        self.btn_attack.grid(row=0, column=0, padx=5)

        self.btn_heal = tk.Button(frame_btn, text="🧪 Potion (+20)", font=("Helvetica", 10, "bold"), bg="#2ECC71", fg="white", width=12, command=self.aksi_heal)
        self.btn_heal.grid(row=0, column=1, padx=5)

        self.btn_stats = tk.Button(frame_btn, text="📊 Info Global", font=("Helvetica", 10, "bold"), bg="#3498DB", fg="white", width=12, command=self.tampil_info_global)
        self.btn_stats.grid(row=0, column=2, padx=5)

    def log(self, pesan):
        self.txt_log.config(state="normal")
        self.txt_log.insert(tk.END, pesan + "\n")
        self.txt_log.see(tk.END)
        self.txt_log.config(state="disabled")

    def update_status(self):
        # Update HP Bar & Label menggunakan @property hp
        self.bar_player_hp['value'] = (self.player.hp / self.player.hp_max) * 100
        self.bar_monster_hp['value'] = (self.monster.hp / self.monster.hp_max) * 100

        # Memanfaatkan special method __str__ secara dinamis
        self.lbl_player_info.config(text=str(self.player))
        self.lbl_monster_info.config(text=str(self.monster))

    def aksi_serang(self):
        if self.player.hp <= 0 or self.monster.hp <= 0:
            return

        # Turn Player (Memanggil Static Method)
        is_crit = GameHelper.cek_critical(peluang=0.35)
        dmg = self.player.serang(self.monster, is_critical=is_crit)
        
        crit_msg = " [CRITICAL HIT!]" if is_crit else ""
        self.log(f"⚔️ {self.player.nama} menyerang {self.monster.nama}{crit_msg} -> {dmg} damage!")

        # Cek Kemenangan
        if self.monster.hp <= 0:
            exp = GameHelper.hitung_exp(level_lawan=2)
            self.log(f"\n🎉 {self.player.nama} MENANG! Mendapatkan +{exp} EXP.")
            messagebox.showinfo("Kemenangan", f"Selamat! {self.player.nama} berhasil mengalahkan {self.monster.nama}!")
            self.nonaktifkan_tombol()
            self.update_status()
            return

        # Turn Monster (Counter Attack)
        is_crit_monster = GameHelper.cek_critical(peluang=0.20)
        dmg_m = self.monster.serang(self.player, is_critical=is_crit_monster)
        self.log(f"👹 {self.monster.nama} membalas -> {dmg_m} damage!\n")

        # Cek Kekalahan
        if self.player.hp <= 0:
            self.log(f"\n☠️ {self.player.nama} GUGUR di medan perang!")
            messagebox.showwarning("Kekalahan", f"{self.player.nama} telah kalah!")
            self.nonaktifkan_tombol()

        self.update_status()

    def aksi_heal(self):
        if self.player.hp <= 0 or self.monster.hp <= 0:
            return

        heal_amount = self.player.heal(20)
        self.log(f"🧪 {self.player.nama} menggunakan Potion -> HP bertambah +{heal_amount}")

        # Monster tetap menyerang saat player heal
        dmg_m = self.monster.serang(self.player, is_critical=False)
        self.log(f"👹 {self.monster.nama} menyerang saat kamu heal -> {dmg_m} damage!\n")

        if self.player.hp <= 0:
            self.log(f"\n☠️ {self.player.nama} GUGUR!")
            self.nonaktifkan_tombol()

        self.update_status()

    def tampil_info_global(self):
        # Memanggil Class Method info_global()
        info = Karakter.info_global()
        messagebox.showinfo("Statistik Global (Class Method)", info)

    def nonaktifkan_tombol(self):
        self.btn_attack.config(state="disabled")
        self.btn_heal.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = BattleArenaGUI(root)
    root.mainloop()