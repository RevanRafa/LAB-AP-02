menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000,22000, 15000]
jumlah = [4, 3, 5]

subtotal_kopi = harga [0] * jumlah [0]
subtotal_matcha = harga [1] * jumlah [1]
subtotal_americano = harga [2] * jumlah [2]

subtotal_pendapatan = [subtotal_kopi, subtotal_matcha, subtotal_americano]

BIAYA_OPERASIONAL = 15000
total_pendapatan = sum(subtotal_pendapatan)
pendapatan_bersih = total_pendapatan - BIAYA_OPERASIONAL

jumlah_barang = sum(jumlah)
target_tercapai = "Ya" if 200000 < total_pendapatan and jumlah_barang > 10 else "Tidak"

print("\n=== Laporan Penjualan Kopi Senja===\n")
for i in range (len(menu)):
    print (f"Subtotal {menu[i]}: Rp{subtotal_pendapatan[i]:,} ")
print(f"Subtotal pendapatan: {total_pendapatan:,}")
print(f"Pendapatan bersih: Rp{pendapatan_bersih:,}")
print(f"Targer tercapai?: {target_tercapai}")
