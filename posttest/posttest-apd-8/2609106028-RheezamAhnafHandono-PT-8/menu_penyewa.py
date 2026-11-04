from datetime import datetime
import data
from data import kendaraan, penyewaan
from fungsi import (
    bersihkan_layar,
    input_angka,
    hitung_total,
    ambil_daftar_kendaraan,
    cari_kendaraan_rekursif,
    tampilkan_kendaraan,
    tampilkan_penyewaan_user,
)

def menu_penyewa(username):
    while True:
        bersihkan_layar()

        print("=== Menu Pengguna ===")
        print("Login sebagai: ", username)
        print("Role: penyewa")
        print("=====================")
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

                    penyewaan[data.id_penyewaan] = {
                        "Penyewa": username,
                        "id_kendaraan": id_ditemukan,
                        "Kendaraan": data_kendaraan["Nama"],
                        "Tanggal": datetime.now().strftime("%d-%m-%Y %H:%M"),
                        "lama": lama,
                        "Total": total,
                        "Status": "Aktif"
                    }

                    data_kendaraan["Status"] = "Disewa"

                    print("Penyewaan berhasil.")
                    print("Total biaya: Rp", total)

                    data.id_penyewaan += 1

            input("Tekan Enter untuk lanjut...")

        elif pilihan == 3:
            ada = tampilkan_penyewaan_user(username)

            if not ada:
                print("Kamu belum memiliki penyewaan")

            input("Tekan enter untuk melanjutkan...")

        elif pilihan == 4:
            ada_aktif = tampilkan_penyewaan_user(username, True)

            if not ada_aktif:
                print("Kamu tidak memiliki penyewaan aktif")

            else:
                id_sewa_input = input_angka(
                    "Id penyewaan yg pengen diubah: "
                )

                if id_sewa_input is not None:
                    data_sewa = penyewaan.get(id_sewa_input)

                    if (
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
            daftar_aktif = tampilkan_penyewaan_user(username, True)

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
                        print("Penyewaan tidak ditemukan atau bukan milikmu.")

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