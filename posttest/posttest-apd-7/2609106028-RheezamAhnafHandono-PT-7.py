import os

akun = { "rejam": { "password" : "rejam123", "role" : "admin"}
}

kendaraan = {
    1: {"Nama": "Bmw m4", "Jenis": "Mobil", "Harga": 4000, "Status": "Tersedia"},
    2: {"Nama": "Honda vario", "Jenis": "Motor", "Harga": 150, "Status": "Tersedia"},
    3: {"Nama": "Porsche 911", "Jenis": "Mobil", "Harga": 5000, "Status": "Tersedia"},
    4: {"Nama": "Yamaha R15", "Jenis": "Motor", "Harga": 200, "Status": "Tersedia"}
}

penyewaan = {}
id_penyewaan = 1

def ambil_daftar_kendaraan():
    return list(kendaraan.keys())

def menu_utama():
    print("===" * 10)
    print("Rental Kendaraan".center(30))
    print("===" * 10)
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    return input("Masukkan Pilihan : ")

def hitung_total(harga, lama_sewa):
    return harga * lama_sewa

def cari_kendaraan_rekursif(id_dicari, daftar_id, indeks=0):
    if indeks >= len(daftar_id):
        return None

    if daftar_id[indeks] == id_dicari:
        return daftar_id[indeks]

    return cari_kendaraan_rekursif(
        id_dicari, daftar_id, indeks + 1
    )

def tambah_kendaraan():
    nama = input("Input nama kendaraan : ")
    jenis = input("Jenis kendaraan (Motor/Mobil) : ")
    harga = input_angka("Harga kendaraan : ")

    if not nama or not jenis:
        print("Input tidak boleh kosong")
    elif jenis.lower() not in ("motor", "mobil"):
        print("Jenis harus mobil atau motor")
    elif harga is None:
        print("Ulangi input")
    elif harga <= 0:
        print("Harga tidak boleh 0 atau dibawahnya")
    else:
        id_baru = max(kendaraan.keys(), default=0) + 1
        kendaraan[id_baru] = {
            "Nama": nama,
            "Jenis": jenis.title(),
            "Harga": harga,
            "Status": "Tersedia"
        }
        print("Kendaraan berhasil ditambahkan dengan ID", id_baru)

def tampilkan_semua_penyewaan():

    if not penyewaan:
        print("Belum ada penyewaan")
        return

    for id_sewa, data_sewa, in penyewaan.items():
        print("-" * 10)
        print("ID sewa   :", id_sewa)
        print("Penyewa   :", data_sewa["Penyewa"])
        print("Kendaraan :", data_sewa["Kendaraan"])
        print("Lama sewa :", data_sewa["lama"], "hari")
        print("Total     : Rp", data_sewa["Total"])
        print("Status    :", data_sewa["Status"])

def tampilkan_kendaraan():
    daftar_id = ambil_daftar_kendaraan()

    if not daftar_id:
        print("Belum ada data kendaraan")
        return

    print("---" * 10)

    for id_kendaraan in daftar_id:
        data = kendaraan[id_kendaraan]
        print(
            "ID:", id_kendaraan,
            "|", data["Nama"],
            "|", data["Jenis"],
            "| Rp", data["Harga"],
            "/hari |", data["Status"]
        )

def input_angka(pesan):
    teks = input(pesan)

    try:
        angka = int(teks)

    except ValueError:
        print("Input harus berupa bilangan bulat.")
        hasil = None

    else:
        hasil = angka

    finally:
        pass

    return hasil


def register():
    username = input("Masukkan username : ")
    password = input("Masukkan password : ")

    if username == "" or password == "":
        print("Username atau password tidak boleh kosong")

    elif username in akun:
        print("Username telah digunakan")

    else:
        akun[username] = {
            "password": password,
            "role": "penyewa"
        }

        print("akun berhasil dibuat, mantap")

def login():
    username = input("masukkan username : ")
    password = input("masukkan password : ")

    if username in akun and akun[username]["password"] == password:
        print("Login berhasil. Selamat datang,", username)
        return username, akun[username]["role"]

    print("Username atau password salah.")
    return None, None

