# Meminta input total belanja dari pengguna
total_belanja = float(input("Masukkan total belanja: "))

# Cek apakah total belanja 100k ke atas
if total_belanja >= 100000:
    print("Anda mendapatkan diskon!")
else:
    print("Anda belum mendapatkan diskon.")