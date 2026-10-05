# Nomor 2

def rekap_nilai(*nilai):

    rata_rata = sum(daftar_nilai) / len(daftar_nilai)
    tertinggi = int(max(daftar_nilai))
    terendah = int(min(daftar_nilai))

    return rata_rata, tertinggi, terendah

daftar_nilai = []

while True:

    nilai = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
    if nilai == "":
        break

    daftar_nilai.append(float(nilai))

if daftar_nilai:
    rata_rata, tertinggi, terendah = rekap_nilai(nilai)

    print(f"Rata-rata kelas: {rata_rata}")
    print(f"Nilai tertinggi: {tertinggi}")
    print(f"Nilai terendah: {terendah}")

else:
    print("Data nilai tidak tersedia.")