def menu_admin(username):
    global id_penyewaan

    while(True):
        os.system("cls")
        print("===" * 10)
        print("selamat datang,", username)
        print("role : Admin")

        print("1. Tambah kendaraan")
        print("2. Lihat kendaraan")
        print("3. Ubah status kendaraan")
        print("4. Hapus kendaraan")
        print("5. Lihat semua penyewaan")
        print("6. Logout")

        pilihan = input_angka("Pilih menu: ")

        if pilihan is None:
            print("Pilihan tidak ada di menu")
            input("Tekan enter untuk melanjutkan...")

        elif pilihan == 1:
            tambah_kendaraan()
            input("Tekan enter untuk melanjutkan...")

        elif pilihan == 2:
            tampilkan_kendaraan()
            input("Tekan enter untuk melanjutkan...")

        elif pilihan == 3:
            tampilkan_kendaraan()
            id_input = input_angka("Id kendaraan yang diubah : ")

            if id_input is None:
                pass

            elif id_input not in kendaraan:
                print("kendaraan tidak ditemukan")

            else:
                status_pilihan = input_angka(
                    "1. Tersedia | 2. Disewa : "
                )

                if status_pilihan == 1:
                    kendaraan[id_input]["Status"] = "Tersedia"
                    print("Status diubah menjadi tersedia")

                elif status_pilihan == 2:
                    sedang_aktif = any(
                        sewa["id_kendaraan"] == id_input
                        and sewa["Status"] == "Aktif"
                        for sewa in penyewaan.values()
                    )

                    if sedang_aktif:
                        print("Kendaraan sudah memiliki penyewaan aktif.")

                    else:
                        kendaraan[id_input]["Status"] = "Disewa"
                        print("Status diubah menjadi Disewa.")

                elif status_pilihan is not None:
                    print("Pilihan status tidak valid.")

            input("Tekan Enter untuk lanjut...")

        elif pilihan == 4:
            tampilkan_kendaraan()
            id_input = input_angka("Id kendaraan yang dihapus : ")

            if id_input is None:
                pass

            elif id_input not in kendaraan:
                print("Kendaraan tidak ditemukan")

            else:
                sedang_aktif = any(
                    sewa["id_kendaraan"] == id_input
                    and sewa["Status"] == "Aktif"
                    for sewa in penyewaan.values()
                )

                if sedang_aktif:
                    print("Kendaraan sedang disewa dan tidak dapat dihapus")

                else:
                    del kendaraan[id_input]
                    print("Kendaraan berhasil dihapus")

            input("Tekan enter untuk melanjutkan...")

        elif pilihan == 5:
            tampilkan_semua_penyewaan()
            input("Tekan enter untuk melanjutkan...")

        elif pilihan == 6:
            break

        else:
            print("Pilihan tidak tersedia")
            input("Tekan enter untuk melanjutkan...")

