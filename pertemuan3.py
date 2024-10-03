# # Slide 5
# my_list = [10, 20, 30, 40, 50]
# print(my_list[0])  # Output: 10
# print(my_list[2])  # Output: 30

# Slide 6
# my_list = [10, 20, 30, 40]
# my_list[2] = 35
# print(my_list)  # Output: [10, 20, 35, 40]

# # # Slide 7
# my_list.append(60)  # Menambah elemen di akhir list
# try :
# my_list.remove(200)
# except ValueError:
    # print('data tidak ada')
      # Menghapus elemen 20
# my_list.insert(2,15) # Menambahkan elemen sesuai index
# my_list.pop(1) # Menghapus elemen berdasarkan index
# print(my_list)

# # Slide 8
# # Program untuk menambahkan elemen pada array (list)
# angka = [1, 2, 3, 4]
# angka.append(5)
# print(angka)  # Output: [1, 2, 3, 4, 5]

# # # Slide 9
# matriks = [[1, 2], [3, 4], [5, 6]]
# print(matriks)
# print(matriks[2][0])  # Output: 2

# # # Slide 10
# matriks[1][1] = 10
# print(matriks)  # Output: [[1, 2], [3, 10], [5, 6]]

# print("--------------------STRING------------------------")

# # Slide 12
# teks = "Hello"
# print(teks[0])  # Output: H
# print(teks[4])  # Output: o

# # Slide 13
# teks = "Hello" + " World"
# print(teks)  # Output: Hello World

# substring = teks[3:8]
# print(substring)  # Output: Hello

# # Slide 14
# teks = "Python"
# print(len(teks))       # Output: 6
# print(teks.upper())    # Output: PYTHON
# print(teks.find('on')) # Output: 2

# # Slide 15
# teks = "Belajar Python"
# print(teks)
# teks_baru = teks.replace("P", "VB")
# print(teks_baru)  # Output: Belajar Pemrograman

# teks = "Rp.100.000"
# print(teks)
# teks_baru = teks.replace(".", "")
# print(teks_baru)  
# # Slide 16
# String
# teks = "Python"
# for huruf in teks:
#     print(huruf)
# # Array
# angka = [1, 2, 3, 4, 5]
# for a in angka:
#     print(a)

# # Slide 17
# kuadrat = [x**2 for x in range(61)]
# print(kuadrat)  # Output: [0, 1, 4, 9, 16, 25]

# # Slide 18
# angka = [3, 5, 7, 9]
# print(max(angka))  # Output: 9
# print(sum(angka))  # Output: 24

# # Slide 19
# angka = [1, 2, 3, 4, 5]
# total = sum(angka)
# rata_rata = total / len(angka)
# print(f"Rata-rata: {rata_rata}")

# # Slide 20
teks = input("Masukkan sebuah teks: ")

vokal = 'aeiouAEIOU'
hitung_vokal = 0

for huruf in teks:
    if huruf in vokal:
        hitung_vokal += 1

print(f"Jumlah huruf vokal: {hitung_vokal}")

