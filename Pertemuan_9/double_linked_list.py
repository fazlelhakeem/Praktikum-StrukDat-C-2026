class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None

class DoubleLinkedList:
   def __init__(self):
      self.head = None
      self.tail = None

   def tambah_akhir(self, tambah):
      baru = Node(tambah)
      
      if not self.head:
         self.head = baru
         self.tail = baru

      else:
         self.tail.next = baru
         baru.prev = self.tail
         self.tail = baru

   def insert_after(self, after, tambah):
      baru = Node(tambah)

      if not self.head:
         print('\nDouble Linked List kosong')
         return
      
      else:
         now = self.head

         while now and now.data != after:
            now = now.next

         if not now:
            print(f'\nTidak bisa menambahkan {tambah} karena {after} tidak ada')
         else:
            baru.next = now.next
            baru.prev = now
            
            if now.next:
               now.next.prev = baru
               
            now.next = baru

            if now == self.tail:
               self.tail = baru

   def hapus(self, hapus):
      now = self.head

      while now:
         if now.data == hapus:
            if not now.prev:
               self.head = now.next
               self.head.prev = None

            elif not now.next:
               self.tail = now.prev
               self.tail.next = None

            else:
               now.prev.next = now.next
               now.next.prev = now.prev
            
            del now
            return
         now = now.next

      print(f'\n{hapus} tidak ditemukan')

   def tampilkan(self, mundur = False):
      if not self.head:
         print('\nDouble Linked List kosong')
         return

      elif not mundur:
         now = self.head
         print('\n= MAJU =')
         
         while now:
            print(f'- {now.data} -')
            now = now.next

      else:
         now = self.tail
         print('\n= MUNDUR =')

         while now:
            print(f'- {now.data} -')
            now = now.prev


double = DoubleLinkedList()

double.tambah_akhir(1)
double.tambah_akhir(2)
double.tambah_akhir(3)
double.tambah_akhir(4)
double.tambah_akhir(5)
double.tambah_akhir(6)
double.tambah_akhir(7)
double.tampilkan()

double.hapus(1)
double.hapus(7)
double.hapus(4)
double.hapus(7)
double.tampilkan()

double.insert_after(3, 4)
double.insert_after(6, 7)
double.tampilkan()

double.tampilkan(mundur = True)

      







