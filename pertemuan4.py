# # slide 3
# matriks = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matriks[0][1])  # Output: 2
# matriks[2][2] = 10
# print(matriks)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 10]]

# # slide 4
# matriks1 = [[1, 2], [3, 4]]
# matriks2 = [[5, 6], [7, 8]]

# hasil = [[matriks1[i][j] + matriks2[i][j] for j in range(2)] for i in range(2)]
# print(hasil)  # Output: [[6, 8], [10, 12]]

# # slide 5
# matriks1 = [[1, 2], [3, 4]]
# matriks2 = [[5, 6], [7, 8]]

# hasil = [[sum(a*b for a, b in zip(matriks1_row, matriks2_col)) for 
#           matriks2_col in zip(*matriks2)] for matriks1_row in matriks1]
# print(hasil)  # Output: [[19, 22], [43, 50]]

# # slide 6
# n = 3
# identitas = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
# print(identitas)
# # Output: [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# # SLide 8

# mahasiswa = {'nama': 'Andi', 'nim': '12345', 'jurusan': 'Informatika'}
# print(mahasiswa['nama'])  # Output: Andi
# mahasiswa['angkatan'] = 2023
# del mahasiswa['nim']
# print(mahasiswa)
# for kunci, nilai in mahasiswa.items():
#     print(f"{kunci}: {nilai}")

# # Slide 9

# mahasiswa = {'nama': 'Andi', 'data': {'nim': '12345', 'jurusan': 'Informatika'}}
# print(mahasiswa['data']['nim'])  # Output: 12345

# # Slide 10

# mahasiswa = {
#     '001': {'nama': 'Andi', 'jurusan': 'Informatika'},
#     '002': {'nama': 'Budi', 'jurusan': 'Sistem Informasi'}
# }

# # Mengakses data
# print(mahasiswa['001']['nama'])  # Output: Andi
# # Menambah data baru
# mahasiswa['003'] = {'nama': 'Citra', 'jurusan': 'Teknik Komputer'}
# print(mahasiswa)

# Slide 11

def tambah_mahasiswa(mahasiswa, nim, nama, jurusan):
    mahasiswa[nim] = {'nama': nama, 'jurusan': jurusan}

def hapus_mahasiswa(mahasiswa, nim):
    if nim in mahasiswa:
        del mahasiswa[nim]

mahasiswa = {}
tambah_mahasiswa(mahasiswa, '001', 'Andi', 'Informatika')
tambah_mahasiswa(mahasiswa, '002', 'Budi', 'Sistem Informasi')
hapus_mahasiswa(mahasiswa, '001')
print(mahasiswa)

