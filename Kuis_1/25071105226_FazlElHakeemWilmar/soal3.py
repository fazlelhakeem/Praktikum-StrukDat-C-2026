katalog = [ 
   {'merk': 'Samsung', 'tipe': 'S23', 'sn': 'SAM01', 'stok': 2},
   {'merk': 'Oppo', 'tipe': 'Reno 10', 'sn': 'OPP01', 'stok': 5},
   {'merk': 'Vivo', 'tipe': 'V40', 'sn': 'VIV01', 'stok': 3}
]

merk = []
for i in katalog:
   merk.append(i['merk'])

daftar_merk = set(merk)

def  update_stok(katalog, sn_target, jumlah_tambah):
   for i in katalog:
      if i['sn'] == sn_target:
         i['stok'] += jumlah_tambah

for i in range(3):
   print(f'\nUpdate Stok Ke {i+1}')
   sn = input('masukkan serial number : ')
   tambah = int(input('masukkan jumlah stok tambahan : '))

   update_stok(katalog, sn, tambah)

print('\nDaftar Merk')
for i in daftar_merk:
   print(i)

