print("Program untuk menentukan kelulusan siswa berdasarkan nilai ujian dan persentase kehadiran")

def cek_kelulusan(nilai_ujian, persen_kehadiran):
    if nilai_ujian >= 75 and persen_kehadiran >= 70:
        return "Lulus"
    elif nilai_ujian < 75 and persen_kehadiran >= 70:
        return "Tidak Lulus (nilai kurang)"
    elif nilai_ujian >= 75 and persen_kehadiran < 70:
        return "Tidak Lulus (kehadiran kurang)"
    else:
        return "Tidak Lulus (nilai dan kehadiran kurang)"

nilai = float(input("Masukkan nilai ujian (0-100): "))
kehadiran = float(input("Masukkan persen kehadiran (0-100): "))

hasil = cek_kelulusan(nilai, kehadiran)

print("=== Hasil Kelulusan Siswa ===") 
print(f"Status: {hasil}")
