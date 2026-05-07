class Graph:
   def __init__(self):
      self.graph = {}

   def tambah_kota(self, nama):
      if nama not in self.graph:
         self.graph[nama] = []

   def tambah_jalan(self, u, v, jarak):
      if u in self.graph:
         self.graph[u].append((v, jarak))
         self.graph[v].append((u, jarak))
         print(f'Menambahkan jalan: {u} - {v} ({jarak} km)')

   def tampilkan_graph(self):
      print()
      for kota, jalan in self.graph.items():
         print(f'- {kota} terhubung ke:', end=' ')

         for tujuan, jarak in jalan:
            print(f'{tujuan} ({jarak} km)', end=', ')

         print()

   def dijksra(self, kota_asal):
      jarak = {kota: float('inf') for kota in self.graph.keys()}
      jarak[kota_asal] = 0
      visited = []

      print(f'\nMenghitung rute terdekat dari: {kota_asal}...')

      while len(visited) < len(self.graph):
         kota_skrng = None
         jarak_terdekat = float('inf')

         for kota in self.graph.keys():
            if kota not in visited and jarak[kota] < jarak_terdekat:
               kota_skrng = kota
               jarak_terdekat = jarak[kota]

         if kota_skrng is None:
            break

         visited.append(kota_skrng)

         for tetangga, jarak_tetangga in self.graph[kota_skrng]:
            jarak_new = jarak[kota_skrng] + jarak_tetangga

            if jarak_new < jarak[tetangga]:
               jarak[tetangga] = jarak_new
      
      return bubble_sort(list(jarak.items()))[1:]

def bubble_sort(data):
   n = len(data)
   for i in range(n-1):
      for j in range(0, n-i-1):
         if data[j][1] > data[j+1][1]:
            data[j], data[j+1] = data[j+1], data[j]
   return data

grp = Graph()

grp.tambah_kota('Jakarta')
grp.tambah_kota('Bandung')
grp.tambah_kota('Cirebon')
grp.tambah_kota('Semarang')
grp.tambah_kota('Tasikmalaya')

print('SISTEM NAVIGASI LOGISTIK "KILAT MAJU"')
print('=========================================\n')

grp.tambah_jalan('Jakarta', 'Bandung', 150)
grp.tambah_jalan('Jakarta', 'Cirebon', 200)
grp.tambah_jalan('Bandung', 'Tasikmalaya', 100)
grp.tambah_jalan('Bandung', 'Cirebon', 130)
grp.tambah_jalan('Cirebon', 'Semarang', 250)
grp.tambah_jalan('Tasikmalaya', 'Semarang', 200)

grp.tampilkan_graph()

jarak_jakarta = grp.dijksra('Jakarta')
print('\nJarak terpendek dari Jakarta:')
i = 1
for kota, jarak in jarak_jakarta:
   print(f'{i}. Ke {kota}: {jarak} km')
   i += 1

print('\n=========================================')
print('Simulasi Navigasi Selesai!')