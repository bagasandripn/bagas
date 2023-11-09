# Nama   = Bagas Andrianto
# Kelas  = XI-TKJ2
# No     = 05 
# Soal   = Buatlah sebuah fungsi yang menghitung bilangan Fibonacci ke-n.

def fibonacci(n):
    if n <= 0:
        return "Input harus lebih besar dari 0"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Masukkan nilai n: "))
hasil = fibonacci(n)
print(f"Bilangan Fibonacci ke-{n} adalah {hasil}")
