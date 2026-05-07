class HashTable:
   def __init__(self):
      self.size = 10
      self.table = [[] for _ in range(self.size)]

   def hash_function(self, key):
      total = 0

      for char in str(key):
         total += ord(char)

      return total % self.size

   def insert(self, kode, judul):
      index = self.hash_function(kode)
      bucket = self.table[index]

      for i, (k, j) in enumerate(bucket):
         if k == kode:
            bucket[i] = (kode, judul)
            print(f'Buku dengan kode: {kode} berhasil di-update')
            return

      bucket.append((kode, judul))
      print(f'Buku dengan kode: {kode} dan judul: {judul} berhasil ditambahkan')

   def search(self, kode):
      index = self.hash_function(kode)
      bucket = self.table[index]

      for k, j in bucket:
         if k == kode:
            print(f'kode {k} ditemukan. judul: {j}')
            return

      print('Buku tidak ditemukan')


   def delete(self, kode):
      index = self.hash_function(kode)
      bucket = self.table[index]

      for i, (k, j) in enumerate(bucket):
         if k == kode:
            del bucket[i]
            print(f'Buku dengan kode: {kode} berhasil dihapus')
            return

      print(f'kode {kode} tidak ditemukan')

   def display(self):
      print("\n===== DATA BUKU PERPUSTAKAAN =====")

      for index, bucket in enumerate(self.table):
         print(f"Index {index}: {bucket}")

      print("==========================\n")


perpus = HashTable()

perpus.insert('BK111', 'Mahir C++ Dalam Satu Jam')
perpus.insert('BK222', 'Python Dasar')
perpus.insert('BK333', 'Matematika Diskrit')
perpus.insert('BK444', 'Atomic Habits')
perpus.display()

perpus.insert('BK045', 'Mein Kampf')
perpus.insert('BK111', 'Bumi Manusia')
perpus.display()

perpus.search('BK444')
perpus.search('BK892')

perpus.delete('BK333')
perpus.display()
