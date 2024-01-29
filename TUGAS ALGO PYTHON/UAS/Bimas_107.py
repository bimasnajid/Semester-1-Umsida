# for kata in 'Bimas 107':
#   print (kata)

# buah = ['mangga', 'melon', 'jeruk']
# for buahku in buah :
#   print('Saya suka sekali dengan' + buahku)

# buah = {'mangga':'kuning', 'melon':'hijau', 'jeruk':'orange', 'anggur':'ungu'}
# for buahku in buah :
#     print (buahku + ' warnanya adalah ' + buah[buahku])

# buah = ['mangga','melon','jeruk']
# for buahku in buah :
#     print('saya suka sekali dengan ', buah)

# for i in range(10):
#   print("perulangan ke - ", i);

# for i in range(10, 20):
#   print("Nilai i =", i);

# for i in range(1, 30, 2):
#   print("Nilai i =", i );

# tupleBinatang = ("Kucing", "Anjing", "Burung","Ayam")
# for binatang in tupleBinatang:
#   print(binatang);

# karakter = "Bimas";
# for kata  in karakter:
#   print(kata);

# for i in range(10):
#   if (i == 6):
#     continue
#   print(i)

# for i in range(10):
#   if (i == 6):
#     break
#   print(i)

# namaKota = ["Sidoarjo", "Surabaya", "Mojokerto"]
# for kota in namaKota:
#   print(kota)
# else :
#   print("Selesai")

# i = 1
# while i <= 10:
#   print("Bimas 107")
#   i += 1

# nama = ["Amel", "Dean", "khafi", "Arsya", "Bimas"]

# i = 0
# while i < len(nama):
#   print(nama[i])
#   i += 1

# informatika=6
# while informatika>=6:
#     print(informatika)
#     if informatika == 15:
#         continue
#     informatika+=1

# i = 6 
# while i >= 6:
#   print(i)
#   if  i == 15:
#     break
#   i += 1

# x = 1;
# while x < 10:
#   print(x)
#   break
# else:
#   print("selesai")

# Model 2

# buah = []
# sayur = ["bayam"]

# print(buah)
# print(sayur)

# list1 = ['informatika', 'umsida', 2020, 2021]
# list2 = [1, 2, 3, 4, 5]
# list3 = ["a","b","c"]

# print(list1)
# print(list2)
# print(list3)

# angka = [1, 2, 3, 4, 5]
# list = ['ini', 'adalah', 'contoh', 'list']
# kampus = ['sidoarjo',2021, "A", "B"]

# print(angka[3])
# print(list[2])
# print(kampus[0])

# list1 = ['informatika','umsida', 2020, 2021]
# list2 = [1, 2, 3, 4, 5, 6, 7]

# print("list1[0]: ", list1[0])
# print("list2[1:5]: ", list2[1:5])

# list = ['aslab', 'informatika', 1945, 2021]
# print ("sekarang kita beranda pada tahun :", list[2])

# list[2] = 2022
# print ("sekarang kita berada pada tahun :", list[2])

# list = ['informatika', 'umsida', 2020, 2021]
# print("Nilai ada pada index 2 : ", list[2])

# list[2] = 2023
# print("nilai baru ada pada index 2 : ", list[2])

# list = ['aslab', 'informatika', 1945, 2021]
# print (list)
# del  list[2]
# print("setelah di hapus : ", list)

# Program contoh yang memanfaatkan list genap
# num = [-1,2,53,5, 50, 153, 91,87]
# genap = [x for x in num if x%2==0]
# print("liat angka", num)
# print("angka genap pada list tersebut :", genap)

# Program contoh yang memanfaatkan list ganjil
# num=[-1, 2, 53, 5, 50, 153, 91, 87]
# ganjil=[x for x in num if x%2!=0]
# print("list angka",num)
# print("angka ganjil pada list tersebut : ",ganjil)

# tup1 = ('fisika', 'kimia', 1993, 2017)
# tup2 = (1, 2, 3, 4, 5)
# tup3 = "a", "b","c","d"
# print(tup1)
# print(tup2)
# print(tup3)

# kosong = ()
# print (kosong)

# prodi = ('Informatika')
# fakultas = "Saintek",
# print(prodi)

# tup1 = ('Informatika','Mesin', 2000, 2021)
# tup2 = (1, 2, 3, 4, 5)

# print("tup1[0]" , tup1[0])

# print ("tup2[1:5]:", tup2[1:5])

# tup = ('Informatika', 'Mesin', 2000, 2021)
# print(tup)

# del tup

# tup = ('Industri','Elektro', 2020)
# print("Setelah menghapus tuple :", tup)

# tuple1 = ("Ini", "tuple", 1)
# tuple2 = ("ini", "tuple", 2)

