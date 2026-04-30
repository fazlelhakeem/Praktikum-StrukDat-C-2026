class Node:
   def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None

class BinaryTree:
   def __init__(self):
      self.root = None

   def insert_root(self, baru):
      if self.root is None:
         new = Node(baru)
         self.root = new

   def insert_left(self, parent, baru):
      new = Node(baru)

      if parent.left is None:
         parent.left =  new
      else:
         new.left = parent.left
         parent.left = new

   def insert_right(self, parent, baru):
      new = Node(baru)

      if parent.right is None:
         parent.right =  new
      else:
         new.right = parent.right
         parent.right = new

def traverse_preorder(now):
   if now is not None:
      print(now.data, end=' - ')
      traverse_preorder(now.left)
      traverse_preorder(now.right)


def traverse_inorder(now):
   if now is not None:
      traverse_inorder(now.left)
      print(now.data, end=' - ')
      traverse_inorder(now.right)


def traverse_postorder(now):
   if now is not None:
      traverse_postorder(now.left)
      traverse_postorder(now.right)
      print(now.data, end=' - ')


def get_leaf_nodes(now):
   if now is None:
      return 
   if now.left is None and now.right is None:
      print(now.data)

   get_leaf_nodes(now.left)
   get_leaf_nodes(now.right)


audit = BinaryTree()

audit.insert_root('A')
audit.insert_left(audit.root, "B")
audit.insert_right(audit.root, "C")

audit.insert_left(audit.root.left, 'D')
audit.insert_right(audit.root.left, 'E')

audit.insert_right(audit.root.right, 'F')


print('''SISTEM AUDIT DISTRIBUSI "CEPAT SAMPAI"
======================================
[INFO] Membangun Struktur Gudang...
[INFO] Struktur berhasil dibuat.
HASIL AUDIT:''')

print('1. Pre-Order   :', end=" ")
traverse_preorder(audit.root)
print()

print('2. In-Order   :', end=" ")
traverse_inorder(audit.root)
print()

print('3. Post-Order   :', end=" ")
traverse_postorder(audit.root)
print()

print('[DATA] Gudang Ujung (Leaf Nodes):')
get_leaf_nodes(audit.root)