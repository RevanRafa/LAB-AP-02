# Nomor 3

ALFABET = "abcdefghijklmnopqrstuvwxyz"

def cek_sandi(ch, k):
    cek_kapital = ch.isupper()
    ch_lower = ch.lower()
    posisi_asli = ALFABET.find(ch_lower)
    if posisi_asli == -1:
        return ch
    posisi_baru = (posisi_asli + k) % len(ALFABET)
    ch_baru = ALFABET[posisi_baru]
    return ch_baru.upper() if cek_kapital else ch_baru

def mesin_enkripsi(teks, k):
    hasil = ""
    for ch in teks:
        hasil += cek_sandi(ch, k)
    return hasil

def mesin_dekripsi(teks, k):
    return mesin_enkripsi(teks, -k)

def retas_sandi(sandi, kata_kunci):
    hasil = []
    for k in range(26):
        pesan_dekripsi = mesin_dekripsi(sandi, k)
        if pesan_dekripsi.lower().find(kata_kunci.lower()) != -1:
            hasil.append((k, pesan_dekripsi))
    return hasil

sandi = input("Masukkan pesan tersita (enkripsi Caesar): ")
kata_kunci = input("Masukkan kata kunci target: ")
print(f"Output Deskripsi: {retas_sandi(sandi, kata_kunci)}")