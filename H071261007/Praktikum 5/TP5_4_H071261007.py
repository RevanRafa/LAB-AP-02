# Nomor 4

def deteksi_anomali_email(email):
    anomali = []
    
    if " " in email:
        anomali.append("Tidak boleh mengandung spasi di posisi manapun.")
        
    count_at = email.count("@")
    if count_at != 1:
        anomali.append("Harus memiliki tepat satu karakter @.")
        return anomali

    local, domain = email.split("@")

    if len(local) == 0 or len(domain) == 0:
        anomali.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")

    if local.startswith(".") or local.endswith(".") or ".." in local:
        anomali.append("Bagian local tidak boleh diawali atau diakhiri titik (.), serta tidak boleh mengandung titik berurutan (..).")

    if "." not in domain:
        anomali.append("Bagian domain wajib memiliki minimal satu titik.")
    
    if ".." in domain or domain.endswith("."):
        anomali.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")

    if not (email.endswith(".com") or email.endswith(".id") or email.endswith(".ac.id")):
        anomali.append("Wajib berakhiran dengan .com, .id, atau .ac.id")

    return anomali

def cetak_daftar(daftar_email_valid, karakter_border):
    if not daftar_email_valid:
        return ""
    max_len = max(len(email) for email in daftar_email_valid)
    width = max_len + 4
    border_line = (karakter_border * width)[:width]
    lines = [border_line]
    for email in daftar_email_valid:
        lines.append(f"| {email.ljust(max_len)} |")
    lines.append(border_line)
    return "\n".join(lines)

print("=== Sistem Pencatatan Email Valid ===")
border_char = input("Masukkan border dengan karakter bebas: ")
print("\nKetik 'tutup' untuk mengakhiri masukan dan mencetak email.")

email_valid_list = []

while True:
    email = input("Masukkan email: ")
    if email.lower() == "tutup":
        break
    
    if email in email_valid_list:
        print(">> Email DITOLAK karena:")
        print("   - Email sudah terdaftar (Duplikat)")
        continue

    anomali = deteksi_anomali_email(email)
    if len(anomali) == 0:
        email_valid_list.append(email)
        print(">> Email VALID!")
    else:
        print(">> Email DITOLAK karena:")
        for error in anomali:
            print(f"   - {error}")

print("\n=== HASIL EMAIL VALID ===")
print(cetak_daftar(email_valid_list, border_char))