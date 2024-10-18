#!usr
# -*- coding: UTF-8 -*-
# mod by: Risky Ali
# team: life of programmer


import os
import sys
import time
from time import sleep
import Games.games
import Games.tebak_angka
import Games.tebak_isi_kotak
from Tools import banner
from Tools import avg
import Games

wd = "\033[90;1m" # dark
GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"  # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"   # White
R = "\033[31m"    # Red
C = "\033[36;1m"  # Cyan

def runntxt(s):
        for noobs in s + '\n':
                sys.stdout.write(noobs)
                sys.stdout.flush()
                time.sleep(8. / 2100)

def pilih_game():
        chose_games = int(input(f"1. Dungeon Games\n2. Tebak Angka\n3. Tebak isi kotak\n\n Silahkan Pilih: "))
        if chose_games == 1:
            Games.games.start_game()
        elif chose_games == 2:
            Games.tebak_angka.tebak_angka()
        elif chose_games == 3:
            Games.tebak_isi_kotak.tebak()
        else:
            print(f"\nPilihan Tidak Tepat. {pilihan}")

def pilihan():
    pilih = int(input(f"\n{CC}Selamat Datang di program python sederhana\n Silahkan pilih Program dibawah  \n\n{W}1.Games\n{W}2.Tools\n\n{Y}Masukkan pilihanmu :{GG}  "))
    if pilih == 1:
        pilih_game()
    if pilih == 2:
    	avg.average

def stop():
	runntxt(RR+'Program akan dihentikan')
	sleep(1)
	print(f"{G}3...")
	sleep(1)
	print("2...")
	sleep(1)
	print("1...")
	sleep(1)
	print(f"{RR}Program Berhenti")

def banner():
    os.system('clear')
    print("\n")
    runntxt(GL+"╭━━━━━━━╮ ╔════════════════╗")
    runntxt(WW+'┃... •● | ║ W E L C O M E  ╚═╗')
    runntxt(GL+'┃███████┃ ║ R I S K Y  A L I ║')
    runntxt(GG+'┃███████┃ ║ E N J O Y        ╚═╗')
    runntxt(WW+'┃███████┃ ║ Y O U R  T O O L S ║')
    runntxt(GG+'┃███████┃ ║ I N                ║')
    runntxt(Y+'┃███████┃ ║ T E R M U X        ╚╗')
    runntxt(B+'┃ # = > ┃ ╚═════════════════════╝	')
    runntxt(BB+'╰━━━━━━━╯	')

if __name__ == "__main__":
    banner()
    pilihan()
    stop()
