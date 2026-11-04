from data import kendaraan, penyewaan
from fungsi import (
    bersihkan_layar,
    input_angka,
    tampilkan_kendaraan,
    tampilkan_semua_penyewaan,
)

def tambah_kendaraan():
    nama = input("Masukkan nama kendaraan: ")
    jenis = input("Masukkan jenis kendaraan (Motor/Mobil): ")
    harga = input_angka("Masukkan harga: ")

    if not nama or not jenis:
        print("input tidak boleh kosong")
    elif jenis.lower() not in ["motor", "mobil"]:
        print("Jenis kendaraan harus 'Motor' atau 'Mobil'.")
    elif harga is None:
        print("Harga harus berupa angka.")
    else:
        id_baru = max(kendaraan.keys(), default=0) + 1
        kendaraan[id_baru] = {
            "Nama": nama,
            "Jenis": jenis.title(),
            "Harga": harga,
            "Status": "Tersedia"
        }
        print("Kendaraan berhasil ditambahkan dengan ID", id_baru)

def menu_admin(username):
    while True:
        bersihkan_layar()
        print("=== Menu Admin ===")
        print("Login sebagai: ", username)
        print("Role: admin")
        print("=====================")

        print("1. Tambah Kendaraan")
        print("2. Lihat kendaraan")
        print("3. Ubah status penyewaan")
        print("4. Hapus Kendaraan")
        print("5. Lihat semua penyewaan")
        print("6. Logout")
        print()
        pilihan = input_angka("Masukkan Pilihan : ")

        if pilihan is None:
            print("Pilihan tidak ada di menu")
            input("Tekan Enter untuk melanjutkan...")

        elif pilihan == 1:
            tambah_kendaraan()
            input("Tekan Enter untuk melanjutkan...")

        elif pilihan == 2:
            tampilkan_kendaraan()
            input("Tekan Enter untuk melanjutkan...")

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
            print("Pilihan tidak ada di menu")
            input("Tekan Enter untuk melanjutkan...")