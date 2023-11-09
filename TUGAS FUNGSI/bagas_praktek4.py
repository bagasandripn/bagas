# Nama   = Bagas Andrianto
# Kelas  = XI-TKJ2
# No     = 05 
# Soal   = Buatlah sebuah fungsi untuk menghitung jumlah digit dari suatu bilangan.

def hitung_jumlah_digit(bilangan):
    # Mengonversi bilangan menjadi string untuk menghitung jumlah digit
    bilangan_str = str(bilangan)
    # Menghitung jumlah digit
    jumlah_digit = len(bilangan_str)
    return jumlah_digit

bilangan = int(input("Masukkan bilangan: "))
jumlah_digit = hitung_jumlah_digit(bilangan)
print("Jumlah digit dari", bilangan, "adalah", jumlah_digit)