# Nomor 4

def konversi_suhu(suhu, skala_asal, skala_tujuan):

    if skala_asal == skala_tujuan:
        suhu = suhu
    elif skala_asal == "C":
        if skala_tujuan == "F":
            suhu = (9 / 5 * suhu) + 32
        elif skala_tujuan == "K":
            suhu = suhu + 273.15
    elif skala_asal == "F":
        if skala_tujuan == "C":
            suhu = 5 / 9 * (suhu - 32)
        elif skala_tujuan == "K":
            suhu = 5 / 9 * (suhu - 32) + 273.15
    elif skala_asal == "K":
        if skala_tujuan == "C":
            suhu = suhu - 273.15
        elif skala_tujuan == "F":
            suhu = 9 / 5 * (suhu - 273.15) + 32

    return suhu

print("=== Konversi Suhu ===")

while True:

    suhu = input("Masukkan suhu (atau 'selesai' untuk keluar): ").lower()
    if suhu == "selesai":
        break
    else:
        suhu = float(suhu)

    try:

        skala_asal = input("Skala asal (C/F/K): ").upper()
        if skala_asal != "C" and skala_asal != "F" and skala_asal != "K":
            raise ValueError

        skala_tujuan = input("Skala tujuan (C/F/K): ").upper()
        if skala_tujuan != "C" and skala_tujuan != "F" and skala_tujuan != "K":
            raise ValueError

        print(f"Hasil: {suhu} {skala_asal} --> {konversi_suhu(suhu, skala_asal, skala_tujuan)} {skala_tujuan} ")

    except ValueError:
        print("Error: Skala suhu tidak dikenali")