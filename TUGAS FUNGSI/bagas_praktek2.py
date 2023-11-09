# Nama   = Bagas Andrianto
# Kelas  = XI-TKJ2
# No     = 05 
# Soal   = Buatlah sebuah fungsi untuk menghitung faktorial dari suatu bilangan.

def hitung_faktorial(n):
    faktorial = 1
    for i in range(1, n + 1):
        faktorial *= i
    return faktorial

bilangan = int(input("Masukkan bilangan: "))
hasil_faktorial = hitung_faktorial(bilangan)
print("Faktorial dari", bilangan, "adalah", hasil_faktorial)