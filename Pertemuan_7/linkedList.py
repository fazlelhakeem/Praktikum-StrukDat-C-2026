class Node:
   def __init__(self, data):
      self.data = data
      self.next = None

def nilaiTerendah(angka):
   low = angka.data
   banding = angka.next
   while banding:
      if banding.data < low:
         low = banding.data
      banding = banding.next

   return low

def hapusNode(head, hapus):
   if head == hapus:
      return head.next

   node_now = head
   while node_now != hapus:
      node_now == node_now.next

   node_now.next = node_now.next.next

   return head

def sisip_node(head, tambah, posisi):
   if posisi == 1:
      tambah.next = head
      return tambah

node1 = Node(21)
node2 = Node(34)
node3 = Node(98)
node4 = Node(25)

node1.next = node2
node2.next = node3
node3.next = node4

print(nilaiTerendah(node1))
