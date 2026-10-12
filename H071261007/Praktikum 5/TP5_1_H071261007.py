# Nomor 1

def bersihkan_teks(teks):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    teks = teks_input.lower()
    teks_bersih = ""
    for character in teks:
        if character in alfabet:
            teks_bersih += character
    return teks_bersih

def cek_palinrome(teks):
    teks_reversed = "".join(reversed(teks))
    if teks == teks_reversed:
        return (True, -1)
    for huruf in range(len(teks)):
        if teks[huruf] != teks_reversed[huruf]:
            return (False, huruf)

def inti_palinrome(teks):
    panjang_maksimal = 0
    substring_maksimal = ""
    indeks_awal = 0
    for huruf_awal in range(len(teks)):
        for huruf_akhir in range(huruf_awal + 1, len(teks) + 1):
            substring = teks[huruf_awal:huruf_akhir]    
            if len(substring) > panjang_maksimal and cek_palinrome(substring)[0]:
                    panjang_maksimal = len(substring)
                    substring_maksimal = substring
                    indeks_awal = huruf_awal
    return {"teks": substring_maksimal, "panjang": panjang_maksimal, "indeks_awal": indeks_awal}
teks_input = input("Masukkan teks prasasti: ")

teks_bersih = bersihkan_teks(teks_input)
print(f"Teks Bersih: {teks_bersih}")

hasil = inti_palinrome(teks_bersih)
print(f"Output Terharap: {hasil}")