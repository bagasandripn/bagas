# Nama   = Bagas Andrianto
# Kelas  = XI-TKJ2
# No     = 05 
# Soal   = Buatlah sebuah fungsi yang menghitung total dari deret bilangan ganjil hingga
#          batas tertentu yang ditentukan pengguna.

def total_bilangan_ganjil(batas):
    total = 0
    for i in range(1, batas + 1, 2):
        total += i
    return total

batas = int(input("Masukkan batas: "))
hasil = total_bilangan_ganjil(batas)
print("Total deret bilangan ganjil hingga batas", batas, "adalah", hasil)
