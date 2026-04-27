def registrasi_gadget(merk, tipe, harga, sn):
   if harga <= 1000000:
      print('\nHarga harus di atas 1.000.000')
      return None
   elif len(sn) < 5:
      print('\nSerial number minimal 5 karakter')
      return None

   return dict({'merk':merk, 'tipe':tipe, 'harga':harga, 'sn':sn, 'status':'Tersedia'})

inventaris = []

for i in range(3):
   merk = input("\nMasukkan merk gadget : ")
   tipe = input("Masukkan tipe gadget : ")
   harga = float(input('Masukkan harga gadget : Rp. '))
   sn = input('Masukkan serial number : ')

   inventaris.append(registrasi_gadget(merk, tipe, harga, sn))

for item in inventaris:
   print('\n')
   for x, y in item.items():
      print(f'{x} : {y}')