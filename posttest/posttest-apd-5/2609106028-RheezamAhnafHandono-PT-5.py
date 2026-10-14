import os

akun = [["rejam", "rejam123", "admin"]]

kendaraan = [
    [1, "Bmw m4", "Mobil", 4000, "Tersedia"],
    [2, "Honda vario", "Motor", 150, "Tersedia"],
    [3, "Porsche 911", "Mobil", 5000, "Tersedia"],
    [4, "Yamaha R15", "Motor", 200, "Tersedia"]
]

penyewaan = []

id_penyewaan = 1
id_kendaraan = 5

while True:
    os.system("cls")

    print("===" * 10)
    print("Rental Kendaraan".center(30))
    print("===" * 10)
    print("1. Login")
    print("2. Register")
    print("3. Exit")

    pilihan = int(input("\nMasukkan Pilihan Anda : "))

    if pilihan == 2:
            os.system("cls")
            print("===" * 10)
            print("Register".center(30))
            print("===" * 10)

            username = input("Masukkan Username : ")
            password = input("Masukkan Password : ")

            if username == "" or password == "":
                print("Username atau Password tidak boleh kosong!")
                input("Tekan Enter untuk melanjutkan...")
                continue

            else: 
                sudahAda = False
                for Data in akun:
                    if Data[0] == username:
                        sudahAda = True

                if sudahAda:
                    print("Username sudah dipakai!")
                else:
                    akun.append([username, password, "user"])
                    print("Akun berhasil dibuat!")

            input("Tekan Enter untuk melanjutkan...")

    elif pilihan == 1:
        os.system("cls")
        print("======== Login ========")

        username = input("Masukkan Username : ")
        password = input("Masukkan Password : ")

        Role = ""

        for Data in akun:
            if username == Data[0] and Data[1] == password:
                Role = Data[2]

        if Role == "":
            print("Username atau Password salah!")
            input("Tekan Enter untuk melanjutkan...")

        else: 
            masuk = True

            while masuk:
                os.system("cls")
                print("===" * 10)
                print("selamat datang,", username)
                print("role : ", Role)

                if Role == "admin":
                    print("1. Tambah kendaraan")
                    print("2. Lihat kendaraan")
                    print("3. Ubah Status Kendaraan")
                    print("4. Hapus Kendaraan")
                    print("5. Data penyewaan")
                    print("6. Logout")
                    
                    Menu = int(input("\nMasukkan Pilihan Anda : "))

#create
                    if Menu == 1:
                        os.system("cls")
                        print("======== Tambah kendaraan ========")

                        nama = input("Masukkan Nama Kendaraan : ")
                        jenis = input("Jenis (Mobil/Motor) : ")
                        harga = int(input("Masukkan Harga sewa Kendaraan : "))

                        if nama == "" or jenis == "" or harga == "":
                            print("Data tidak boleh kosong!")

                        elif int(harga) <= 0:
                            print("Harga harus lebih dari 0!")

                        elif jenis.lower() != "mobil" and jenis.lower() != "motor":
                            print("Jenis kendaraan harus Mobil atau Motor!")

                        else:
                            kendaraan.append([
                                id_kendaraan,
                                nama,
                                jenis.title(),
                                int(harga),
                                "Tersedia"
                            ])

                        id_kendaraan += 1
                        print("Kendaraan berhasil ditambahkan!")

                        input("Tekan Enter untuk melanjutkan...")


#read
                    elif Menu == 2:
                        os.system("cls")
                        print("======== Daftar kendaraan ========")

                        if len(kendaraan) == 0:
                            print("Belum ada kendaraan yang tersedia!")

                        else:
                            for Data in kendaraan:
                                print("-----" * 10)
                                print("ID Kendaraan : ", Data[0])
                                print("Nama Kendaraan : ", Data[1])
                                print("Jenis : ", Data[2])
                                print("Harga : Rp", Data[3])
                                print("Status : ", Data[4])
                                print()

                        input ("Tekan Enter untuk melanjutkan...")


