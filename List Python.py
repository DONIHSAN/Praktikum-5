# Membuat sebuah list sebanyak 5 elemen dengan nilai bebas

Numbering = ['100', '200', '300', '400', '500', '600']

# AKSES LIST

# Tampilkan elemen ke 3
print("Numbering[3]:", Numbering[3])

print('\n')

# Ambil nilai elemen ke 2 sampai 4
print("Numbering[2:4]:", Numbering[2:4])
print()

# Ambil elemen terakhir
print("Numbering[5]:", Numbering[5])
print()

# UBAH ELEMEN LIST

# Ubah elemen ke 4 dengan nilai lainnya
print("Nilai Juri ke peserta No 4 :", Numbering[4])

Numbering[4] = 575
print("Nilai baru peserta No 4 Adalah :",Numbering[4])
print()


# Ubah elemen ke 4 sampai dengan elemen terakhir
Numbering[4:] = ["585", "675"]
print("Ubah element ke-4 hingga akhir :", Numbering)
print()

# TAMBAH ELEMEN LIST

# Ambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B)
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

b.append(a[0:2])
print(b)

# Tambah list B dengan nilai string
print()
b.append("11")
print(b)

# Tambah list B dengan 3 nilai
print()
print(b + [12, 13, 14])

# Gabungkan list B dengan list A
print()
print(a + b)

