import random

def tebak_angka():
    print("===== Selamat datang di permainan Tebak Angka! =====")
    print("Saya telah memilih angka antara 1 sampai 100.")
    print("Tugas Anda adalah menebaknya!\n")

    # Komputer memilih angka acak antara 1 dan 100
    angka_rahasia = random.randint(1, 100)
    tebakan = None
    percobaan = 0

    # Permainan berjalan sampai pemain berhasil menebak angka
    while tebakan != angka_rahasia:
        try:
            # Pemain memasukkan tebakan
            tebakan = int(input("Masukkan tebakan Anda: "))
            percobaan += 1

            # Memberikan petunjuk apakah tebakan terlalu besar atau kecil
            if tebakan < angka_rahasia:
                print("Terlalu rendah! Coba angka yang lebih besar.")
            elif tebakan > angka_rahasia:
                print("Terlalu tinggi! Coba angka yang lebih kecil.")
        except ValueError:
            # Mengatasi input yang bukan angka
            print("Input tidak valid! Harap masukkan angka.")

    # Ketika pemain menebak angka dengan benar
    print(f"\nSelamat! Anda berhasil menebak angka {angka_rahasia} dalam {percobaan} percobaan.")

# Memulai permainan
if __name__ == "__main__":
    tebak_angka()