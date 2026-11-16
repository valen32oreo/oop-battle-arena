import tkinter as tk
from tkinter import messagebox

from models import Karakter
from helpers import GameHelper


class FlatButton(tk.Button):
    """Widget Tombol Flat Kustom dengan Efek Hover."""
    def __init__(self, parent, bg_color, hover_color, text_color="#FFFFFF", **kwargs):
        super().__init__(
            parent,
            bg=bg_color,
            fg=text_color,
            activebackground=hover_color,
            activeforeground=text_color,
            bd=0,
            relief="flat",
            cursor="hand2",
            font=("Segoe UI", 9, "bold"),
            padx=16,
            pady=8,
            **kwargs
        )
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.bind("<Enter>", lambda e: self.config(bg=self.hover_color) if self["state"] != "disabled" else None)
        self.bind("<Leave>", lambda e: self.config(bg=self.bg_color) if self["state"] != "disabled" else None)


class CustomHPBar(tk.Canvas):
    """Indikator HP Bar Kustom Berbasis Canvas."""
    def __init__(self, parent, width=220, height=14, bg_color="#0F172A", fill_color="#10B981"):
        super().__init__(parent, width=width, height=height, bg=bg_color, highlightthickness=1, highlightbackground="#334155")
        self.fill_color = fill_color
        self.bar_width = width
        self.bar_height = height

    def update_hp(self, current, max_val):
        self.delete("all")
        percentage = max(0, min(1, current / max_val))
        fill_w = int(self.bar_width * percentage)
        if fill_w > 0:
            self.create_rectangle(0, 0, fill_w, self.bar_height, fill=self.fill_color, width=0)


class BattleArenaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("OOP Battle Arena")
        self.root.geometry("640x630")
        self.root.configure(bg="#0F172A")
        self.root.resizable(False, False)

        # Inisialisasi Objek Karakter (Constructor & Validation)
        try:
            self.player = Karakter("Knight Valen", hp_awal=100, attack=25, armor=8)
            self.monster = Karakter("Shadow Demon", hp_awal=90, attack=22, armor=4)
        except ValueError as e:
            messagebox.showerror("Error Inisialisasi", str(e))
            self.root.destroy()
            return

        self.setup_ui()
        self.update_status()
        self.tampilkan_log_awal()

    def setup_ui(self):
        # Header Utama
        header_frame = tk.Frame(self.root, bg="#0F172A")
        header_frame.pack(pady=(14, 6))

        lbl_title = tk.Label(
            header_frame,
            text="⚔️ OOP BATTLE ARENA",
            font=("Segoe UI", 15, "bold"),
            fg="#F8FAFC",
            bg="#0F172A"
        )
        lbl_title.pack()

        # Panel Kartu Karakter
        cards_container = tk.Frame(self.root, bg="#0F172A")
        cards_container.pack(fill="x", padx=20, pady=4)

        # --- Kartu Player (Kiri) ---
        card_player = tk.Frame(cards_container, bg="#1E293B", padx=14, pady=12, highlightthickness=1, highlightbackground="#334155")
        card_player.pack(side="left", expand=True, fill="both", padx=(0, 5))

        tk.Label(card_player, text="HERO PLAYER", font=("Segoe UI", 8, "bold"), fg="#10B981", bg="#1E293B").pack(anchor="w")
        self.lbl_player_name = tk.Label(card_player, text=self.player.nama, font=("Segoe UI", 11, "bold"), fg="#F8FAFC", bg="#1E293B")
        self.lbl_player_name.pack(anchor="w", pady=(2, 4))

        self.lbl_player_stats = tk.Label(card_player, text="", font=("Segoe UI", 9), fg="#94A3B8", bg="#1E293B", justify="left")
        self.lbl_player_stats.pack(anchor="w", pady=(0, 6))

        self.hp_bar_player = CustomHPBar(card_player, width=230, fill_color="#10B981")
        self.hp_bar_player.pack(anchor="w")

        # --- Kartu Monster (Kanan) ---
        card_monster = tk.Frame(cards_container, bg="#1E293B", padx=14, pady=12, highlightthickness=1, highlightbackground="#334155")
        card_monster.pack(side="right", expand=True, fill="both", padx=(5, 0))

        tk.Label(card_monster, text="ENEMY MONSTER", font=("Segoe UI", 8, "bold"), fg="#F43F5E", bg="#1E293B").pack(anchor="w")
        self.lbl_monster_name = tk.Label(card_monster, text=self.monster.nama, font=("Segoe UI", 11, "bold"), fg="#F8FAFC", bg="#1E293B")
        self.lbl_monster_name.pack(anchor="w", pady=(2, 4))

        self.lbl_monster_stats = tk.Label(card_monster, text="", font=("Segoe UI", 9), fg="#94A3B8", bg="#1E293B", justify="left")
        self.lbl_monster_stats.pack(anchor="w", pady=(0, 6))

        self.hp_bar_monster = CustomHPBar(card_monster, width=230, fill_color="#F43F5E")
        self.hp_bar_monster.pack(anchor="w")

        # --- Log Pertarungan ---
        log_frame = tk.Frame(self.root, bg="#1E293B", padx=10, pady=8, highlightthickness=1, highlightbackground="#334155")
        log_frame.pack(fill="both", expand=True, padx=20, pady=10)

        tk.Label(log_frame, text="LOG PERTARUNGAN", font=("Segoe UI", 9, "bold"), fg="#94A3B8", bg="#1E293B").pack(anchor="w", pady=(0, 4))

        self.txt_log = tk.Text(log_frame, height=8, state="disabled", font=("Consolas", 9), bg="#020617", fg="#F8FAFC", bd=0, highlightthickness=0, wrap="word")
        self.txt_log.pack(fill="both", expand=True)

        self.txt_log.tag_config("player", foreground="#34D399")
        self.txt_log.tag_config("monster", foreground="#FB7185")
        self.txt_log.tag_config("crit", foreground="#FBBF24", font=("Consolas", 9, "bold"))
        self.txt_log.tag_config("heal", foreground="#60A5FA")
        self.txt_log.tag_config("system", foreground="#94A3B8", font=("Consolas", 9, "italic"))

        # --- Tombol Aksi ---
        btn_frame = tk.Frame(self.root, bg="#0F172A")
        btn_frame.pack(pady=(0, 14))

        self.btn_attack = FlatButton(btn_frame, bg_color="#EF4444", hover_color="#DC2626", text="⚔️ Serang", command=self.aksi_serang)
        self.btn_attack.grid(row=0, column=0, padx=6)

        self.btn_heal = FlatButton(btn_frame, bg_color="#10B981", hover_color="#059669", text="🧪 Potion (+20)", command=self.aksi_heal)
        self.btn_heal.grid(row=0, column=1, padx=6)

        self.btn_stats = FlatButton(btn_frame, bg_color="#3B82F6", hover_color="#2563EB", text="📊 Info Global", command=self.tampil_info_global)
        self.btn_stats.grid(row=0, column=2, padx=6)

    def log(self, pesan, tag="system"):
        self.txt_log.config(state="normal")
        self.txt_log.insert(tk.END, pesan + "\n", tag)
        self.txt_log.see(tk.END)
        self.txt_log.config(state="disabled")

    def tampilkan_log_awal(self):
        """Menampilkan header (staticmethod) dan status awal karakter (__str__)."""
        self.log(GameHelper.format_header("PERTARUNGAN DIMULAI"), "system")
        self.log(str(self.player), "player")
        self.log(str(self.monster), "monster")

    def update_status(self):
        self.hp_bar_player.update_hp(self.player.hp, self.player.hp_max)
        self.hp_bar_monster.update_hp(self.monster.hp, self.monster.hp_max)

        self.lbl_player_stats.config(
            text=f"HP: {self.player.hp}/{self.player.hp_max}\nAttack: {self.player.attack} | Armor: {self.player.armor}"
        )
        self.lbl_monster_stats.config(
            text=f"HP: {self.monster.hp}/{self.monster.hp_max}\nAttack: {self.monster.attack} | Armor: {self.monster.armor}"
        )

    def cek_akhir_pertarungan(self):
        """Mengecek pemenang. Mengembalikan True jika pertarungan sudah selesai."""
        if self.monster.hp <= 0:
            exp = GameHelper.hitung_exp(level_lawan=2)
            self.log(f"\n🎉 {self.player.nama} MENANG! Mendapatkan +{exp} EXP.", "crit")
            self.nonaktifkan_tombol()
            messagebox.showinfo("Kemenangan", f"Selamat! {self.player.nama} berhasil mengalahkan {self.monster.nama}!")
            return True

        if self.player.hp <= 0:
            self.log(f"\n☠️ {self.player.nama} GUGUR di medan perang!", "monster")
            self.nonaktifkan_tombol()
            messagebox.showwarning("Kekalahan", f"{self.player.nama} telah kalah!")
            return True

        return False

    def aksi_serang(self):
        if self.player.hp <= 0 or self.monster.hp <= 0:
            return

        is_crit = GameHelper.cek_critical(peluang=0.35)
        dmg = self.player.serang(self.monster, is_critical=is_crit)

        if is_crit:
            self.log(f"💥 CRITICAL HIT! {self.player.nama} menyerang -> {dmg} damage!", "crit")
        else:
            self.log(f"⚔️ {self.player.nama} menyerang {self.monster.nama} -> {dmg} damage", "player")

        # Perbarui tampilan dulu, baru popup (agar HP bar sudah sesuai saat popup muncul)
        self.update_status()
        if self.cek_akhir_pertarungan():
            return

        is_crit_monster = GameHelper.cek_critical(peluang=0.20)
        dmg_m = self.monster.serang(self.player, is_critical=is_crit_monster)
        self.log(f"👹 {self.monster.nama} membalas -> {dmg_m} damage", "monster")

        self.update_status()
        self.cek_akhir_pertarungan()

    def aksi_heal(self):
        if self.player.hp <= 0 or self.monster.hp <= 0:
            return

        heal_amount = self.player.heal(20)
        self.log(f"🧪 {self.player.nama} meminum Potion -> HP +{heal_amount}", "heal")

        dmg_m = self.monster.serang(self.player, is_critical=False)
        self.log(f"👹 {self.monster.nama} menyerang saat heal -> {dmg_m} damage", "monster")

        self.update_status()
        self.cek_akhir_pertarungan()

    def tampil_info_global(self):
        info = Karakter.info_global()
        messagebox.showinfo("Statistik Global (Class Method)", info)

    def nonaktifkan_tombol(self):
        self.btn_attack.config(state="disabled", bg="#475569")
        self.btn_heal.config(state="disabled", bg="#475569")


if __name__ == "__main__":
    root = tk.Tk()
    app = BattleArenaGUI(root)
    root.mainloop()