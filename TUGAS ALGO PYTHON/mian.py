# print("Diagnosa kebutuhan susu sesuai umur anda")

# umur = int(input("Masukkan umur anda : "))

# if(umur<=5):
#     Susu= print("Kebutuhan susu yang anda butuhkan adalah Nutrisi AHA - DHA")

# elif(umur<=10):
#     Susu= print("Kebutuhan susu yang anda butuhkan adalah Nutrisi Active")
# elif(umur<=17):
#     Susu= print("Kebutuhan susu yang anda butclsuhkan adalah Nutrisi Teen")
# elif(umur<=25):
#     Susu= print("Kebutuhan susu yang anda butuhkan adalah Calsium Teen")
# elif(umur<=50):
#     Susu= print("Kebutuhan susu yang anda butuhkan adalah Calsium Active")
# elif(umur>50):
#     Susu= print("Kebutuhan susu yang anda butuhkan adalah Calsium Gold")

# nomer 2 masseh
# def cek_bilangan(bilangan):
#     if bilangan > 0 and bilangan % 2 == 0:
#         print("Bilangan bulat positif genap")
#     elif bilangan > 0 and bilangan % 2 != 0:
#         print("Bilangan bulat positif ganjil")
#     elif bilangan < 0 and bilangan % 2 == 0:
#         print("Bilangan bulat negatif genap")
#     elif bilangan < 0 and bilangan % 2 != 0:
#         print("Bilangan bulat negatif ganjil")
#     else:
#         print("Bilangan bulat nol")

# # Menerima input dari pengguna
# bilangan = int(input("Masukkan bilangan bulat: "))
# cek_bilangan(bilangan)

# nomer 3 masseh
# def hitung_upah(golongan, jam_kerja):
#     if golongan == 1:
#         upah_per_jam = 7000
#         upah_lembur_per_jam = 3000
#     elif golongan == 2:
#         upah_per_jam = 8000
#         upah_lembur_per_jam = 4000
#     elif golongan == 3:
#         upah_per_jam = 9000
#         upah_lembur_per_jam = 5000
#     else:
#         print("Golongan tidak valid")
#         return

#     if jam_kerja > 10:
#         jam_biasa = 10
#         jam_lembur = jam_kerja - 10
#     else:
#         jam_biasa = jam_kerja
#         jam_lembur = 0

#     upah = (jam_biasa * upah_per_jam) + (jam_lembur * upah_lembur_per_jam)
#     return upah

# # Input golongan dan jam kerja per hari dari karyawan
# golongan = int(input("Masukkan golongan karyawan (1/2/3): "))
# jam_kerja = int(input("Masukkan jumlah jam kerja per hari: "))

# total_upah = hitung_upah(golongan, jam_kerja)
# if total_upah is not None:
#     print(f"Upah karyawan per hari adalah: {total_upah}")

# nomer 4 masseh
# def kategori_berat_badan(tinggi_badan, berat_badan):
#     berat_ideal = (100 - tinggi_badan) * 0.9
#     selisih = berat_ideal - berat_badan
#     persentase_selisih = (selisih / berat_ideal) * 100

#     if persentase_selisih < -20:
#         return "Obesitas"
#     elif -20 <= persentase_selisih <= -10:
#         return "Kelebihan berat badan"
#     elif -10 < persentase_selisih < 10:
#         return "Normal"
#     elif 10 <= persentase_selisih <= 20:
#         return "Kurus"
#     else:
#         return "Kategori tidak dapat ditentukan"

# # Input tinggi badan (dalam cm) dan berat badan (dalam kg)
# tinggi = float(input("Masukkan tinggi badan (dalam cm): "))
# berat = float(input("Masukkan berat badan (dalam kg): "))

# hasil_kategori = kategori_berat_badan(tinggi, berat)
# print(f"Kategori berat badan: {hasil_kategori}")
