class Pemain:
    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objective = nilai_objective

    def hitung_skor_akhir(self):
        return (0.3 * self.nilai_kill) + (0.3 * self.nilai_assist) + (0.4 * self.nilai_objective)

    def status_performa(self):
        if self.hitung_skor_akhir() >= 60:
            return "Unggul"
        else:
            return "Perlu Evaluasi"

    def tampilkan_data(self):
        skor_akhir = self.hitung_skor_akhir()
        status = self.status_performa()
        return f"{self.nama:<11} | {self.id_pemain:<13} | {self.role:<11} | {skor_akhir:<11.2f} | {status:<14}"

print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===")

jumlah_pemain = int(input("Masukkan jumlah pemain: "))

daftar_pemain = []

for i in range(jumlah_pemain):
    print(f"\n--Data Pemain ke-{i+1}--")
    nama = input("Nama: ")
    id_pemain = input("ID Pemain: ")
    role = input("Role: ")
    nilai_kill = int(input("Nilai Kill: "))
    nilai_assist = int(input("Nilai Assist: "))
    nilai_objective = int(input("Nilai Objective: "))

    pemain = Pemain(nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective)
    daftar_pemain.append(pemain)

print("\n=== REKAPITULASI PERFORMA PEMAIN ===")
print("=" * 81)
print(f"| {'No':<2} | {'Nama':<11} | {'ID Pemain':<13} | {'Role':<11} | {'Skor Akhir':<11} | {'Status':<14} |")
print("=" * 81)
for i, pemain in enumerate(daftar_pemain, start=1):
    print(f"| {i:<2} | {pemain.tampilkan_data()} |")
print("=" * 81)