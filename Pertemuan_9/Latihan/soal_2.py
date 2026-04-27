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
         print('[Maju]')

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

   def hapus_kendaraan(self, plat):
      now = self.head

      while now:
         if now.data == plat:
            if now.prev:
               now.prev.next = now.next
            else:
               self.head = now.next

            if now.next:
               now.next.prev = now.prev
            else:
               self.tail = now.prev

            del now
            return
         now = now.next

      print(f'\nplat {plat} tidak ditemukan')

parkir = DoubleLinkedList()

parkir.tambah_kendaraan("B 1111 AA")
parkir.tambah_kendaraan("D 2222 BB")
parkir.tambah_kendaraan("A 3333 CC")
parkir.tambah_kendaraan("B 4444 DD")

print("Sebelum:")
parkir.tampilkan_maju()

parkir.hapus_kendaraan("A 3333 CC")

print("\nSesudah:")
parkir.tampilkan_maju()