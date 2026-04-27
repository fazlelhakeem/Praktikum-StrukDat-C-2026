class Node:
   def __init__(self, nama, keluhan):
      self.nama = nama
      self.keluhan = keluhan
      self.next = None

class AntrianRS:
   def __init__(self):
      self.head = None
      self.tail = None
      self.size = 0

   def enqueue(self, nama, keluhan):
      pasien = Node(nama, keluhan)

      if self.tail is None:
         self.head = self.tail = pasien
         self.head.next = self.tail
      
      else:
         self.tail.next = pasien
         self.tail = pasien
      
      self.size += 1
      print(f'{nama:<7}terdaftar dengan keluhan: {keluhan:<10} (No. Antrian: {self.size})')

   def dequeue(self):
      if self.tail is None:
         print('Antrian kosong')

      hapus = self.head
      self.head = self.head.next
      self.size -= 1

      print(f'Dokter memanggil: {hapus.nama} (keluhan: {hapus.keluhan})')

   def peek(self):
      if self.head is None:
         print('Antrian kosong') 

      print(f'Pasien selanjutnya: {self.head.nama} - {self.head.keluhan}')

   def is_empty(self):
      return self.head is None

   def clear(self):
      self.head = None
      print('\nSesi poliklinik selesai. Antrian dikosongkan')

   def display(self):
      no = 1
      print('\n- ANTRIAN SAAT INI - ')

      current = self.head
      while current:
         print(f'{no} {current.nama:<10}-> {current.keluhan}')
         no += 1
         current = current.next
      
      print()

   def jumlah_antri(self):
      print(f'\nJumlah pasien menunggu: {self.size}')

antri = AntrianRS()

print("""====================================
SISTEM ANTRIAN POLI UMUM
RS Sehat Bersama
====================================""")

print('Antrian Kosong' if antri.is_empty() else 'Antrian berisi')

antri.enqueue('Budi', 'demam tinggi')
antri.enqueue('Ani', 'batuk pilek')
antri.enqueue('Citra', 'sakit kepala')
antri.jumlah_antri()
antri.dequeue()
antri.enqueue('Dodi', 'nyeri perut')
antri.display()
antri.dequeue()
antri.jumlah_antri()
antri.clear()

print('Antrian Kosong' if antri.is_empty() else 'Antrian berisi')
