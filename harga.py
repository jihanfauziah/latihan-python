barang1 = 20000
barang2 = 50000
barang3 = 40000
barang4 = 120000

# Menghitung total belanja
total_belanja = barang1 + barang2 + barang3 + barang4

# Memeriksa apakah total belanja memenuhi syarat diskon
if total_belanja >= 200000:
    diskon = total_belanja * 0.075  # 7.5% diskon
else:
    diskon = 0

# Menghitung total bayar setelah diskon
total_bayar = total_belanja - diskon

# Menampilkan hasil
print("Total Belanja :", total_belanja)
print("Diskon        :", diskon)
print("Total Bayar   :", total_bayar)