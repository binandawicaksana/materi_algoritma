# Slide 7
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

# # Contoh
# data = [64, 34, 25, 12, 22, 11, 90]
# bubble_sort(data)
# print(data)

# Slide 11

# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_idx = i
#         for j in range(i+1, n):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]

# # Contoh
# data = [64, 25, 12, 22, 11]
# selection_sort(data)
# print(data)


# Slide 15
# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         L = arr[:mid]
#         R = arr[mid:]

#         merge_sort(L)
#         merge_sort(R)

#         i = j = k = 0

#         while i < len(L) and j < len(R):
#             if L[i] < R[j]:
#                 arr[k] = L[i]
#                 i += 1
#             else:
#                 arr[k] = R[j]
#                 j += 1
#             k += 1

#         while i < len(L):
#             arr[k] = L[i]
#             i += 1
#             k += 1

#         while j < len(R):
#             arr[k] = R[j]
#             j += 1
#             k += 1

# # Contoh
# data = [38, 27, 43, 3, 9, 82, 10]
# merge_sort(data)
# print(data)
