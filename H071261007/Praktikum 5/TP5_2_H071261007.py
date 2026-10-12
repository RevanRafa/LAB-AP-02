# Nomor 2

def cek_kata(teks, kata):
    teks_lower = teks.lower()
    kata_lower = kata.lower()
    list_index_kemunculan = []
    posisi = 0
    while True:
        index_kemunculan = teks_lower.find(kata_lower, posisi)
        if index_kemunculan != -1:
            list_index_kemunculan.append(index_kemunculan)
        else:
            break
        posisi = index_kemunculan + len(kata_lower)
    return list_index_kemunculan

def cek_batas_kata(teks, i, panjang):
    alfabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if i == 0:
        huruf_sebelum_kata = False
    elif teks[i - 1] in alfabet:
        huruf_sebelum_kata = True
    else:
        huruf_sebelum_kata = False

    index_sesudah = i + panjang
    if index_sesudah >= len(teks):
        huruf_sesudah_kata = False
    elif teks[index_sesudah] in alfabet:
        huruf_sesudah_kata = True
    else:
        huruf_sesudah_kata = False

    return not huruf_sebelum_kata and not huruf_sesudah_kata

def sensor_kata(teks, kata, simbol):
    semua_indeks = cek_kata(teks, kata)
    panjang = len(kata)
    indeks_valid = []
    for indeks_akhir in semua_indeks:
        if cek_batas_kata(teks, indeks_akhir, panjang):
            indeks_valid.append(indeks_akhir)

    teks_tersensor = ""
    indeks_awal = 0
    for indeks_akhir in indeks_valid:
        teks_tersensor += teks[indeks_awal:indeks_akhir] + (simbol * panjang)
        indeks_awal = indeks_akhir + panjang
    teks_tersensor += teks[indeks_awal:]

    return (teks_tersensor, len(indeks_valid), indeks_valid)

teks = input("Masukkan Teks: ")
kata = input("Masukkan kata target: ")
simbol = input("Masukkan simbol: ")

hasil_teks, jumlah, list_indeks_kemunculan = sensor_kata(teks, kata, simbol)
print(f"Hasil Teks: {hasil_teks}")
print(f"Jumlah: {jumlah} | Indeks: {list_indeks_kemunculan}")
