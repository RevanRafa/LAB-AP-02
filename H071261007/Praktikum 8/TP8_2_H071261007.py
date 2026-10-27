# Nomor 2

import re

def validasi_username(username):
    pattern = r"^[a-zA-Z]\w{4,11}$"
    return bool(re.match(pattern, username))

# -----

print("--- Registrasi Username ---")
print("Ketik 'SELESAI' untuk mengakhiri.\n")

list_username_valid = []

while True:
    username = input("Masukkan username: ")
    
    if username.upper() == "SELESAI":
        break
        
    if validasi_username(username):
        print("Username tersedia.\n")
        list_username_valid.append(username)
    else:
        print("Username tidak valid!\n")

print("\n--- Rekapitulasi ---")
print("Username valid:")
for i, username in enumerate(list_username_valid, 1):
    print(f"{i}. {username}")

print(f"Jumlah username valid: {len(list_username_valid)}")