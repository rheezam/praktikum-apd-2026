import os

akun = { "rejam": { "password" : "rejam123", "role" : "admin"}
}

kendaraan = {
    1: {"Nama" : "Bmw m4", "Jenis" : "Mobil", "Harga" : 4000, "Status" : "Tersedia"},
    2: {"Nama" : "Honda vario", "Jenis" : "Motor", "Harga" : 150, "Status" : "Tersedia"},
    3: {"Nama" : "Porsche 911", "Jenis" : "Mobil", "Harga" : 5000, "Status" : "Tersedia"},
    4: {"Nama" : "Yamaha R15", "Jenis" : "Motor", "Harga" : 200, "Status" : "Tersedia"}
}

penyewaan = {}

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
                if username in akun:
                    print("Username sudah digunakan")
                else:
                    akun[username] = {"password" : password, "role" : "penyewa"}
                    print("Akun berhasil dibuat!")

            input("Tekan Enter untuk melanjutkan...")

    elif pilihan == 1:
        os.system("cls")
        print("======== Login ========")

        username = input("Masukkan Username : ")
        password = input("Masukkan Password : ")

        Role = ""

        if username in akun and akun[username]["password"] == password:
            Role = akun[username]["role"]

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
                            kendaraan[id_kendaraan] = {
                                "Nama" : nama,
                                "Jenis" : jenis.title(),
                                "Harga" : int(harga),
                                "Status" : "Tersedia"
                            }

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
                            for id_kendaraan, Data in kendaraan.items():
                                print("-----" * 10)
                                print("ID Kendaraan : ", id_kendaraan)
                                print("Nama Kendaraan : ", Data["Nama"])
                                print("Jenis : ", Data["Jenis"])
                                print("Harga : Rp", Data["Harga"])
                                print("Status : ", Data["Status"])
                                print()

                        input ("Tekan Enter untuk melanjutkan...")


#update
                    elif Menu == 3:
                        os.system("cls")
                        print("======== Ubah Status kendaraan ========")

                        for id_kendaraan, data in kendaraan.items():
                            print(id_kendaraan, "-", data["Nama"], "| Status :", data["Status"])

                        id_update = input("\ninput id kendaraan : ")

                        if not id_update.isdigit():
                            print("ID harus berupa angka!")

                        elif int(id_update) not in kendaraan:
                            print("kendaraan tidak ditemukan")

                        else:
                            data = kendaraan[int(id_update)]

                            print("\nnama kendaraan : ", data["Nama"])
                            print("\njenis kendaraan : ", data["Jenis"])
                            print("\nstatus saat ini : ", data["Status"])
                            print("1. Tersedia")
                            print("2. Disewa")
                            print()

                            status_baru = int(input("pilih status baru : "))

                            if status_baru == 1:
                                data["Status"] = "Tersedia"
                                print("Status berhasil diubah ke Tersedia")

                            elif status_baru == 2:
                                data["Status"] = "Disewa"
                                print("Status berhasil diubah ke Disewa")

                            else:
                                print("Pilihan tidak valid")

                        input("\ntekan enter untuk melanjutkan...")

