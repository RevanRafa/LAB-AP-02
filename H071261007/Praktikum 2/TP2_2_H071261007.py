# Nomor 2

try:

    jarak = float(input("Masukkan jarak pengiriman (km): "))
    if jarak < 0:
        print("Invalid")
        exit()
    else:
        layanan = (input("Layanan express (ya/tidak): "))
        if layanan != "ya" and layanan != "tidak":
            print("Invalid")
            exit()
        else:
            if jarak >= 0 and jarak < 5:
                tarif = 10000
            elif jarak >= 5 and jarak <= 20:
                tarif = 20000
            else:
                tarif = 35000

        total_tarif = tarif + 15000 if "ya" == layanan else 0
        print(f"Total tarif pengiriman: Rp{total_tarif:,}")

except ValueError:
     print("Invalid")
     exit()