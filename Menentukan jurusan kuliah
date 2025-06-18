def rekomendasi_jurusan(minat, pelajaran):
    if minat == "sains":
        if pelajaran == "matematika":
            return "Teknik"
        elif pelajaran == "biologi":
            return "Kedokteran"
    elif minat == "sosial":
        if pelajaran == "ekonomi":
            return "Manajemen"
        elif pelajaran == "bahasa":
            return "Ilmu Komunikasi"
    elif minat == "seni" and pelajaran == "seni budaya":
        return "Desain"
    elif minat == "teknologi" and pelajaran == "matematika":
        return "Teknik Informatika"
    else:
        return "Belum ada jurusan yang cocok ditemukan."

print("=== Sistem Pakar: Pilih Jurusan Kuliah ===")
minat = input("Apa minat kamu? (sains/sosial/seni/teknologi): ").lower()
pelajaran = input("Pelajaran favorit kamu? (matematika/biologi/ekonomi/bahasa/seni budaya): ").lower()

jurusan = rekomendasi_jurusan(minat, pelajaran)

print("=== Hasil Rekomendasi Jurusan ===")
print(f"Rekomendasi jurusan: {jurusan}") 
