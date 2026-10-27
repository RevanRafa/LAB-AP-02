# Nomor 1

import re

def validasi_nim(nim):
    pattern = r"^H071\d{6}$"
    return bool(re.match(pattern, nim))

def validasi_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$" #x@x.x
    return bool(re.match(pattern, email))

def validasi_telepon(no_telephone):
    pattern = r"^[08]\d{10,13}$"
    return bool(re.match(pattern, no_telephone))

# -----

print("--- Validasi Data Mahasiswa ---")
nim = input("Masukkan NIM".ljust(19)+": ")
email = input("Masukkan Email".ljust(19)+": ")
no_telephone = input("Masukkan No. Telp".ljust(19)+": ")

print("\n--- Hasil Validasi ---")

if validasi_nim(nim):
    print("NIM".ljust(12)+": Valid")
    status_nim = True
else:
    print("NIM".ljust(12)+": Format NIM tidak valid!")
    status_nim = False
    
if validasi_email(email):
    print("Email".ljust(12)+": Valid")
    status_email = True
else:
    print("Email".ljust(12)+": Format email tidak valid!")
    status_email = False
    
if validasi_telepon(no_telephone):
    print("No. Telepon".ljust(12)+": Valid")
    status_telp = True
else:
    print("No. Telepon".ljust(12)+": Nomor telepon tidak valid!")
    status_telp = False
    
if status_nim and status_email and status_telp:
    print("\nData mahasiswa berhasil diverifikasi!")