# tuple3 = (tuple1, tuple2)

# print(tuple3)

# dict = {'Nama': 'Andika', 'Age': 18, 'Class': 'First'}
# print ("dict ['Nama']: ", dict['Nama'])
# print ("dict['Age']:", dict['Age'])

# dict = {'Name': 'Andika', 'Age': 15, 'Class': 'First'}
# dict ['Age'] = 19;
# dict ['University'] = "Universitas Muhammadiyah Sidoarjo"

# print ("dict ['Age']: ", dict['Age'])
# print ("dict ['University']: ", dict['University'])

# dict = {'Name': 'Andika', 'Age': 15, 'Class': 'First'}
# dict ['Age'] = 19;
# dict['University'] = "Universitas Muhammadiyah Sidoarjo" 

# print ("dict['Age']: ", dict['Age'])
# print ("dict['University]: ", dict ['University'])

# dict = {'Name': 'Putri', 'Age': 19, 'Class': 'First'}

# del dict['Name']
# dict.clear()
# del dict

# print("dict['Age']:", dict['Age'])
# print ("dict['University']: ", dict['University'])

# print ("\ncontoh  1")
# dic1 ={1:100, 2:200}
# dic2 ={3:300, 4:400}
# dic3 ={5:500, 6:600}
# dic4 = {}
# for d in (dic1, dic2, dic3): dic4.update(d)
# print(dic4)

# print("\ncontoh 2")
# d = {1: 100, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}
# cek_angka = 3
# if cek_angka in d:
#   print(cek_angka, 'tersedia dalam dictionary')
# else:
#   print(cek_angka,'tidak tersedia dalam dictionary')
  
# print("\ncontoh 3")
# d1 = {'a': 1000, 'b': 2000}
# d2 = {'x': 3000, 'y': 2000}
# d = d1.copy()
# d.update(d2)
# print(d)

# set_prodi = {"informatika", "industri", "mesin", "elektro"}
# for elemen in set_prodi:
#   print (set_prodi)

# set_prodi = {"informatika", "industri", "mesin", "elektro"}
# if "informatika" in set_prodi:
#   print("informatika ada dalam set_prodi")
# else:
#   print("informatika ad dalam set_prodi")

# set_prodi = {"informatika", "industri", "mesin", "elektro"}
# set_prodi.add("teknik")
# print(set_prodi)

# set_prodi = {"informatika", "industri", "mesin", "elektro"}
# set_prodi.clear()
# print(set_prodi)

# prodi = {"informatika", "industri", "mesin", "elektro"}
# fakultas = {"fst", "fpip", "fbhis", "fikes"}

# gabungan1 = prodi.union(fakultas)
# print(gabungan1)

# prodi.update(fakultas)
# print(gabungan1)

# MODUL 6 START

# def Hello() :
#   print("Hello World")
# Hello()

# def namaKalian () :
#   print("Bimas Najid, 231080200107")
# namaKalian()

# def coba () :
#   print("Hai nama saya Bimas, saya kuliah di UMSIDA")

# coba()

# def hitung () :
#   return 10 + 20
# tampil = hitung()
# print("Hasil Perhitungan :", tampil)

# def praktikum (bahasa) :
#   print("Saya sedang praktikum dengan menggunakan bahasa pemrograman ", bahasa)
# praktikum("Phython")

# def bio (nama, hobi) :
#   print("Hai namaku", nama, ", Saya mempunyai hobi ", hobi)
# bio("Bimas", "Bermain bulutangkis dan ngoding")

# def luas_segitiga(alas, tinggi) :
#   luas = (alas * tinggi) / 2
#   print ("Luas Segitiga adalah : ", luas)
# luas_segitiga(5,15)

# def luas_segitiga(alas, tinggi) :
#   luas = (alas * tinggi) / 2
#   return luas
# print("Luas Segitiga adalah : ", luas_segitiga(5,15))

# def hitung_umur (thn_sekarnag, thn_lahir) :
#   umur = thn_sekarnag - thn_lahir
#   print("Umurku sekarnag  : ", umur , "tahun")
# hitung_umur(2023, 2005)

# def makanan (makan, minum) :
#   print("Saya sedang makan : ", makan)
#   print("Saya sedang minum : ", minum)

# makan = input ("Masukkan nama makanan : ")
# minum = input ("Masukkan nama minuman : ")
# makanan(makan, minum)

# def praktikum(nama, nim, kelompok_parktikum):
#     print("Nama saya", nama)
#     print("Nim saya", nim)
#     print("Saya termasuk kelompok",kelompok_parktikum)

# nama = input("Masukkan nama anda : ")
# nim = input("Masukkan nim anda : ")
# kelompok_parktikum = input("Masukkan kelompok praktikum anda : ")

