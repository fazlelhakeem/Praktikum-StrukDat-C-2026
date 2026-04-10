pengunjung_hari_ini = [ 
   {"id": "M001", "nama": "Rina",   "usia": 20, "kategori": "Fiksi", "kembali": False}, 
   {"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains", "kembali": True}, 
   {"id": "M003", "nama": "Siti",   "usia": 19, "kategori": "Fiksi", "kembali": False}, 
   {"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum", "kembali": True}, 
   {"id": "M005", "nama": "Yuni",   "usia": 18, "kategori": "Sains", "kembali": False}, 
   {"id": "M006", "nama": "Bagas",  "usia": 22, "kategori": "Hukum", "kembali": False}, 
]

#SOAL 1
def tampilakn_pengunjung():
   print('== DATA PENGUNJUNG PERPUSTAKAAN ==')
   print('No |  ID  |   Nama   | Usia |  Kategori  | Status Kembali')
   print('-----------------------------------------------------------')
   for i in range(len(pengunjung_hari_ini)):
      print(f'{i+1}  | {pengunjung_hari_ini[i]['id']:<5}| {pengunjung_hari_ini[i]['nama']:<9}|  {pengunjung_hari_ini[i]['usia']:<4}| {pengunjung_hari_ini[i]['kategori']:<11}| {'Sudah Kembali' if pengunjung_hari_ini[i]['kembali'] == True else 'Belum Kembali'}')

def filter_belum_kembali():
   belum_kembali = [x['nama'] for x in pengunjung_hari_ini if x['kembali'] == False]

   for i in range(len(belum_kembali)-1):
      for j in range(len(belum_kembali)-1-i):
         if belum_kembali[j] > belum_kembali[j+1]:
            belum_kembali[j], belum_kembali[j+1] = belum_kembali[j+1], belum_kembali[j]

   print('\n== PENGUNJUNG BELUM KEMBALI ==')
   total_belum_kembali = 0
   for i in range(len(belum_kembali)):
      print(f'{i+1}. {belum_kembali[i]}')
      total_belum_kembali += 1
   print(f'Total belum kembali: {total_belum_kembali} pengunjung')

tampilakn_pengunjung()
filter_belum_kembali()


#SOAL 2
def info_perpustakaan():
   info = ('Perpustakaan Kampus Terpadu', 'Jl. Pendidikan No. 5, Pekanbaru', '0761-54321')

   print('\nInfo Perpustakaan:')
   print(f'Nama   : {info[0]}')
   print(f'Alamat : {info[1]}')
   print(f'Telp   : {info[2]}')


def rekap_kategori():
   kategori_buku_unik = set([x['kategori'] for x in pengunjung_hari_ini])

   print(f'\nKategori buku unik: {kategori_buku_unik}')
   print(f'Jumlah kategori: {len(kategori_buku_unik)}')

   data_frekuensi_pengunjung = {}

   for i in (pengunjung_hari_ini):
      if i['kategori'] in data_frekuensi_pengunjung:
         data_frekuensi_pengunjung[i['kategori']] += 1
      else:
         data_frekuensi_pengunjung[i['kategori']] = 1
   

   print('\nRekap per kategori:')
   for i, j in data_frekuensi_pengunjung.items():
      print(f'{i:<7} : {j} pengunjung')

   maks_frekuensi  = max([i for i in data_frekuensi_pengunjung.values()])

   kategori_terbanyak = [i for i in data_frekuensi_pengunjung.keys() if data_frekuensi_pengunjung.get(i) == maks_frekuensi]

   print(f'\nKategori terbanyak: {kategori_terbanyak} ({maks_frekuensi} pengunjung)\n')

info_perpustakaan()
rekap_kategori()

#SOAL 3
class Pengunjung:
   total_pengunjung = 0

   def __init__(self, id, nama, kategori):
      self.__id = id
      self.__nama = nama
      self.__kategori = kategori
      Pengunjung.total_pengunjung +=1

   def get_id(self):
      return self.__id

   def get_nama(self):
      return self.__nama

   def get_kategori(self):
      return self.__kategori

   def tampilkan_info(self):
      print(f'ID        : {self.get_id()}')
      print(f'Nama      : {self.get_nama()}')
      print(f'Kategori  : {self.get_kategori()}\n')

   @staticmethod
   def hitung_pengunjung():
      return Pengunjung.total_pengunjung

