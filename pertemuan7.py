# SLide 7
# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i+1
#     return -1
#     # return 'Tidak ditemukan'


# # Contoh penggunaan
# data = [10, 23, 45, 70, 11, 15]
# # target = 70
# print(f"data = {data}")
# target = int(input("Masukan nilai yang ingin dicari?:"))
# # target2 = int(input("Masukan nilai ke 2 yang ingin dicari?:"))
# result = linear_search(data, target)
# # result2 = linear_search(data, target2)
# # hasil = []
# # hasil.append(result)
# # hasil.append(result2)

# # print("Elemen ditemukan pada indeks:", result)
# # print("Pencarian ke 1 ditemukan pada urutan data ke:", result)
# # print("Pencarian ke 2 ditemukan pada urutan data ke:", result2)
# print("Pencarian ditemukan pada urutan data ke:", result)




# Slide 12
# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2
#         print(f"low = {low}")
#         print(f"mid = {mid}")
#         print(f"high = {high}")

#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1

#     return -1

# # Contoh penggunaan
# data = [11, 12, 15, 23, 45, 70]
# target = 45
# print(f"data = {data}")
# result = binary_search(data, target)
# print("Elemen ditemukan pada indeks:", result)

#Slide 13 rekursi adalah metode untuk memanggil dirinya sendiri
def binary_search_recursive(arr, low, high, target):
    if high >= low:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_recursive(arr, mid + 1, high, target)
        else:
            return binary_search_recursive(arr, low, mid - 1, target)
    else:
        return -1
# Contoh penggunaan
data = [11, 12, 15, 23, 45, 70]
target = 45
result = binary_search_recursive(data, 0, len(data) - 1, target)
print("Elemen ditemukan pada indeks:", result)

