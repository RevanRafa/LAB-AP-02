# Nomor 3

kursi = 0

while kursi >= 0 or kursi < 0:

    try:

        kursi = int(input("Masukkan maksimal kursi bus: "))
        if kursi <= 0:
            print("Input harus lebih dari 0!\n")
            continue
        break

    except ValueError:
        print("Input jumlah kursi harus berupa angka!\n")

print("--- Sistem Reservasi PO BUS Dimulai ---\n")

profit = 0

while kursi > 0:
    print(f"Sisa kursi: {kursi}")

    try:

        umur = int(input("Masukkan umur penumpang: "))
        
        if umur < 0:
            print("Umur tidak valid!\n")
            continue
        elif umur >= 0 and umur <= 5:
            print("Kategori: Balita - Tiket Gratis (Rp 0)\n")
            pendapatan = 0
        elif umur >= 6 and umur <= 12:
            print("Kategori: Anak - Harga Rp 50.000\n")
            pendapatan = 50000
        else:
            print("Kategori: Dewasa - Harga Rp 100.000\n")
            pendapatan = 100000

        kursi -= 1
        profit += pendapatan

        if kursi == 0:
            print("--- Semua Kursi Terisi ---")
            print(f"Total pendapatan perjalanan PO BUS kali ini: Rp {profit}")

    except ValueError:

        print("Input umur harus berupa angka!\n")