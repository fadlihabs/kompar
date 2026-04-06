# Program sederhana tentang looping

print("=== Contoh Looping For ===")
for i in range(1, 6):
    print(f"Perulangan ke-{i}")

print("\n=== Contoh Looping While ===")
angka = 1
while angka <= 5:
    print(f"Angka saat ini: {angka}")
    angka += 1

print("\n=== Tabel Perkalian 1-3 ===")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
