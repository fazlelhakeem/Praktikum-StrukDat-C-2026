class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None

class DoubleLinkedList:
   def __init__(self):
      self.head = None
      self.tail = None

   def tambah_kendaraan(self, plat):
      baru = Node(plat)
      
      if not self.head:
         self.head = baru
         self.tail = baru
      else:
         baru.prev = self.tail
         self.tail.next = baru
         self.tail = baru

   def tampilkan_maju(self):
      if not self.head:
         print('\nLinked list kosong')
         return
      else:
         print('\n[Maju]')

         now = self.head
         while now:
            print(now.data)
            now = now.next

   def tampilkan_mundur(self):
      if not self.head:
         print('\nLinked list kosong')
         return
      else:
         print('\n[Mundur]')

         now = self.tail
         while now:
            print(now.data)
            now = now.prev

parkir = DoubleLinkedList()

parkir.tambah_kendaraan("B 1234 ABC")
parkir.tambah_kendaraan("D 5678 XYZ")
parkir.tambah_kendaraan("A 9999 TUV")

parkir.tampilkan_maju()
parkir.tampilkan_mundur()