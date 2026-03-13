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

def sisipkan_vip(head, plat_baru, plat_target):
   node_now = plat_target

   if node_now.next == None:
      node_now.next = plat_baru
      return head

   plat_baru.next = node_now.next
   node_now.next = plat_baru
   return head

def tampilkan_antrean(head):
   while head:
      print(head.data, end=" ")
      head = head.next

node5 = Node('mobil5')

node1 = sisipkan_vip(node1, node5, node3)
tampilkan_antrean(node1)