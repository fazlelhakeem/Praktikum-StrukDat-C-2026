skema_komisi = ( 
   (100000000, 10), # Penjualan >= 100jt -> Komisi 10% 
   (50000000,  5),  # Penjualan >= 50jt  -> Komisi 5% 
   (20000000,  2),  # Penjualan >= 20jt  -> Komisi 2% 
   (0,         0)   # Di bawah 20jt      -> Tidak ada komisi
) 

def hitung_komisi(total_penjualan, skema, index = 0):
   if index == 3:
      return 0
   elif total_penjualan >= skema[index][0]:
      return int(skema[index][1])
   else:
      index += 1
      return hitung_komisi(total_penjualan, skema, index)

nama = input('Masukkan Nama Sales : ')
total = int(input('Masukkan Total Penjualan : '))

persen = hitung_komisi(total, skema_komisi)
nom_komisi = total * persen / 100

print(f'Nilai komisi {nama} adalah {nom_komisi:.2f}, dengan total penjualan {total}')