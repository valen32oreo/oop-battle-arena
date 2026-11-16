import time
from models import Karakter
from helpers import GameHelper

def main():
    print(GameHelper.format_header("WELCOME TO OOP BATTLE ARENA"))

    # Inisialisasi Karakter (Object Instantiation & Constructor)
    try:
        player = Karakter("Knight Valen", hp_awal=100, attack=25, armor=8)
        monster = Karakter("Shadow Demon", hp_awal=85, attack=22, armor=4)
    except ValueError as e:
        print(f"Error saat pembuatan karakter: {e}")
        return

    print("\n--- STATUS AWAL KARAKTER ---")
    print(player)
    print(monster)

    ronde = 1

    # Game Loop Pertarungan Interaktif
    while player.hp > 0 and monster.hp > 0:
        print(GameHelper.format_header(f"RONDE {ronde}"))
        
        # Turn Player
        is_crit_player = GameHelper.cek_critical(peluang=0.35)
        player.serang(monster, is_critical=is_crit_player)
        
        if monster.hp <= 0:
            print(f"\n🎉 WINNER! {player.nama} berhasil mengalahkan {monster.nama}!")
            exp_gained = GameHelper.hitung_exp(level_lawan=2)
            print(f"✨ Mendapatkan +{exp_gained} EXP!")
            break

        time.sleep(1)

        # Turn Monster
        is_crit_monster = GameHelper.cek_critical(peluang=0.20)
        monster.serang(player, is_critical=is_crit_monster)

        if player.hp <= 0:
            print(f"\n☠️ GAME OVER! {player.nama} telah gugur di medan perang.")
            break

        ronde += 1
        time.sleep(1)

    # Menampilkan Informasi Statistik Global (Class Method)
    print(GameHelper.format_header("GAME SELESAI"))
    print(Karakter.info_global())

if __name__ == "__main__":
    main()