# Tugas Praktikum 3

* Buat repository baru **Labspy03**
* Masukan **Latihan1.py** dan **Latihan2.py** kedalam repository.
* Buat program sederhana dengan perulangan : **Program1.py**
"Seorang pengusaha menginvestasikan uangnya untuk memulai usaha dengan modal awal 100 juta, pada bulan pertama dan kedua belum mendapatkan laba. Pada bulan ketiga baru mulai mendapatkan laba sebesar 1%, dan pada bulan kelima pendapatan meningkat 5%, selanjutnya pada bulan kedelapan mengalami penurunan keuntungan sebesar 2%, sehingga laba menjadi 3%. Hitung total keuntungan selama 8 bulan berjalan usahanya."
* Buat file **Radme.md** yang berisi penjelasan alur algoritma program latihan1.py, latihan2.py, dan program1.py beserta screenshoot hasilnya.
* Commit dan push ke repository




# Latihan1.py
```
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
```
* Masukan data berupa tipe data integer 
```
num = int(input("Masukkan Nilai N:"))
```
* Memberikan nilai acak dalam tipe data float
```
from random import random
a = random()
```
* Fungsi ```for``` sebagai perulangan atau looping yang mengacu pada nilai ```N```
```
for i in range ( start, stop, step):
    print("Data ke:", i, "->", (a))
```
* Mencetak hasil perulangan yang terjadi dan menghasilkan variabel nilai antara 0 sampai 0.5 sebanyak ```range(N)```
* Output :

![latihan1](https://user-images.githubusercontent.com/56512562/72221464-a00ba500-358d-11ea-99e9-70441b891e3c.png)

# Latihan2.py
```
# Latihan 2
a = int()
b = int()

while a>= 0:
    a=int(input("Masukkan Bilangan: "))
    if a == 0:
        break
    if a > b:
        b = a
print("Bilangan terbesar adalah: ", b)
print("Selesai")
```
* Perulangan yang dipakai terus menerus bila memenuhi syarat ```while a>= 0:```
* Masukan data berupa tipe data integer ```a=int(input("Masukkan Bilangan: "))```
* Kondisi perulangan jika nilai
 ```   
    if a == 0:
        break
 ``` 
 maka statment dinyatakan selesai.
 * Kondisi perulangan mencari nilai terbesar tanpa dibatasi
 ```
 if a > b:
        b = a
 ```
 * Mencetak bilangan terbesar dan hasil dinyatakan selesai
 ```
 print("Bilangan terbesar adalah: ", b)
 print("Selesai")
 ```
 * Output
 
![latihan2](https://user-images.githubusercontent.com/56512562/72221599-ffb68000-358e-11ea-9870-22dd281a6f21.png)

# Program1.py
"Seorang pengusaha menginvestasikan uangnya untuk memulai usaha dengan modal awal 100 juta, pada bulan pertama dan kedua belum mendapatkan laba. Pada bulan ketiga baru mulai mendapatkan laba sebesar 1%, dan pada bulan kelima pendapatan meningkat 5%, selanjutnya pada bulan kedelapan mengalami penurunan keuntungan sebesar 2%, sehingga laba menjadi 3%. Hitung total keuntungan selama 8 bulan berjalan usahanya."
```
# Program 1

modal = 100000000
laba = 0
untung = 0

for i in range(1, 9):
    if(i < 3):
        laba = 0
        untung = untung + laba
    elif(i < 5):
        laba = modal*1/100
        untung = untung + laba
    elif(i < 8):
        laba = modal*5/100
        untung = untung + laba
    else:
        laba = modal*2/100
        untung = untung + laba
    print("Laba bulan ke", i, "Sebesar:", laba)
print("Total laba adalah:", untung)
```
* Deklarasi variabel
```
modal = 100000000
laba = 0
untung = 0
```
* Menentukan jumlah perulangan yang mewakili bulan ```for i in range(1, 9):```
* Menghitung presentase penjualan dalam beberapa bulan
```
    if(i < 3):
        laba = 0
        untung = untung + laba
    elif(i < 5):
        laba = modal*1/100
        untung = untung + laba
    elif(i < 8):
        laba = modal*5/100
        untung = untung + laba
 ```
 * Kondisi yang menyatakan penghitungan laba dan mencetak hasil sekaligus
 ```
 else:
        laba = modal*2/100
        untung = untung + laba
    print("Laba bulan ke", i, "Sebesar:", laba)
print("Total laba adalah:", untung)
```
* Output

![program1](https://user-images.githubusercontent.com/56512562/72221793-7a33cf80-3590-11ea-8486-6b3c74e35bfd.png)

# Terima Kasih
