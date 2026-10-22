playlist = []       
genre_set = set()   


def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    playlist.append((judul, artis, genre, durasi))
    genre_set.add(genre)


def tampilkan_playlist(playlist):
    garis = "=" * 55
    print(garis)
    print(f" {'No':<4}{'Judul':<20}{'Artis':<15}{'Genre':<10}Durasi")
    print(garis)
    for no, (judul, artis, genre, durasi) in enumerate(playlist, start=1):
        print(f" {no:<4}{judul:<20}{artis:<15}{genre:<10}{durasi // 60}:{durasi % 60:02d}")
    print(garis)
    total_durasi = 0
    for lagu in playlist:
        total_durasi = total_durasi + lagu[3]
    print(f" Total durasi playlist: {total_durasi // 60} menit {total_durasi % 60} detik")


def filter_genre(playlist, genre_target):
    playlist_terfilter = []
    for lagu in playlist:
        if lagu[2] == genre_target:
            playlist_terfilter.append(lagu)
    print(f"\nLagu bergenre '{genre_target}':")
    for no, (judul, artis, _, durasi) in enumerate(playlist_terfilter, start=1):
        print(f"  {no}. {judul} - {artis} ({durasi // 60}:{durasi % 60:02d})")


def hapus_lagu(playlist, nomor):
    if nomor < 1 or nomor > len(playlist):
        print("Nomor lagu tidak valid.")
        return
    judul_dihapus = playlist.pop(nomor - 1)[0]
    genre_set.clear()
    for lagu in playlist:
        genre_set.add(lagu[2])
    print(f"Lagu '{judul_dihapus}' berhasil dihapus.")


def statistik_playlist(playlist, genre_set):
    jumlah_per_genre = {}
    for _, _, genre, _ in playlist:
        jumlah_per_genre[genre] = jumlah_per_genre.get(genre, 0) + 1

    terpanjang = max(playlist, key=lambda lagu: lagu[3])
    terpendek = min(playlist, key=lambda lagu: lagu[3])

    print("=" * 40)
    print("   STATISTIK PLAYLIST - PLAYTUNE")
    print("=" * 40)
    print(f"Total lagu     : {len(playlist)}")
    print(f"Jumlah genre   : {len(genre_set)}")
    print(f"Daftar genre   : {genre_set}")
    print()
    print("Distribusi genre:")
    for genre, jumlah in jumlah_per_genre.items():
        print(f"  {genre:<8}: {'#' * jumlah} ({jumlah})")
    print()
    print(f"Lagu terpanjang: {terpanjang[0]} ({terpanjang[3] // 60}:{terpanjang[3] % 60:02d})")
    print(f"Lagu terpendek : {terpendek[0]} ({terpendek[3] // 60}:{terpendek[3] % 60:02d})")
    print("=" * 40)


print("=" * 40)
print("   PLAYLIST MUSIK - PLAYTUNE")
print("=" * 40)
print()
print("Menu:")
print("1. Tambah Lagu")
print("2. Tampilkan Playlist")
print("3. Filter berdasarkan Genre")
print("4. Hapus Lagu")
print("5. Statistik Playlist")
print("6. Keluar")

while True:
    try:
        menu = int(input("Pilih menu (1-6): "))
    except ValueError:
        print("Input tidak valid, masukkan angka 1-6.\n")
        continue

    if menu == 1:
        judul = input("Judul lagu: ").strip().title()
        artis = input("Artis: ").strip().title()
        genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ").strip().title()
        try:
            durasi = int(input("Durasi (dalam detik): "))
            if durasi <= 0:
                raise ValueError
        except ValueError:
            print("Durasi harus berupa angka positif.\n")
            continue
        tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)
        print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!\n")

    elif menu == 2:
        print()
        if not playlist:
            print("Playlist masih kosong.\n")
            continue
        tampilkan_playlist(playlist)
        print()

    elif menu == 3:
        if not playlist:
            print("Playlist masih kosong.\n")
            continue
        print(f"Genre tersedia: {genre_set}")
        target = input("Masukkan genre yang ingin difilter: ").strip().title()
        filter_genre(playlist, target)
        print()

    elif menu == 4:
        if not playlist:
            print("Playlist masih kosong.\n")
            continue
        print()
        tampilkan_playlist(playlist)
        try:
            nomor = int(input("\nMasukkan nomor lagu yang ingin dihapus: "))
        except ValueError:
            print("Nomor harus berupa angka.\n")
            continue
        hapus_lagu(playlist, nomor)
        print()

    elif menu == 5:
        if not playlist:
            print("Playlist masih kosong.\n")
            continue
        statistik_playlist(playlist, genre_set)
        print()

    elif menu == 6:
        print("Terima kasih telah menggunakan PlayTune!")
        break

    else:
        print("Menu hanya 1-6.\n")