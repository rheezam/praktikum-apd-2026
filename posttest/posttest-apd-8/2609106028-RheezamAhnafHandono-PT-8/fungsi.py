import os
from prettytable import PrettyTable
from data import kendaraan, penyewaan

def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")


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


def hitung_total(harga, lama_sewa):
    return harga * lama_sewa


def ambil_daftar_kendaraan():
    return list(kendaraan.keys())


def cari_kendaraan_rekursif(id_dicari, daftar_id, indeks=0):
    if indeks >= len(daftar_id):
        return None

    if daftar_id[indeks] == id_dicari:
        return daftar_id[indeks]

    return cari_kendaraan_rekursif(
        id_dicari, daftar_id, indeks + 1
    )


def tampilkan_kendaraan():
    daftar_id = ambil_daftar_kendaraan()

    if not daftar_id:
        print("Belum ada data kendaraan")
        return

    tabel = PrettyTable()
    tabel.field_names = ["ID", "Nama", "Jenis", "Harga / Hari", "Status"]
    tabel.align["Nama"] = "l"
    tabel.align["Harga / Hari"] = "r"

    for id_kendaraan in daftar_id:
        data = kendaraan[id_kendaraan]
        tabel.add_row([
            id_kendaraan,
            data["Nama"],
            data["Jenis"],
            "Rp " + str(data["Harga"]),
            data["Status"]
        ])

    print(tabel)


def tampilkan_semua_penyewaan():
    if not penyewaan:
        print("Belum ada penyewaan")
        return

    tabel = PrettyTable()
    tabel.field_names = [
        "ID Sewa", "Penyewa", "Kendaraan", "Tanggal Sewa",
        "Lama (Hari)", "Total", "Status"
    ]
    tabel.align["Penyewa"] = "l"
    tabel.align["Kendaraan"] = "l"
    tabel.align["Total"] = "r"

    for id_sewa, data_sewa in penyewaan.items():
        tabel.add_row([
            id_sewa,
            data_sewa["Penyewa"],
            data_sewa["Kendaraan"],
            data_sewa["Tanggal"],
            data_sewa["lama"],
            "Rp " + str(data_sewa["Total"]),
            data_sewa["Status"]
        ])

    print(tabel)


def tampilkan_penyewaan_user(username, hanya_aktif=False):
    """Menampilkan tabel penyewaan milik satu user.
    Mengembalikan daftar id penyewaan yang ditampilkan (kosong jika tidak ada)."""
    daftar_id = []

    tabel = PrettyTable()
    tabel.field_names = [
        "ID Sewa", "Kendaraan", "Tanggal Sewa",
        "Lama (Hari)", "Total", "Status"
    ]
    tabel.align["Kendaraan"] = "l"
    tabel.align["Total"] = "r"

    for id_sewa, data_sewa in penyewaan.items():
        if data_sewa["Penyewa"] != username:
            continue

        if hanya_aktif and data_sewa["Status"] != "Aktif":
            continue

        daftar_id.append(id_sewa)
        tabel.add_row([
            id_sewa,
            data_sewa["Kendaraan"],
            data_sewa["Tanggal"],
            data_sewa["lama"],
            "Rp " + str(data_sewa["Total"]),
            data_sewa["Status"]
        ])

    if daftar_id:
        print(tabel)

    return daftar_id