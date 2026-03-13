class Node:
   def __init__(self, data):
      self.data = data
      self.next = None

node1 = Node('mobil1')
node2 = Node('mobil2')
node3 = Node('mobil3')
node4 = Node('mobil4')

node1.next = node2
node2.next = node3
node3.next = node4

def tambahKendaraan(head, plat):
   head = head
   node_now = head

   while node_now and node_now.next != None:
      node_now = node_now.next

   node_now.next = plat

   return head

def hapusKendaraan(head, plat):
   node_now = head

   while node_now.next and node_now.next != plat:
      node_now = node_now.next

   if node_now is None:
      return head

   node_now.next = node_now.next.next

   return head

node5 = Node('mobil5')

node1 = tambahKendaraan(node1, node5)
node1 = hapusKendaraan(node1, node2)

def tampilkan_antrean(head):
   while head:
      print(head.data, end=" ")
      head = head.next

tampilkan_antrean(node1)