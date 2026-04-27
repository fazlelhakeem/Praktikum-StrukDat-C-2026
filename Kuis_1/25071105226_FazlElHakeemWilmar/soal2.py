stok_gadget = [ 
   {'merk': 'Samsung', 'tipe': 'S23', 'harga': 12000000}, 
   {'merk': 'Oppo', 'tipe': 'Reno 10', 'harga': 6000000}, 
   {'merk': 'Xiaomi', 'tipe': 'Mi 13', 'harga': 10000000}, 
   {'merk': 'Iphone', 'tipe': '15 Pro', 'harga': 20000000}, 
] 

def filter_harga(data, min_harga, max_harga):
   hasil = []

   for i in data:
      if i['harga'] >= min_harga and i['harga'] <= max_harga:
         hasil.append(i)

   return hasil

atas = int(input('Masukkan batas atas harga barang :  Rp. '))
bawah = int(input('Masukkan batas bawah harga barang :  Rp. '))

new_data = filter_harga(stok_gadget, bawah, atas)

if len(new_data) == 0:
   print('\nTidak ada gadget dalam rentang harga tersebut')
else:
   for i in new_data:
      print()
      for x, y in i.items():
         print(f'{x} : {y}')