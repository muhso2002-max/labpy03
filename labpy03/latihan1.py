from random import random

n = int(input("Masukkan nilai N: "))
i = 1

while i <= n:
    angka = random()
    if angka < 0.5:
        print(f"data ke: {i} => {angka}")
    i += 1

print("Program selesai.")
