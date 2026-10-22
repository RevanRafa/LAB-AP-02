# Nomor 2

def daftar_kandidat(kandidat_set, nama):
    nama = nama.capitalize()
    if nama in kandidat_set:
        print(f"'{nama}' sudah terdaftar!")
    else:
        kandidat_set.add(nama)
        print(f"'{nama}' berhasil didaftarkan sebagai kandidat!")


def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    nama_pemilih = nama_pemilih.lower()
    pilihan = pilihan.capitalize()

    if pilihan not in kandidat_set:
        print(f"Error: kandidat '{pilihan}' tidak ada! Suara tidak dicatat.")
    elif nama_pemilih in rekap_suara:
        print(f"'{nama_pemilih}' sudah memberikan suara! Suara tidak dicatat.")
    else:
        rekap_suara[nama_pemilih] = pilihan
        print(f"Suara '{nama_pemilih}' untuk '{pilihan}' berhasil dicatat!")

# rekap_suara = {"nama_pemilih X":"pilihan A", "nama_pemilih Y":"pilihan A"}

def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}
    for kandidat in kandidat_set:
        perolehan[kandidat] = 0
    for pilihan in rekap_suara.values():
        perolehan[pilihan] += 1
    return perolehan

# perolehan = {"kandidat A":0+1+1,"kandidat B":0}

def tampilkan_hasil(perolehan):
    for nama, jumlah in perolehan.items():
        print(f"   {nama}: {jumlah} suara")
    print()
    print(f"Total suara masuk: {sum(perolehan.values())}")

    suara_tertinggi = max(perolehan.values())
    
    pemenang = []
    for nama, jumlah in perolehan.items():
        if jumlah == suara_tertinggi:
            pemenang.append(nama)

    if len(pemenang) > 1:
        print("Hasil seri! Perlu pemilihan ulang.")
    else:
        print(f"PEMENANG: {pemenang[0]} dengan {suara_tertinggi} suara!")


#-----

kandidat_set = set()
rekap_suara = {}

print("==================================")
print("   SISTEM PEMILIHAN KETUA KELAS")
print("==================================")

while True:
    nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ")
    if nama == "":
        if len(kandidat_set) < 2:
            print("Minimal harus ada 2 kandidat!")
            continue
        break
    daftar_kandidat(kandidat_set, nama)

print(f"\nKandidat terdaftar: {sorted(kandidat_set)}")

print()
print("--- FASE PEMUNGUTAN SUARA ---")
print()

while True:
    nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ")
    if nama_pemilih == "":
        break
    print(f"Kandidat yang tersedia: {sorted(kandidat_set)}")
    pilihan = input("Pilih kandidat: ")
    berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)

print()
print("=================================")
print("   HASIL PEMILIHAN KETUA KELAS   ")
print("=================================")
print()
perolehan = hitung_suara(rekap_suara, kandidat_set)
tampilkan_hasil(perolehan)