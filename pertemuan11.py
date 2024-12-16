# slide 11
# def count_up_to(max):
#     count = 1
#     while count <= max:
#         yield count  # Menghasilkan angka satu per satu
#         count += 1

# # Menggunakan generator untuk menghitung
# for number in count_up_to(5):
#     print(number)

#Slide 15
# numberslist = [i for i in range(1, 5)]
# print(f"List= {numberslist}")
# totallist = sum(numberslist)
# print(f"Sum List= {totallist}")

# def generate_numbers():
#     for i in range(1, 5):
#         yield i

# numbersgenerate = generate_numbers()
# for number in generate_numbers():
#     print(f"Generate List= {number}")
# totalgenerate = sum(numbersgenerate)
# print(f"Sum List= {totalgenerate}")

#Slide 18
# import time
# start_time_list = time.time()
# numberslist = [i for i in range(1, 100)]
# # print(f"List= {numberslist}")
# totallist = sum(numberslist)
# print(f"Sum List= {totallist}")
# end_time_list = time.time()
# print(f"Time build List= {end_time_list - start_time_list} second")


# start_time_generate = time.time()
# def generate_numbers():
#     for i in range(1, 100):
#         yield i

# numbersgenerate = generate_numbers()
# # for number in generate_numbers():
# #     print(f"Generate List= {number}")
# totalgenerate = sum(numbersgenerate)
# print(f"Sum List= {totalgenerate}")
# end_time_generate= time.time()
# print(f"Time build List= {end_time_generate - start_time_generate} second")

#Slide 19
import time
import sys
start_time_list = time.time()
numberslist = [i for i in range(1, 100)]
# print(f"List= {numberslist}")
totallist = sum(numberslist)
print(f"Sum List= {totallist}")
end_time_list = time.time()
print(f"Time build List= {end_time_list - start_time_list} second")
print(f"Size of List: {sys.getsizeof(numberslist)} bytes")


start_time_generate = time.time()
def generate_numbers():
    for i in range(1, 100):
        yield i

numbersgenerate = generate_numbers()
# for number in generate_numbers():
#     print(f"Generate List= {number}")
totalgenerate = sum(numbersgenerate)
print(f"Sum List= {totalgenerate}")
end_time_generate= time.time()
print(f"Time build List= {end_time_generate - start_time_generate} second")
print(f"Size of Generate: {sys.getsizeof(numbersgenerate)} bytes")
