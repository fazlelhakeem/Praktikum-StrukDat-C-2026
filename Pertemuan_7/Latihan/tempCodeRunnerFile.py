
node2.next = node3
node3.next = node4

def tambahKendaraan(head, plat):
   head = head
   node_now = head

   while node_now and node_now.next != None:
      node_now = node_now.next

   node_now.next = plat