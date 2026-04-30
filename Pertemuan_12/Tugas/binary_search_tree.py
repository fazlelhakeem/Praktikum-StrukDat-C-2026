class Node:
   def __init__(self, id_buku, judul):
      self.id_buku = id_buku
      self.judul = judul
      self.left = None
      self.right = None

def insert(now, id_buku, judul):
   baru = Node(id_buku, judul)

   if now is None:
      return baru
   else:
      if baru.id_buku < now.id_buku:
         now.left = insert(now.left, id_buku, judul)
      elif baru.id_buku > now.id_buku:
         now.right = insert(now.right, id_buku, judul)
   
   return now

def search(now, cari_id):
   if now is None:
      return False
   elif cari_id == now.id_buku:
      return now.judul
   elif cari_id < now.id_buku:
      return search(now.left, cari_id)
   else:
      return search(now.right, cari_id)
   

def traverse_inorder(now):
   if now is None:
      return

   traverse_inorder(now.left)
   print(f'ID: {now.id_buku}, Judul: "{now.judul}"')
   traverse_inorder(now.right)

def get_min(now):
   while now.left:
      now = now.left

   return now.id_buku

def get_max(now):
   while now.right:
      now = now.right

   return now.id_buku

def height(now):
   if now is None:
      return 0

   else:
      kiri = height(now.left)
      kanan = height(now.right)

      return max(kiri, kanan) + 1

print('''SISTEM KATALOG PERPUSTAKAAN "ILMU TERANG"
=========================================''')
#menambahkan data ke dalam katalog
perpus = Node(50, 'Dasar Pemrograman')
print('Berhasil memasukkan: ID 50 - Dasar Pemrograman')

perpus = insert(perpus, 30, 'Struktur Data')
print('Berhasil memasukkan: ID 30 - Struktur Data')

perpus = insert(perpus, 70, 'Kecerdasan Buatan')
print('Berhasil memasukkan: ID 70 - Kecerdasan Buatan')

perpus = insert(perpus, 20, 'Matematika Diskrit')
print('Berhasil memasukkan: ID 20 - Matematika Diskrit')

perpus = insert(perpus, 40, 'Basis Data')
print('Berhasil memasukkan: ID 40 - Basis Data')

perpus = insert(perpus, 60, 'Jaringan Komputer')
print('Berhasil memasukkan: ID 60 - Jaringan Komputer')

perpus = insert(perpus, 80, 'Sistem Operasi')
print('Berhasil memasukkan: ID 80 - Sistem Informasi')

#menampilkan koleksi buku (inorder)
print('\nKoleksi buku (in-order traversal):')
traverse_inorder(perpus)

#mencari buku berdasarkan ID
print('\nMencari ID 60...', end=" ")
print(f'ditemukan! judul: {search(perpus, 60)}' if search(perpus, 60) else 'data tidak ditemukan')

print('Mencari ID 100...', end=" ")
print(f'ditemukan {search(perpus, 100)}' if search(perpus, 100) else 'data tidak ditemukan')

#menampilkan ID terbesar & terkecil
print(f'\nID Terkecil: {get_min(perpus)}')
print(f'ID Terbesar: {get_max(perpus)}')

#menampilkan tinggi tree
print(f'Tinggi (height) Tree: {height(perpus)-1}')
print('=========================================')
print('Simulasi Selesai!')
