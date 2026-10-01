import sys

print("===============================================================")
print("Lembaga Kursus Bahasa inggris" .center(62)) 
print("===============================================================")

print("Login" .center(62))
print("===============================================================")

username = input("Masukkan Username : ")
Password = input("Masukkan Password : ")

if username == "Rheezam" and Password == "028":
    print("Login Berhasil, Lanjut menu berikutnya")

else:
    print("Username atau Password anda salah, Silahkan input ulang")

    for i in range(2):
        username = input("Masukkan Username : ")
        Password = input("Masukkan Password : ")

        if username == "Rheezam" and Password == "028":
            print("Login Berhasil, Lanjut menu berikutnya")
            break

        else:
            print("Username atau Password anda salah")

    else:
        print("Sudah percobaan ke 3, Silahkan dicoba lagi lain waktu")
        sys.exit()

print("===============================================================")
print("Input data siswa" .center(62))
print("===============================================================")

DataSiswa = []

while True:
    NamaSiswa = input("Masukkan Nama siswa : ")
    Kelas = input("Masukkan Kelas siswa (a/b/c) : ")
    Ujian = input("Mengikuti Ujian (iya/tidak) : ")

    if Ujian == "tidak":
        print("Tidak mengikuti ujian")
        Nilai = 0
        Kategori = "Tidak mengikuti ujian"

        DataSiswa.append([NamaSiswa, Kelas, Ujian, Nilai, Kategori])
        continue

    elif Ujian == "iya":
        print("Mengikuti Ujian")

        soal = 20

        while True:
            SoalBenar = int(input("Masukkan Jumlah benar : "))
            SoalSalah = int(input("Masukkan Jumlah salah : "))

            if SoalBenar + SoalSalah == soal:
                Nilai = SoalBenar * 5
                print("Nilai : ", Nilai)
                break

            else:
                print("Soal hanya 20, silahkan periksa kembali")

        if Nilai >= 80 :
            Kategori = "Sangat Baik"
        elif Nilai >= 60 :
            Kategori = "baik"
        elif Nilai >= 40 :
            Kategori = "cukup"
        elif Nilai == 0 :
            Kategori = "Tidak mengikuti ujian"
        else:
            Kategori = "Perlu belajar lagi"
        print("Kategori : ", Kategori)
                
        DataSiswa.append([NamaSiswa, Kelas, Ujian, Nilai, Kategori])
        
        Lagi = input("Apakah anda masih ingin menginput data siswa yang lain ? (iya/tidak) : ")

        if Lagi == "tidak": 
            print("Lanjut menu berikutnya")
            break
        
print("===============================================================")
print("Data Akhir" .center(62))
print("===============================================================")


for kelas in ["a", "b", "c"]:
    print("\nKelas", kelas)
    for siswa in DataSiswa:
        if siswa[1] == kelas:
            print("Nama :", siswa[0])
            print("Mengikuti Ujian :", siswa[2])
            print("Nilai :", siswa[3])
            print("Kategori :", siswa[4])
            print(" ")
