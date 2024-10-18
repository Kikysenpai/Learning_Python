import random
from time import sleep

posisi_hadiah = random.randint(1,5)
bentuk = "|_|"
kosong = [bentuk] * 5

hadiah = kosong.copy()
hadiah[posisi_hadiah - 1] = "|$|"

kosong = "   ".join(kosong)
hadiah = "   ".join(hadiah)
def tebak():
    pilih = int(input(f"Perhtikan 5 kotah dibawah ini\n\n {kosong}\n\n Menurutmu kotak nomor berapakah yang berisi hadiah: "))
    if pilih == posisi_hadiah:
        print(f"\n{hadiah}\n\nSelamat Pilihanmu Benar, Nikmati Hadiahnya ")
    else:
        print(f"\n{hadiah}\n\nMaaf kamu kurang beruntung, Hadiah berada di kotak ke {posisi_hadiah}")


if __name__ == "__main__":
    tebak()