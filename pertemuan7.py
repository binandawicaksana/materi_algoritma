# SLide 7
# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1

# # Contoh penggunaan
# data = [10, 23, 45, 70, 11, 15]
# target = 70
# result = linear_search(data, target)
# print("Elemen ditemukan pada indeks:", result)

#Slide 12
# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1

#     return -1

# # Contoh penggunaan
# data = [11, 12, 15, 23, 45, 70]
# target = 15
# result = binary_search(data, target)
# print("Elemen ditemukan pada indeks:", result)

#Slide 13
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

