# def lagu_anak_ayam(n):
#     for i in range(n, 0, -1):
#         if i == 1:
#             print(f"Anak ayam turun {i}, mati satu tinggal induknya")
#         else:
#             print(f"Anak ayam turun {i}, mati satu tinggal {i-1}")

# n = int(input("Masukkan jumlah anak ayam semula : "))
# lagu_anak_ayam(n)

# #penghitung
# counter = 0

# # Inputan user
# teks_input = input("Input karakter: ")

# while teks_input != '.':
#     counter += len(teks_input)
#     teks_input = input("Input karakter lagi: ")

# print("Jumlah karakter =", counter)


# nomor 3
# Inisialisasi counter
counter = 0

# Membaca bilangan pertama dari keyboard
bilangan = int(input("Masukkan bilangan bulat (ketik -1 untuk mengakhiri): "))

# Melakukan pengulangan hingga ditemui bilangan -1
while bilangan != -1:
    # Memeriksa apakah bilangan adalah bilangan genap
    if bilangan % 2 == 0:
        counter = counter + 1
    
    # Membaca bilangan berikutnya dari keyboard
    bilangan = int(input("Masukkan bilangan bulat (ketik -1 untuk mengakhiri): "))

# Menampilkan jumlah kemunculan bilangan genap
print("Jumlah bilangan genap:", counter)

# nomer 2 cadangan
# def hitung_jumlah_karakter():
#     counter = 0
#     karakter = ""

#     while karakter != '.':
#         karakter = input("Masukkan karakter (ketik titik untuk berhenti): ")
        
#         if karakter != '.':
#             counter += 1

#     print(f"Jumlah karakter (tanpa titik) = {counter}")

# # Panggil fungsi untuk menjalankan program
# hitung_jumlah_karakter()

# nomor 4
# Fungsi untuk menghitung KPK
# def hitung_kpk(bilangan1, bilangan2):
#     # Inisialisasi variabel untuk menyimpan hasil KPK
#     kpk = max(bilangan1, bilangan2)

#     while True:
#         if kpk % bilangan1 == 0 and kpk % bilangan2 == 0:
#             # Jika KPK ditemukan, keluar dari loop
#             break
#         kpk += 1

#     return kpk

# # Input dua bilangan bulat dari pengguna
# bilangan1 = int(input("Masukkan bilangan bulat pertama: "))
# bilangan2 = int(input("Masukkan bilangan bulat kedua: "))

# # Memanggil fungsi untuk menghitung KPK
# hasil_kpk = hitung_kpk(bilangan1, bilangan2)

# # Menampilkan hasil KPK
# print(f"KPK dari {bilangan1} dan {bilangan2} adalah: {hasil_kpk}")


# nomor 5
# # Fungsi untuk menghitung KPK
# def hitung_kpk(bilangan1, bilangan2):
#     kpk = max(bilangan1, bilangan2)

#     while True:
#         if kpk % bilangan1 == 0 and kpk % bilangan2 == 0:
#             break
#         kpk += 1

#     return kpk

# bilangan1 = int(input("Masukkan bilangan bulat pertama: "))
# bilangan2 = int(input("Masukkan bilangan bulat kedua: "))

# hasil_kpk = hitung_kpk(bilangan1, bilangan2)

# # Menampilkan hasil KPK
# print(f"KPK dari {bilangan1} dan {bilangan2} adalah: {hasil_kpk}")


# Inisialisasi counter
counter = 0

# Membaca bilangan pertama dari keyboard
bilangan = int(input("Masukkan bilangan bulat (ketik -1 untuk mengakhiri): "))

# Melakukan pengulangan hingga ditemui bilangan -1
while bilangan != -1:
    if bilangan % 2 == 0:
        counter = counter + 1
    
    bilangan = int(input("Masukkan bilangan bulat (ketik -1 untuk mengakhiri): "))

print("Jumlah bilangan genap:", counter)
