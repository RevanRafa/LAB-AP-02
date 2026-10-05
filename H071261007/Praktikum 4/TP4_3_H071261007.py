# Nomor 3

def hitung_mundur(angka_awal):

    if angka_awal < 0:
        print("Luncurkan!")
    else:
        print(angka_awal)
        hitung_mundur(angka_awal - 1)

while True:

    angka_awal = int(input("Masukkan angka awal hitung mundur: "))
    if angka_awal < 0:
        print("Input tidak valid, angka tidak boleh negatif!\n")
    else:
        (hitung_mundur(angka_awal))
        break
