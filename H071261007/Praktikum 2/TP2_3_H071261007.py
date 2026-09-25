# Nomor 3

try:

    nilai = float(input("Masukkan nilai tes: "))
    if nilai < 0:
        print("Invalid")
        exit()
    elif nilai >= 80:
        print("Lolos ke Tahap Wawancara")
    else:
        pengalaman = float(input("Masukkan pengalaman kerja (tahun): "))
        if pengalaman < 0:
            print("Invalid")
            exit()
        else:
            if nilai >= 65 and pengalaman >= 2:
                print("Lolos bersyarat")
            else:
                print("Tidak lolos")

except ValueError:
    print("Invalid")
    exit()