class PengunjungPrioritas(Pengunjung):
   def __init__(self, id, nama, kategori, prioritas):
      super().__init__(id, nama, kategori)
      self.prioritas = prioritas

   def tampilkan_info(self):
      print(f'ID        : {self.get_id()}')
      print(f'Nama      : {self.get_nama()}')
      print(f'Kategori  : {self.get_kategori()}')
      print(f'Prioritas : {self.prioritas}')

      if self.prioritas == 'Mendesak':
         print('** Layani Segera!! **')

tamu1 = Pengunjung('M001', 'Rina', 'Fiksi')
tamu2 = PengunjungPrioritas('M007', 'Gilang', 'Referensi', 'Mendesak')

tamu1.tampilkan_info()
tamu2.tampilkan_info()
print(f'\nTotal pengunjung terdaftar: {Pengunjung.hitung_pengunjung()}')

#SOAL 4
class Node:
   def __init__(self, data):
      self.data = data
      self.next = None

class AntrianPeminjaman:
   def __init__(self):
      self.head = None

   def tambah(self, data):
      tambah = Node(data)

      if not self.head:
         self.head = tambah
         return

      node_now = self.head
      while node_now.next:
         node_now = node_now.next
      
      node_now.next = tambah

   def tampilkan(self):
      node_now = self.head

      print('\n===== ANTRIAN PEMINJAMAN ======')
      urutan = 0

      while node_now:
         print(f'[{urutan+1}] {node_now.data['id']} - {node_now.data['nama']:<8}| {node_now.data['kategori']}')
         urutan += 1
         node_now = node_now.next
      print(f'Total antrian: {urutan}')

   def panggil_berikutnya(self):
      print('\nMemanggil pengunjung berikutnya...')
      print(f'Silahkan masuk: {self.head.data['nama']} ({self.head.data['id']}) - {self.head.data['kategori']}')

      self.head = self.head.next

   def cari(self, nama):
      node_now = self.head
      posisi = 1
      print(f'\nMencari "{nama}"...')

      while node_now:
         if node_now.data['nama'] == nama:
            print(f'Ditemukan: {node_now.data['id']} - {node_now.data['nama']} | {node_now.data['kategori']} (posisi ke-{posisi})')
            return
         node_now = node_now.next
         
         posisi += 1

      print('\nNama Tidak Ditemukan!!!')

   def hapus_berdasarkan_id(self, id):
      print(f'\nMenghapus pengunjung dengan ID {id}')

      #kalau pengunjung di posisi 1
      if self.head.data['id'] == id:
         self.head = self.haed.next
         print(f'{self.head.data['nama']} ({self.head.data['id']}) berhasil dihapus dari antrian.')
         return

      #kalau di posisi tengah atau akhir
      node_now = self.head
      while node_now.next and node_now.next.data['id'] != id:
         node_now = node_now.next

      #kalau gk ada
      if node_now.next == None:
         print('\nData tidak ditemukan!!!')
         return

      node_now.next = node_now.next.next
      print(f'{self.head.data['nama']} ({self.head.data['id']}) berhasil dihapus dari antrian.')

   def hitung(self):
      total = 0

      node_now = self.head
      while node_now:
         node_now = node_now.next
         total += 1

      return total

antrian = AntrianPeminjaman()
antrian.tambah({"id": "M001", "nama": "Rina",   "kategori": "Fiksi"}) 
antrian.tambah({"id": "M002", "nama": "Hendra", "kategori": "Sains"}) 
antrian.tambah({"id": "M003", "nama": "Siti",   "kategori": "Fiksi"}) 
antrian.tambah({"id": "M004", "nama": "Taufik", "kategori": "Hukum"}) 
 
antrian.tampilkan() 
antrian.panggil_berikutnya() 
antrian.tampilkan() 
antrian.hapus_berdasarkan_id("M003") 
antrian.tampilkan() 
antrian.cari("Taufik") 
print("Total antrian:", antrian.hitung()) 