class Node:
   def __init__(self, data):
      self.data = data
      self.next = None

class CircularLinkedList:
   def __init__(self):
      self.head = None
      self.tail = None

   def tambah_petugas(self, nama):
      tambah = Node(nama)

      if not self.head:
         self.head = tambah
         self.tail = tambah
         self.tail.next = self.head

      else:
         self.tail.next = tambah
         self.tail = tambah
         self.tail.next = self.head

   def giliran_berikutnya(self, n):
      if not self.head:
         print('\nLinked list kosong')

      else:
         now = self.head
         giliran = 1

         while giliran <= n:
            print(f'Giliran {giliran}: {now.data}')
            now = now.next
            giliran += 1

petugas = CircularLinkedList()

petugas.tambah_petugas('Andi')
petugas.tambah_petugas('Budi')
petugas.tambah_petugas('Citra')
petugas.tambah_petugas('Dewi')

petugas.giliran_berikutnya(6)