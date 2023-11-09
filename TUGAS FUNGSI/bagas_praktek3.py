# Nama   = Bagas Andrianto
# Kelas  = XI-TKJ2
# No     = 05 
# Soal   = Buatlah sebuah fungsi yang menghitung nilai pangkat dari suatu bilangan
#          dengan eksponen tertentu.

def hitung_pangkat(basis, eksponen):
    hasil = 1
    for _ in range(eksponen):
        hasil *= basis
    return hasil

basis = float(input("Masukkan basis: "))
eksponen = int(input("Masukkan eksponen: "))
hasil_pangkat = hitung_pangkat(basis, eksponen)
print(f"{basis} pangkat {eksponen} = {hasil_pangkat}")