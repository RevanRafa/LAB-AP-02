# Nomor 3

import re

print("=== Pembersihan Data Nomor Telepon ===")
jumlah_no_telephone = int(input("Masukkan jumlah data: "))

list_nomor = []

for i in range(1, jumlah_no_telephone + 1):
    no_telephone = input(f"Nomor ke-{i}: ")
    list_nomor.append(no_telephone)

print("\n--- Hasil Pembersihan ---")

list_nomor_valid = []
jumlah_nomor_valid = 0

for i in range(jumlah_no_telephone):
    sebelum = list_nomor[i]
    sesudah = re.sub(r"[\s-]", "", sebelum)
    
    if re.match(r"^\d{10,13}$", sesudah):
        status = "Valid"
        jumlah_nomor_valid += 1
        list_nomor_valid.append(sesudah)
    else:
        status = "Tidak valid"
        
    print(f"Data {i+1}:")
    print(f"Sebelum : {sebelum}")
    print(f"Sesudah : {sesudah}")
    print(f"Status  : {status}\n")

print(f"Jumlah nomor valid: {jumlah_nomor_valid}")