#update
                    elif Menu == 3:
                        os.system("cls")
                        print("======== Ubah Status kendaraan ========")

                        for data in kendaraan:
                            print(data[0], "-", data[1], "| Status :", data[4])

                        id_update = input("\ninput id kendaraan : ")

                        if not id_update.isdigit():
                            print("ID harus berupa angka!")

                        else:
                            ditemukan = False


                        for data in kendaraan:
                            if data[0] == int(id_update):
                                ditemukan = True

                                print("\nnama kendaraan : ", data[1])
                                print("\njenis kendaraan : ", data[2])
                                print("\nstatus saat ini : ", data[4])
                                print("1. Tersedia")
                                print("2. Disewa")
                                print()

                                status_baru = int(input("pilih status baru : "))

                                if status_baru == 1:
                                    data[4] = "Tersedia"
                                    print("Status berhasil diubah ke Tersedia")

                                elif status_baru == 2:
                                    data[4] = "Disewa"
                                    print("Status berhasil diubah ke Disewa")

                                else:
                                    print("Pilihan tidak valid")

                        input("\ntekan enter untuk melanjutkan...")

#delete
                    elif Menu == 4:
                        os.system("cls")
                        print("======== Hapus kendaraan ========")

                        for data in kendaraan:
                            print(data[0], "-", data[1])

                        id_hapus = input("\nmasukkan id kendaraan : ")

                        if not id_hapus.isdigit():
                            print("ID harus berupa angka!")

                        else:
                            id_hapus = int(id_hapus)
                            ditemukan = False
                            sedangDisewa = False

                            for data in kendaraan:
                                if data[0] == id_hapus:
                                    ditemukan = True

                            for data in penyewaan:
                                if data[2] == id_hapus and data[6] == "Aktif":
                                    sedangDisewa = True

                            if not ditemukan:
                                print("Kendaraan tidak ditemukan")

                            elif sedangDisewa:
                                print("Kendaraan sedang disewa")

                            else:
                                for data in kendaraan:
                                    if data[0] == id_hapus:
                                        kendaraan.remove(data)
                                        print("Kendaraan berhasil dihapus")
                                        break

                        input("Tekan enter untuk melanjutkan...")

                    elif Menu == 5:
                        os.system("cls")
                        print("===== Data semua penyewaan =====")

                        if len(penyewaan) == 0:
                            print("Belum ada penyewaan")

                        else:
                            for Data in penyewaan:
                                print("---" * 10)
                                print("ID sewa   : ", Data[0])
                                print("Penyewa   : ", Data[1])
                                print("Kendaraan : ", Data[3])
                                print("Lama Sewa : ", Data[4], "Hari")
                                print("Total     : Rp", Data[5])
                                print("Status    : ", Data[6])

                        input("\nTekan Enter untuk melanjutkan...")

                    elif Menu == 6:
                        masuk = False

                    else:
                        print("Menu tidak tersedia.")
                        input("\nTekan Enter untuk lanjut.")

                else: 
                    print("1. Lihat kendaraan")
                    print("2. Sewa kendaraan")
                    print("3. Lihat penyewaan saya")
                    print("4. Ubah Lama sewa")
                    print("5. Batalkan penyewaan")
                    print("6. Logout")
                    print()

                    Menu = input("Pilih Menu : ")

                    if Menu == "1":
                        os.system("cls")
                        print("===== Daftar kendaraan =====")

                        if len(kendaraan) == 0:
                            print("Tidak ada kendaraan")

                        else:
                            for Data in kendaraan:
                                print("---" * 10)
                                print("Id     : ", Data[0])
                                print("Nama   : ", Data[1])
                                print("Jenis  : ", Data[2])
                                print("Harga  : Rp", Data[3])
                                print("Status : ", Data[4])

                        input("\nTekan enter untuk melanjutkan...")

                    elif Menu == "2":
                        os.system("cls")
                        print("===== Sewa kendaraan =====")

                        for Data in kendaraan:
                            print(Data[0], "-", Data[1], "| Rp", Data[3], "/Hari", "|", Data[4])

                        Id = input("\nPilih Id kendaraan : ")

                        if not Id.isdigit():
                            print("Id harus berupa angka")

                        else:
                            PilihanKendaraan = None

                            for Data in kendaraan:
                                if Data[0] == int(Id):
                                    PilihanKendaraan = Data

                            if PilihanKendaraan is None:
                                print("Kendaraan tidak ditemukan")

                            elif PilihanKendaraan[4] != "Tersedia":
                                print("Kendaraan tidak tersedia")

                            else:
                                Lama = input("Lama sewa (hari) : ")

                                if not Lama.isdigit():
                                    print("Lama sewa harus berupa angka")

                                elif int(Lama) <= 0:
                                    print("Lama sewa minimal 1 hari")

                                else:
                                    Total = PilihanKendaraan[3] * int(Lama)

                                    penyewaan.append([
                                        id_penyewaan,
                                        username,
                                        PilihanKendaraan[0],
                                        PilihanKendaraan[1],
                                        int(Lama),
                                        Total,
                                        "Aktif"
                                    ])

                                    id_penyewaan += 1
                                    PilihanKendaraan[4] = "Disewa"

                                    print("Penyewaan berhasil!")
                                    print("Total harga: Rp", Total)

                        input("\nTekan Enter untuk lanjut.")

                    elif Menu == "3":
                        os.system("cls")
                        print("===== Penyewaan saya =====")

                        Adasewa = False

                        for Data in penyewaan:
                            if Data[1] == username:
                                Adasewa = True
                                print("---" * 10)
                                print("Id sewa   : ", Data[0])
                                print("Kendaraan : ", Data[3])
                                print("Lama sewa : ", Data[4], "Hari")
                                print("Total     : Rp", Data[5])
                                print("Status    : ", Data[6])

                        if not Adasewa:
                            print("Kamu belum memiliki penyewaan")

                        input("\nTekan enter untuk melanjutkan...")


                    elif Menu == "4":
                        os.system("cls")
                        print("===== Ubah lama sewa =====")

                        Adasewa = False

                        for Data in penyewaan:
                            if Data[1] == username and Data[6] == "Aktif":
                                Adasewa = True
                                print("Id :", Data[0], "|", Data[3], "|", Data[4], "Hari")

                        if not Adasewa:
                            print("Kamu belum memiliki penyewaan aktif")

                        else:
                            Id = input("\nMasukkan id sewa : ")

                            if not Id.isdigit():
                                print("Id harus berupa angka")

                            else:
                                ditemukan = False

                                for Data in penyewaan:
                                    if Data[0] == int(Id) and Data[1] == username and Data[6] == "Aktif":
                                        ditemukan = True
                                        LamaBaru = input("Lama sewa baru (hari) : ")

                                        if not LamaBaru.isdigit():
                                            print("Lama sewa harus berupa angka")

                                        elif int(LamaBaru) <= 0:
                                            print("Lama sewa minimal 1 hari")

                                        else:
                                            for Mobil in kendaraan:
                                                if Mobil[0] == Data[2]:
                                                    Data[4] = int(LamaBaru)
                                                    Data[5] = Mobil[3] * int(LamaBaru)
                                                    print("Penyewaan berhasil diperbarui")
                                                    print("Total baru: Rp", Data[5])
                                        break

                                if not ditemukan:
                                    print("Penyewaan tidak ditemukan")

                        input("\nTekan enter untuk melanjutkan...")

                    elif Menu == "5":
                        os.system("cls")
                        print("===== Batalkan Penyewaan =====")

                        Adasewa = False

                        for Data in penyewaan:
                            if Data[1] == username and Data[6] == "Aktif":
                                Adasewa = True
                                print("Id :", Data[0], "-", Data[3])

                        if not Adasewa:
                            print("Kamu belum memiliki penyewaan aktif")

                        else:
                            Id = input("\nMasukkan id sewa : ")

                            if not Id.isdigit():
                                print("Id harus berupa angka")

                            else:
                                ditemukan = False

                                for Data in penyewaan:
                                    if Data[0] == int(Id) and Data[1] == username and Data[6] == "Aktif":
                                        ditemukan = True
                                        Data[6] = "Dibatalkan"

                                        for Mobil in kendaraan:
                                            if Mobil[0] == Data[2]:
                                                Mobil[4] = "Tersedia"

                                        print("Penyewaan berhasil dibatalkan")
                                        break

                                if not ditemukan:
                                    print("Penyewaan tidak ditemukan")

                        input("\nTekan enter untuk melanjutkan...")

                    elif Menu == "6":          
                        masuk = False


    elif pilihan == 3:
        os.system("cls")
        print("Terimakasih telah menggunakan layanan rental kami")
        break


    else:
        print("Pilihan tidak ada di menu")
        input("tekan enter untuk kembali")         


                        



                            


