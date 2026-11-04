from data import akun

def register():
    username = input("masukkan username : ")
    password = input("masukkan password : ")

    if username in akun:
        print("Username sudah digunakan.")
        return

    akun[username] = {"password": password, "role": "penyewa"}
    print("Register berhasil. Silakan login.")
