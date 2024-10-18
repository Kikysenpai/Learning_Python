#!usr
# -*- coding: UTF-8 -*-
# mod by: Risky Ali
# team: life of programmer


import os
import sys
import time
import random
import mechanize
from time import sleep
from avg import average

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


def pilihan():
    pilih = int(input(f"\n{CC}Choose your tools \n\n{W}1.Menghitung Rata²\n{W}2.Algorithm\n\n{Y}Masukkan pilihanmu :{GG}  "))
    if pilih == 1:
    	average()
    if pilih == 2:
    	print(f"{Y}ini Algorithm")

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
