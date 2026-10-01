# Nomor 2

print("--- Setup Denah Bioskop NontonYuk ---")

try:
     baris = int(input("Masukkan jumlah baris: "))
     if baris <= 0:
        print("Jumlah baris harus lebih dari 0!")
        exit()
except ValueError:
     print("Input baris harus berupa angka!")
     exit()
   

try:
     kursi = int(input("Masukkan jumlah kursi: "))
     if kursi <= 0:
        print("Jumlah kursi harus lebih dari 0!")
        exit()
except ValueError:
     print("Input kursi harus berupa angka!")
     exit()
     


print("--- Daftar Kursi Tersedia ---")

for baris in range(1,baris + 1):
    for kursi in range(1,kursi + 1):
         if kursi == 13:
              continue
         elif baris == 1 and kursi % 2 == 0:
              continue
         print(f"Baris {baris} - Kursi {kursi}")
