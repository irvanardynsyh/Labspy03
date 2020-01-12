# Latihan 1

num = int(input("Masukkan Nilai N:"))

from random import random
a = random()

jumlah = num+1
start = 1
stop = jumlah
step = 1
for i in range ( start, stop, step):
    print("Data ke:", i, "->", (a))
print("Selesai")