def menu_penyewa(username):
    global id_penyewaan

    while True:
        os.system("cls")

        print("=== Menu Pengguna ===")
        print("Login sebagai: ", username)
        print("1. Lihat Kendaraan")
        print("2. Sewa Kendaraan")
        print("3. Lihat Penyewaan Saya")
        print("4. Ubah Lama Sewa")
        print("5. Batalkan Penyewaan")
        print("6. Logout")

        pilihan = input_angka("Pilih Menu : ")

        if pilihan is None:
            input("Tekan enter untuk melanjutkan...")

        elif pilihan == 1:
            tampilkan_kendaraan()
            input("Tekan enter untuk melanjutkan...")

        elif pilihan == 2:
            tampilkan_kendaraan()
            id_input = input_angka("Id kendaraan yang ingin disewa : ")

            if id_input is None:
                input("Tekan enter untuk melanjutkan...")
                continue

            id_ditemukan = cari_kendaraan_rekursif(
            id_input, ambil_daftar_kendaraan()
            )

            if id_ditemukan is None:
                print("Kendaraan tidak ditemukan")

            elif kendaraan[id_ditemukan]["Status"] != "Tersedia":
                print("Kendaraan tidak tersedia")

            else:
                lama = input_angka("Lama sewa (Hari) : ")

                if lama is None:
                    print("Input tidak valid, silahkan input ulang")

                elif lama <= 0:
                    print("Lama sewa minimal 1 hari")

                else:
                    data_kendaraan = kendaraan[id_ditemukan]
                    total = hitung_total(
                        data_kendaraan["Harga"], lama
                    )

                    penyewaan[id_penyewaan] = {
                        "Penyewa": username,
                        "id_kendaraan": id_ditemukan,
                        "Kendaraan": data_kendaraan["Nama"],
                        "lama": lama,
                        "Total": total,
                        "Status": "Aktif"
                    }

                    data_kendaraan["Status"] = "Disewa"

                    print("Penyewaan berhasil.")
                    print("Total biaya: Rp", total)

                    id_penyewaan += 1

            input("Tekan Enter untuk lanjut...")

        elif pilihan == 3:
            ada = False

            for id_sewa, data_sewa in penyewaan.items():
                if data_sewa["Penyewa"] == username:
                    ada = True

                    print("---" * 10)
                    print("Id sewa   :", id_sewa)
                    print("Kendaraan :", data_sewa["Kendaraan"])
                    print("Lama sewa :", data_sewa["lama"], "hari")
                    print("Total     : Rp", data_sewa["Total"])
                    print("Status    :", data_sewa["Status"])

            if not ada:
                print("Kamu belum memiliki penyewaan")

            input("Tekan enter untuk melanjutkan...")

        elif pilihan == 4:
            ada_aktif = False

            for id_sewa, data_sewa in penyewaan.items():
                if(
                    data_sewa["Penyewa"] == username
                    and data_sewa["Status"] == "Aktif"
                ):

                    ada_aktif = True

                    print(
                        "Id :", id_sewa, "|", data_sewa["Kendaraan"], "|", data_sewa["lama"], "Hari"

                    )

            if not ada_aktif:
                print("Kamu tidak memiliki penyewaan aktif")

            else:
                id_sewa_input = input_angka(
                    "Id penyewaan yg pengen diubah: "
                )

                if id_sewa_input is not None:
                    data_sewa = penyewaan.get(id_sewa_input)

                    if(
                        data_sewa is None
                        or data_sewa["Penyewa"] != username
                        or data_sewa["Status"] != "Aktif"
                    ):

                        print("Penyewaan tidak benar atau bukan milikmu")

                    else:
                        lama_baru = input_angka(
                            "Lama sewa baru (Hari): "
                        )

                        if lama_baru is None:
                            print("Lama sewa tidak valid")

                        elif lama_baru <= 0:
                            print("Lama sewa baru minimal 1 hari")

                        else:
                            data_kendaraan = kendaraan.get(data_sewa["id_kendaraan"])

                            if data_kendaraan is None:
                                print("data tidak ditemukan")

                            else:
                                data_sewa["lama"] = lama_baru
                                data_sewa["Total"] = hitung_total(
                                    data_kendaraan["Harga"], lama_baru
                                )

                                print("Penyewaan berhasil diperbarui.")
                                print("Total baru: Rp", data_sewa["Total"])

            input("Tekan Enter untuk lanjut...")

        elif pilihan == 5:
            daftar_aktif = []

            for id_sewa, data_sewa in penyewaan.items():
                if (
                    data_sewa["Penyewa"] == username and data_sewa["Status"] == "Aktif"
                ):

                    daftar_aktif.append(id_sewa)
                    print ("Id: ", id_sewa, "|", data_sewa["Kendaraan"])

            if not daftar_aktif:
                print("Kamu tidak memiliki penyewaan aktif")

            else:
                id_sewa_input = input_angka(
                    "ID penyewaan yang dibatalkan: "
                )

                if id_sewa_input is not None:
                    data_sewa = penyewaan.get(id_sewa_input)

                    if (
                        data_sewa is None
                        or data_sewa["Penyewa"] != username
                        or data_sewa["Status"] != "Aktif"
                    ):
                        print(
                            "Penyewaan tidak ditemukan atau bukan milikmu."
                        )

                    else:
                        data_sewa["Status"] = "Dibatalkan"
                        id_kendaraan_sewa = data_sewa["id_kendaraan"]

                        if id_kendaraan_sewa in kendaraan:
                            kendaraan[id_kendaraan_sewa]["Status"] = "Tersedia"

                        print("Penyewaan berhasil dibatalkan.")

            input("Tekan Enter untuk lanjut...")

        elif pilihan == 6:
            break

        else:
            print("Pilihan tidak tersedia.")
            input("Tekan Enter untuk lanjut...")

while True:
    os.system("cls")
    pilihan = menu_utama()

    if pilihan == "1":
        username, role = login()

        if role == "admin":
            menu_admin(username)

        elif role == "penyewa":
            menu_penyewa(username)

        input("Tekan Enter untuk kembali ke menu awal...")

    elif pilihan == "2":
        register()
        input("Tekan Enter untuk kembali ke menu awal...")

    elif pilihan == "3":
        print("Terima kasih telah menggunakan layanan Rental Kendaraan.")
        break

    else:
        print("Pilihan tidak tersedia.")
        input("Tekan Enter untuk mencoba lagi...")