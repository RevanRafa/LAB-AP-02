# Nomor 1

print("--- Rekapitulasi Transaksi Dins Store ---")
print("Ketik '0' untuk menutup toko dan mengakhiri sesi\n")

item = 0

while item >= 0 or item < 0:
        try:

            item = int(input("Masukkan jumlah item: "))
            if item > 100:
                print("Maksimal 100 item per transaksi!\n")
            elif item < 0:
                print("Jumlah tidak boleh negatif\n")
            elif item > 0:
                print(f"Transaksi {item} item telah berhasil\n")
            else:
                print("Toko telah ditutup. Sesi rekap selesai.")
                break 

        except ValueError:
            print("Input harus berupa angka\n")