#delete
                    elif Menu == 4:
                        os.system("cls")
                        print("======== Hapus kendaraan ========")

                        for id_kendaraan, data in kendaraan.items():
                            print(id_kendaraan, "-", data["Nama"])

                        id_hapus = input("\nmasukkan id kendaraan : ")
                        if not id_hapus.isdigit():

                            print("ID harus berupa angka!")

                        else:
                            id_hapus = int(id_hapus)
                            ditemukan = id_hapus in kendaraan
                            sedangDisewa = False

                    

                            if not ditemukan:
                                print("Kendaraan tidak ditemukan")

                            elif sedangDisewa:
                                print("Kendaraan sedang disewa")

                            else:
                                del kendaraan[id_hapus]
                                print("Kendaraan berhasil dihapus")

                        input("Tekan enter untuk melanjutkan...")

                    elif Menu == 5:
                        os.system("cls")
                        print("===== Data semua penyewaan =====")

                        if len(penyewaan) == 0:
                            print("Belum ada penyewaan")

                        else:
                            for id_sewa, sewa in penyewaan.items():
                                print("---" * 10)
                                print("ID sewa   : ", id_sewa)
                                print("Penyewa   : ", sewa["Penyewa"])
                                print("Kendaraan : ", sewa["Kendaraan"])
                                print("Lama Sewa : ", sewa["lama"], "Hari")
                                print("Total     : Rp", sewa["Total"])
                                print("Status    : ", sewa["Status"])

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
                            for id_kendaraan, Data in kendaraan.items():
                                print("---" * 10)
                                print("Id     : ", id_kendaraan)
                                print("Nama   : ", Data["Nama"])
                                print("Jenis  : ", Data["Jenis"])
                                print("Harga  : Rp", Data["Harga"])
                                print("Status : ", Data["Status"])

                        input("\nTekan enter untuk melanjutkan...")

                    elif Menu == "2":
                        os.system("cls")
                        print("===== Sewa kendaraan =====")

                        for id_kendaraan, Data in kendaraan.items():
                            print(id_kendaraan, "-", Data["Nama"], "| Rp", Data["Harga"], "/Hari", "|", Data["Status"])

                        Id = input("\nPilih Id kendaraan : ")

                        if not Id.isdigit():
                            print("Id harus berupa angka")

                        else:
                            PilihanKendaraan = kendaraan.get(int(Id))

                            if PilihanKendaraan is None:
                                print("Kendaraan tidak ditemukan")

                            elif PilihanKendaraan["Status"] != "Tersedia":
                                print("Kendaraan tidak tersedia")

                            else:
                                Lama = input("Lama sewa (hari) : ")

                                if not Lama.isdigit():
                                    print("Lama sewa harus berupa angka")

                                elif int(Lama) <= 0:
                                    print("Lama sewa minimal 1 hari")

                                else:
                                    Total = PilihanKendaraan["Harga"] * int(Lama)

                                    penyewaan[id_penyewaan] = {
                                        "Penyewa" : username,
                                        "id_kendaraan" : int(Id),
                                        "Kendaraan" : PilihanKendaraan["Nama"],
                                        "lama" : int(Lama),
                                        "Total" : Total,
                                        "Status" : "Aktif"
                                    }

                                    id_penyewaan += 1
                                    PilihanKendaraan["Status"] = "Disewa"

                                    print("Penyewaan berhasil!")
                                    print("Total harga: Rp", Total)

                        input("\nTekan Enter untuk lanjut.")

                    elif Menu == "3":
                        os.system("cls")
                        print("===== Penyewaan saya =====")

                        Adasewa = False

                        for id_sewa, sewa in penyewaan.items():
                            if sewa["Penyewa"] == username:
                                Adasewa = True
                                print("---" * 10)
                                print("Id sewa   : ", id_sewa)
                                print("Kendaraan : ", sewa["Kendaraan"])
                                print("Lama sewa : ", sewa["lama"], "Hari")
                                print("Total     : Rp", sewa["Total"])
                                print("Status    : ", sewa["Status"])

                        if not Adasewa:
                            print("Kamu belum memiliki penyewaan")

                        input("\nTekan enter untuk melanjutkan...")


                    elif Menu == "4":
                        os.system("cls")
                        print("===== Ubah lama sewa =====")

                        Adasewa = False

                        for id_sewa, sewa in penyewaan.items():
                            if sewa["Penyewa"] == username and sewa["Status"] == "Aktif":
                                Adasewa = True
                                print("Id :", id_sewa, "|", sewa["Kendaraan"], "|", sewa["lama"], "Hari")

                        if not Adasewa:
                            print("Kamu belum memiliki penyewaan aktif")

                        else:
                            Id = input("\nMasukkan id sewa : ")

                            if not Id.isdigit():
                                print("Id harus berupa angka")

                            else:
                                sewa = penyewaan.get(int(Id))
                                
                                if sewa is None or sewa["Penyewa"] != username or sewa["Status"] != "Aktif":
                                    print("Penyewaan tidak ditemukan")

                                else: 
                                    LamaBaru = input("Lama sewa baru (hari) : ")

                                    if not LamaBaru.isdigit():
                                        print("Lama sewa harus berupa angka")

                                    elif int(LamaBaru) <= 0:
                                        print("Lama sewa minimal 1 hari")

                                    else:
                                        mobil = kendaraan.get(sewa["id_kendaraan"])
                                        if mobil is not None:
                                            sewa["lama"] = int(LamaBaru)
                                            sewa["Total"] = mobil["Harga"] * int(LamaBaru)
                                            print("Penyewaan berhasil diperbarui")
                                            print("Total baru: Rp", sewa["Total"])
                                    
                        input("\nTekan enter untuk melanjutkan...")

                    elif Menu == "5":
                        os.system("cls")
                        print("===== Batalkan Penyewaan =====")

                        Adasewa = False

                        for id_sewa, sewa in penyewaan.items():
                            if sewa["Penyewa"] == username and sewa["Status"] == "Aktif":
                                Adasewa = True
                                print("Id :", id_sewa, "-", sewa["Kendaraan"])

                        if not Adasewa:
                            print("Kamu belum memiliki penyewaan aktif")

                        else:
                            Id = input("\nMasukkan id sewa : ")

                            if not Id.isdigit():
                                print("Id harus berupa angka")

                            else:
                                sewa = penyewaan.get(int(Id))

                                if sewa is None or sewa["Penyewa"] != username or sewa["Status"] != "Aktif":
                                    print("Penyewaan tidak ditemukan")

                                else:
                                    sewa["Status"] = "Dibatalkan"
                        
                                    if sewa["id_kendaraan"] in kendaraan:
                                        kendaraan[sewa["id_kendaraan"]]["Status"] = "Tersedia"

                                    print("Penyewaan berhasil dibatalkan")

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


                        



                            


