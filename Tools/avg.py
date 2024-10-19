#ini adalah algoritma untuk mencari nilai rata rata
import sys
import os
from time import sleep

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

def average():
	os.system('clear')
	print(f'''{G}╔════════════════════════════════════════════════════╗\n║  {W} Mencari nilai pembayaran rata-rata untuk acara   {G}║\n╚════════════════════════════════════════════════════╝''')
	uang = "Ribu"
	jumlah_peserta = int(input(f'\n{YY}× {W}berapa jumlah peserta:{Y} '))
	tiket_masuk = int(input(f'{GG}$ {W}berapa harga tiket masuk per orang:{GG} '))
	konsumsi = int(input(f'{CC}$ {W}berapa biaya konsumsi per orang:{GL} '))
	biaya_travel = int(input(f'{BB}$ {W}berapa biaya bus travel:{BB} '))

	avg = ((tiket_masuk * jumlah_peserta) + (konsumsi * jumlah_peserta) + biaya_travel) / jumlah_peserta
	avg = int(avg)
	print(f'''\n{CC}Menghitung harga rata² yang harus dibayar''')
	print(f"\n{W}[ ({GG}{tiket_masuk}{RR} × {YY}{jumlah_peserta}){RR} + ({GL}{konsumsi}{RR} × {YY}{jumlah_peserta}){RR} + {BB}{biaya_travel} ){CC} ÷{YY} {jumlah_peserta} {W}]")
	sleep(1)
	print(f"\nSetiap peserta harus membayar: {GG}{avg}{W} Ribu Rupiah")

if __name__ == "__main__":
	average()
