class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None

class Circular_Single_linked_list:
   def __init__(self):
      self.head = None

   def tambah_akhir(self, tambah):  #menambah data di akhir linked list
      baru = Node(tambah)

      if not self.head:
         self.head = baru
         self.head.next = self.head

      else:
         current = self.head
         while True:
            current = current.next
            if current.next == self.head:
               break

         baru.next = self.head
         current.next = baru

   def delete(self, data):  # Menghapus node berdasarkan data
      if not self.head:
         return

      current = self.head

      while True:
         if current.data == data:
            if current == self.head and current.next == self.head:
               self.head = None

            elif current == self.head:
               last = self.head

               while last.next != self.head:
                  prev = last
                  last = last.next

               self.head = self.head.next
               last.next = self.head

            else:
               prev.next = current.next
               return

         prev = current
         current = current.next

         if current == self.head:
            break

   def display(self):
      if not self.head:
         print('Linked List Kosong!!!')
         return

      print('\n== Circular Single Linked List ==')
      current = self.head
      while True:
         print(current.data)

         if current.next == self.head:
            break

         current = current.next

ll = Circular_Single_linked_list()

ll.tambah_akhir(1)
ll.tambah_akhir(2)
ll.tambah_akhir(3)
ll.tambah_akhir(4)
ll.tambah_akhir(5)

ll.delete(2)
ll.delete(4)

ll.display()