modal = 100000000
laba_total = 0

for bulan in range(1, 9):
    if bulan <= 2:
        laba = 0
    elif bulan <= 4:
        laba = modal * 0.01
    elif bulan <= 7:
        laba = modal * 0.05
    else:
        laba = modal * 0.02
    laba_total += laba
    print(f"Laba bulan ke- {bulan} sebesar: {laba}")

print(f"\nTotal laba adalah:{laba_total}")