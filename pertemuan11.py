# #SLIDE 7
# import sys

# # Membuat objek baru
# a = [1, 2, 3]
# print("Referensi awal:", sys.getrefcount(a))  
# # Output: 2 (default 1 + referensi variabel a)

# # Menambah referensi
# b = a
# print("Referensi setelah b = a:", sys.getrefcount(a))  
# # Output: 3

# # Menghapus referensi
# del b
# print("Referensi setelah del b:", sys.getrefcount(a))  
# # Output: 2

# # SLIDE 10
# import gc

# # Membuat siklus referensi
# a = []
# b = [a]
# a.append(b)

# # Menghapus referensi
# del a, b

# # Memanggil garbage collector
# gc.collect()
# print("Garbage Collection selesai")

# # SLIDE 14
# import weakref

# class Dict(dict):
#     pass

# obj = Dict(red=1, green=2, blue=3) 
# weak_obj = weakref.ref(obj)
# print(weak_obj())  # Mengakses objek menggunakan referensi lemah
# del obj
# print(weak_obj())  # None (objek sudah dihapus)

# # Slide 19
# # Menggunakan List
# nums = [i for i in range(1000000)]
# print(sum(nums))  # Menggunakan banyak memori

# # Menggunakan Generator
# def generate_numbers():
#     for i in range(1000000):
#         yield i

# print(sum(generate_numbers()))  # Memori lebih hemat

# #SLIDE 20
# import sys
# import tracemalloc

# a = [1, 2, 3]
# print("Ukuran objek:", sys.getsizeof(a), "bytes")

# tracemalloc.start()
# a = [i for i in range(100000)]
# print("Penggunaan memori saat ini:", tracemalloc.get_traced_memory())
# tracemalloc.stop()

#SLIDE 21

# import sys
# import tracemalloc
# tracemalloc.start()
# def read_large_file(file_path):
#     with open(file_path) as file:
#         for line in file:
#             yield line.strip()

# for line in read_large_file("pertemuan9.py"):
#     print(line)

# listfile = [f for f in read_large_file("pertemuan9.py")]

# print("Ukuran objek file menggunakan generator:", sys.getsizeof(line), "bytes")
# print("Ukuran objek file menggunakan list:", sys.getsizeof(listfile), "bytes")
# print("Penggunaan memori saat ini:", tracemalloc.get_traced_memory())
# tracemalloc.stop()

