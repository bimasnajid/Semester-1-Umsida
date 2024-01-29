# nomer 1
# def hitung_nilai_akhir(uts, uas):
#     rata_rata = (uts + uas) / 2
#     if rata_rata >= 80:
#         return 'A'
#     elif rata_rata >= 70:
#         return 'B'
#     elif rata_rata >= 60:
#         return 'C'
#     elif rata_rata >= 50:
#         return 'D'
#     else:
#         return 'E'

# nama = input("Masukkan nama: ")
# nim = input("Masukkan NIM: ")
# nilai_uts = float(input("Masukkan nilai UTS: "))
# nilai_uas = float(input("Masukkan nilai UAS: "))

# nilai_akhir = hitung_nilai_akhir(nilai_uts, nilai_uas)

# print("\n=== Hasil Perhitungan ===")
# print("Nama:", nama)
# print("NIM:", nim)
# print("Nilai UTS:", nilai_uts)
# print("Nilai UAS:", nilai_uas)
# print("Nilai Akhir:", nilai_akhir)

# nomer 2
# baris = int(input("Masukkan jumlah baris: "))

# i = baris
# while i >= 0:
#     j = i
#     while j > 0:
#         print("*", end=" ")
#         j -= 1
#     print()
#     i -= 1

# nomer 3
# panjang = int(input("Masukkan panjang sisi: "))
# lebar = int(input("Masukkan lebar sisi: "))

# for i in range(panjang):
#     for j in range(lebar):
#         if i == 0 or i == panjang - 1 or j == 0 or j == lebar - 1:
#             print("$", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# nomer 4
# tinggi = int(input("Masukkan tinggi segitiga: "))

# for i in range(1, tinggi + 1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# Nomor 5
# nama = input("Masukkan nama: ")
# umur = int(input("Masukkan usia: "))

# if 10 <= umur <= 17:
#     print(nama, "termasuk pemain anak-anak/remaja")
# elif 18 <= umur <= 30:
#     print(nama, "termasuk pemain muda/dewasa")
# elif umur > 30:
#     print(nama, "termasuk pemain tua/veteran")
# else:
#     print(nama, "termasuk pemain dibawah umur")

# Nomor 6
# n = 5

# for i in range(1, n+1):
#     for j in range(i):
#         print(i, end="")
#     print()
