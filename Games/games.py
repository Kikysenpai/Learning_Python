import random
import time

# Pemain memiliki nyawa, kekuatan, dan inventaris
class Player:
    def __init__(self):
        self.health = 100
        self.attack_power = 10
        self.inventory = []

    def attack(self):
        return random.randint(5, self.attack_power)

    def heal(self):
        if "Potion" in self.inventory:
            self.health += 30
            self.inventory.remove("Potion")
            print("Anda menggunakan Potion dan mendapatkan 30 poin kesehatan!")
        else:
            print("Anda tidak memiliki Potion!")

    def status(self):
        print(f"Nyawa Anda: {self.health}")
        print(f"Inventaris: {self.inventory}\n")

# Monster memiliki nyawa dan kekuatan
class Monster:
    def __init__(self):
        self.health = random.randint(20, 50)
        self.attack_power = random.randint(5, 15)

    def attack(self):
        return random.randint(3, self.attack_power)

# Fungsi untuk memulai permainan
def start_game():
    player = Player()
    print("Selamat datang di Dungeon Adventure!")
    print("Anda berada di dalam sebuah dungeon yang gelap dan menyeramkan.\n")
    time.sleep(1)

    while True:
        print("Apa yang ingin Anda lakukan?")
        print("1. Menjelajah ruangan")
        print("2. Lihat status")
        print("3. Keluar dari dungeon\n")

        choice = input("Pilih aksi (1/2/3): ")
        if choice == "1":
            explore(player)
            if player.health <= 0:
                print("Anda telah kalah dalam pertarungan! Permainan berakhir.")
                break
        elif choice == "2":
            player.status()
        elif choice == "3":
            print("Anda keluar dari dungeon dengan selamat! Permainan selesai.")
            break
        else:
            print("Pilihan tidak valid! Coba lagi.\n")

# Fungsi untuk menjelajah dungeon
def explore(player):
    event = random.choice(["monster", "treasure", "potion", "nothing"])

    if event == "monster":
        print("\nAnda menemukan monster!")
        monster = Monster()
        fight(player, monster)

    elif event == "treasure":
        print("\nAnda menemukan harta karun! Anda mendapatkan 50 koin emas.")
        player.inventory.append("Koin Emas")

    elif event == "potion":
        print("\nAnda menemukan potion! Anda menyimpan potion di inventaris Anda.")
        player.inventory.append("Potion")

    elif event == "nothing":
        print("\nAnda tidak menemukan apa-apa...")

# Fungsi untuk pertempuran
def fight(player, monster):
    while monster.health > 0 and player.health > 0:
        print(f"\nMonster memiliki {monster.health} nyawa tersisa.")
        print("Apa yang ingin Anda lakukan?")
        print("1. Serang")
        print("2. Gunakan Potion")
        print("3. Lari\n")

        choice = input("Pilih aksi (1/2/3): ")

        if choice == "1":
            damage = player.attack()
            print(f"Anda menyerang monster dan menyebabkan {damage} kerusakan!")
            monster.health -= damage

            if monster.health > 0:
                monster_damage = monster.attack()
                print(f"Monster menyerang balik dan menyebabkan {monster_damage} kerusakan!")
                player.health -= monster_damage
                player.status()

            if monster.health <= 0:
                print("Anda berhasil mengalahkan monster!")
                player.inventory.append("Koin Emas")

        elif choice == "2":
            player.heal()

        elif choice == "3":
            print("Anda berhasil melarikan diri!\n")
            break

        if player.health <= 0:
            print("Anda telah dikalahkan oleh monster!")
            break

# Memulai permainan
if __name__ == "__main__":
    start_game()
