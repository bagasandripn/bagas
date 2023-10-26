# nama: Bagas andri
# kelas: XI TKJ 2
# nomor absen: 05
# soal: Buat program Python yang mengambil total belanjaan dan status anggota (biasa atau premium).Berikan diskon berdasarkan aturan berikut: • Anggota premium: Jika total belanjaan lebih dari 500.000, berikan diskon 15%. Jika tidak, berikan diskon 10%. • Anggota biasa: Jika total belanjaan lebih dari 300.000, berikan diskon 7%. Jika tidak, berikan diskon 0%.
# Input total belanjaan
total_belanjaan = float(input("Masukkan total belanjaan: "))

# Input status anggota (biasa atau premium)
status_anggota = input("Apakah Anda anggota (biasa/premium)? ").lower()

# Inisialisasi variabel diskon
diskon = 0

# Menghitung diskon berdasarkan aturan yang telah diberikan
if status_anggota == "premium":
    if total_belanjaan > 500000:
        diskon = 0.15  # Diskon 15% untuk anggota premium jika total belanjaan > 500.000
    else:
        diskon = 0.10  # Diskon 10% untuk anggota premium jika total belanjaan <= 500.000
elif status_anggota == "biasa":
    if total_belanjaan > 300000:
        diskon = 0.07  # Diskon 7% untuk anggota biasa jika total belanjaan > 300.000

# Menghitung jumlah yang harus dibayar setelah diskon
jumlah_bayar = total_belanjaan - (total_belanjaan * diskon)

# Menampilkan hasil
if diskon > 0:
    print(f"Anda mendapatkan diskon {diskon*100}%.")
    print(f"Total yang harus dibayar: Rp {jumlah_bayar:.2f}")
else:
    print("Anda tidak mendapatkan diskon.")
    print(f"Total yang harus dibayar: Rp {total_belanjaan:.2f}")