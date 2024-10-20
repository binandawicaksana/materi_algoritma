# Single Linked List
# Slide 9
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Slide 10
class SingleLinkedList:
    def __init__(self):
        self.head = None

    def tambah_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

# Slide 11
# Membuat linked list dan menambah elemen
linked_list = SingleLinkedList()
linked_list.tambah_node(10)
linked_list.tambah_node(20)
linked_list.tambah_node(30)

# Akses elemen pertama
print(linked_list.head.data)  # Output: 10

# Slide 12
def print_list(self):
    current = self.head
    while current:
        print(current.data, end='')
        current = current.next
# print_list(linked_list) # Output: 10 20 30

# Slide 13
def hapus_node(self, data):
    current = self.head
    if current and current.data == data:
        self.head = current.next
        return
    prev = None
    while current and current.data != data:
        prev = current
        current = current.next
    if current is None:
        return
    prev.next = current.next

hapus_node(linked_list,10)
print_list(linked_list)

# Double Linked List
# Slide 15
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None

# # # Slide 16
# class DoubleLinkedList:
#     def __init__(self):
#         self.head = None

#     def tambah_node(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node
#             new_node.prev = current

# # Slide 17
#     def hapus_node(self, data):
#         current = self.head
#         while current and current.data != data:
#             current = current.next
#         if current is None:
#             return
#         if current.prev:
#             current.prev.next = current.next
#         if current.next:
#             current.next.prev = current.prev
#         if current == self.head:
#             self.head = current.next

# # Slide 18
# # Membuat double linked list dan menambah elemen
# dll = DoubleLinkedList()
# dll.tambah_node(10)
# dll.tambah_node(20)
# dll.tambah_node(30)

# # Akses elemen pertama dan terakhir
# print(dll.head.data)  # Output: 10
# print(dll.head.next.prev.data)  # Output: 30
# print(dll.head.prev) 

# DoubleLinkedList.hapus_node(dll,20)

# def print_list(self):
#     current = self.head
#     while current:
#         print(current.data, end=' - ')
#         current = current.next
# print_list(dll) # Output: 10 20 30
