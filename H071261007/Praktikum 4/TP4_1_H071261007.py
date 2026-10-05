# Nomor 1

def hitung_subtotal(harga, jumlah, adalah_member):

    subtotal = harga * jumlah

    if adalah_member:
        subtotal = int(subtotal * 0.9)

    return subtotal

print("Selamat datang di Kasir Minimarket!\n")

while True:
    adalah_member = input("Apakah Anda member? (y/n): ")
    if adalah_member == "y":
        adalah_member = True
        break
    elif adalah_member == "n":
        adalah_member = False
        break
    else:
        print("Input invalid\n")

total = 0

while True:
    barang = input("Masukkan nama barang (kosongkan untuk selesai): ")
    if barang == "":
        break
    harga = int(input("Harga barang: "))
    jumlah = int(input("Jumlah barang: "))

    subtotal = hitung_subtotal(harga, jumlah, adalah_member)
    total += subtotal

    print(f"Subtotal {barang}: Rp{subtotal:,}\n")

print(f"Total belanja: Rp{total:,}")