# praktikum(nama, nim,kelompok_parktikum)

# def penjumlahan (bil1, bil2) :
#   hasil = bil1 + bil2
#   return hasil
# bil1 = int(input ("Masukkan bilangan pertama : "))
# bil2 = int(input("Masukkan bilangan kedua : "))

# print("Hasil penjumlahan", penjumlahan(bil1, bil2))


# tugas modul 4 start
# List untuk menyimpan teman-teman
# teman_list = []

# # Jumlah teman yang akan dimasukkan
# jumlah_teman = int(input("Masukkan jumlah teman: "))

# # Perulangan untuk memasukkan data teman ke dalam list
# for i in range(jumlah_teman):
#     print(f"\nMasukkan data teman ke-{i+1}:")
    
#     # Membuat dictionary untuk setiap teman
#     teman = {}
    
#     # Memasukkan data teman
#     teman['nama'] = input("Nama: ")
#     teman['nim'] = input("NIM: ")
#     teman['jenis_kelamin'] = input("Jenis Kelamin: ")
#     teman['alamat'] = input("Alamat: ")
    
#     # Menambahkan dictionary teman ke dalam list
#     teman_list.append(teman)

# # Menampilkan hasil list teman
# print("\nDaftar Teman:")
# for teman in teman_list:
#     print(f"\nNama: {teman['nama']}")
#     print(f"NIM: {teman['nim']}")
#     print(f"Jenis Kelamin: {teman['jenis_kelamin']}")
#     print(f"Alamat: {teman['alamat']}")


# tugas modul 5 start
# from collections import deque
# antrian = deque(['jamal','samsul','adnan'])
# print(antrian)
# # menggunakan .append() untuk menambahkan list
# antrian.append('udin')
# antrian.append('baha')
# print(f'antrian setelah ditambahkan udin dan baha {antrian}')
# # menambahkan .popleft() untuk mengjapus list paling kiri
# antrian.popleft()
# print(f'antrian ketika antrian urutan pertama yaitu jamal di panggil{antrian}')
# antrian.popleft()
# print(f'antrian ketika antrian urutan kedua yaitu samsul di panggil{antrian}')
# antrian.popleft()
# print(f'antrian ketika antrian urutan ketiga yaitu adnan di panggil{antrian}')
# antrian.popleft()
# print(f'antrian ketika antrian urutan keempat yaitu udin di panggil{antrian}')
# antrian.popleft()
# print(f'antrian ketika antrian urutan kelima yaitu baha di panggil, maka antiran akan kosong{antrian}')

# tugas modul 6 start
# def biodata(nama,nim,ttl,kelamin,agama,telepon,email):
#     print(f'nama saya : {nama}')
#     print(f'nim saya : {nim}')
#     print(f'tanggal lahir saya : {ttl}')
#     print(f'kelamin : {kelamin}')
#     print(f'agama  : {agama}')
#     print(f'telepon  : {telepon}')
#     print(f'email  : {email}')
# nama = input('masukan nama : ')
# nim = int(input('masukan nim : '))
# ttl = input('masukan TTL : ')
# kelamin = input('Jenis kelamin : ')
# agama = input('Agama : ')
# telepon = int(input('No teleppon  : '))
# email = input('Email  : ')
# biodata(nama,nim,ttl,kelamin,agama,telepon,email)

# no 2
# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9/5) + 32

# def celsius_to_kelvin(celsius):
#     return celsius + 273.15

# def celsius_to_reamur(celsius):
#     return celsius * 4/5

# def main():
#     try:
#         celsius = float(input("Masukkan suhu dalam Celcius: "))
        
#         fahrenheit = celsius_to_fahrenheit(celsius)
#         kelvin = celsius_to_kelvin(celsius)
#         reamur = celsius_to_reamur(celsius)

#         print(f"{celsius} Celcius setara dengan:")
#         print(f"{fahrenheit:.2f} Fahrenheit")
#         print(f"{kelvin:.2f} Kelvin")
#         print(f"{reamur:.2f} Reamur")

#     except ValueError:
#         print("Input tidak valid. Harap masukkan suhu dalam bentuk angka.")

# if __name__ == "__main__":
#     main()

# no 3
# def cek_ganjil_genap(bilangan):
#     if bilangan % 2 == 0:
#         return "Genap"
#     else:
#         return "Ganjil"

# def main():
#     try:
#         bilangan = int(input("Masukkan sebuah bilangan: "))
#         hasil = cek_ganjil_genap(bilangan)
#         print(f"Bilangan {bilangan} adalah bilangan {hasil}.")
#     except ValueError:
#         print("Input tidak valid. Harap masukkan bilangan bulat.")

# if __name__ == "__main__":
#     main()
