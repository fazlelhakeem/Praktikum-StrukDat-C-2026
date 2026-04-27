from soal1 import registrasi_gadget
from soal3 import update_stok
from soal4 import hitung_komisi


def main():
   inventaris = []
   katalog = []

   while True:
      print("""=== PyGadget Hub === 
      1. Tambah Gadget 
      2. Daftar Inventaris 
      3. Update Stok 
      4. Cek Komisi 
      5. Keluar """)

      pilih = int(input('Masukkan pilihan : '))

      match pilih:
         case 1 :
            merk = input("\nMasukkan merk gadget : ")
            tipe = input("Masukkan tipe gadget : ")
            harga = float(input('Masukkan harga gadget : Rp. '))
            sn = input('Masukkan serial number : ')

            inventaris.append(registrasi_gadget(merk, tipe, harga, sn))
            katalog.append(inventaris[-1])

         case 2 :
            if len(katalog) == 0:
               print('\nTidak ada gadget dalam katalog')
            else:
               for i in katalog:
                  print()
                  for x, y in i.items():
                     print(f'{x:<5}: {y}')

         case 3 :
            sn = input('masukkan serial number : ')
            tambah = int(input('masukkan jumlah stok tambahan : '))

            update_stok(katalog, sn, tambah)

         case 4 :
            nama = input('Masukkan Nama Sales : ')
            total = int(input('Masukkan Total Penjualan : '))

            persen = hitung_komisi(total, skema_komisi)
            nom_komisi = total * persen / 100

            print(f'Nilai komisi {nama} adalah {nom_komisi:.2f}, dengan total penjualan {total}')

         case 5 :
            break

   print('\nTerima Kasih!!!!!')

if __name__ == '__soal5__':
   main()