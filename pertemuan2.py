# Prosedural

# def penjumlahan(a, b):
#     return a + b

# hasil = penjumlahan(8, 9)
# print(hasil)

# Berorientasi Objek

# class PersegiPanjang:
#     def __init__(self, panjang, lebar):
#         self.panjang = panjang
#         self.lebar = lebar

#     def luas(self):
#         return self.panjang * self.lebar

# persegi = PersegiPanjang(5, 3)
# print(persegi.luas())

# Fungsional

# def kali_dua(x):
#     return x * 2

# angka = [1, 2, 3, 4]
# hasil = list(map(kali_dua, angka))
# print(hasil)

# Algoritma Menemukan Bilangan Terbesar dalam Python

# def terbesar(a, b):
#     if a > b:
#         return a
#     else:
#         return b

# bilangan1 = int(input("Masukkan bilangan pertama: "))
# bilangan2 = int(input("Masukkan bilangan kedua: "))

# hasil = terbesar(bilangan1, bilangan2)
# print(f"Bilangan terbesar adalah {hasil} dari angka {bilangan1} dan {bilangan2}")

# Bubble Sort

def bubble_sort(arr):
    n = len(arr)
    print(angka)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] # 64,34,64
                print(f"Proses ke {i} dan {j} adalah {angka}")

angka = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(angka)
print("List setelah diurutkan:", angka)
