print("Program Mencari Nilai Rata-Rata Mahasiswa")

nama = input("Masukkan nama anda: ")
npm = input("Masukkan NPM anda: ")

print("List nilai mata kuliah:")

dpp = float(input("Dasar-Dasar Pemrograman: "))
si = float(input("Sistem informasi: "))
bd = float(input("Basis Data: "))
m = float(input("Multimedia: "))
k = float(input("Kalkulus: "))
an = float(input("Analisis Numerik: "))

nilai = dpp + si + bd + m + k + an
rata_rata = nilai / 6

print("=== Hasil Rata-Rata Nilai Mahasiswa ===")
print("Rata-rata nilai", nama, "dengan NPM", npm, "adalah:", rata_rata) 