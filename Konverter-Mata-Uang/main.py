from kurs import kurs
from konverter import konversi
from tabulate import tabulate

def cetak_tabel():
   konver = []

   for currency, nilai in kurs.items():
      konver.append([currency, f'{nilai:,}'.replace(',', '.')])

   print("\n=== KONVERTER MATA UANG ===")
   print(tabulate(konver, headers=["Kode", "Kurs"], tablefmt="grid"))

def main():
   cetak_tabel()

   dari = input('Dari (IDR/USD/EUR/SGD/JPY): ').upper()
   ke = input('Ke (IDR/USD/EUR/SGD/JPY): ').upper()
   nilai = int(input('Jumlah: '))

   hasil = konversi(dari, ke, nilai)

   if dari == 'IDR':
      print(f'Rp {nilai:,.0f} = {hasil:.2f} {ke}')
   elif ke == 'IDR':
      print(f'{nilai:.2f} {dari} = Rp {hasil:,.0f}')

if __name__ == '__main__':
   main()
   