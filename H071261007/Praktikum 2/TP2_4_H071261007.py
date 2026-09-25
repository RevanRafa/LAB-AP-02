# Nomor 4

Tujuan = (input("Masukkan tujuan (Pantai/Pegunungan/Kota): "))
if Tujuan != "Pantai" and Tujuan != "Pegunungan" and Tujuan != "Kota":
   print("Invalid")
   exit()
else:
    Waktu = (input("Masukkan waktu (Pagi/Malam): "))
    if Waktu != "Pagi" and Waktu != "Malam":
       print("Invalid")
       exit()
    else:
        Tipe_pengunjung = (input("Masukkan tipe pengunjung (Anak/Dewasa): "))
        if Tipe_pengunjung != "Anak" and Tipe_pengunjung != "Dewasa":
           print("Invalid")
           exit()
        else:
            match Tujuan:
                case "Pantai" | "Pegunungan" | "Kota":
                    if Waktu == "Malam" and Tipe_pengunjung == "Dewasa":
                     print("Paket Rekomendasi: Paket C")
                    else:
                        match Tujuan:
                            case "Pantai":
                                if Waktu == "Pagi":
                                 print("Paket Rekomendasi: Paket A")
                                else:
                                    print("Tidak ada paket yang cocok")
                            case "Pegunungan":
                                if Waktu == "Pagi" and Tipe_pengunjung == "Dewasa":
                                 print("Paket Rekomendasi: Paket B")
                                else:
                                    print("Tidak ada paket yang cocok")
                            case "Kota":
                                if Waktu == "Malam":
                                    print("Paket Rekomendasi: Paket C")
                                else:
                                    print("Tidak ada paket yang cocok")