from data import akun

def login():
    username = input("masukkan username : ")
    password = input("masukkan password : ")

    if username in akun and akun[username]["password"] == password:
        print("Login berhasil. Selamat datang,", username)
        return username, akun[username]["role"]

    print("Username atau password salah.")
    return None, None