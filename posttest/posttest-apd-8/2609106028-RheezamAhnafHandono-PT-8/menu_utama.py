from fungsi import bersihkan_layar
from login import login
from register import register
from menu_admin import menu_admin
from menu_penyewa import menu_penyewa

def menu_utama():
    print("---" * 10)
    print("Rental Kendaraan".center(30))
    print("---" * 10)
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    print()
    return input("Masukkan Pilihan : ")


def jalankan_program():
    while True:
        bersihkan_layar()
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


if __name__ == "__main__":
    jalankan_program()