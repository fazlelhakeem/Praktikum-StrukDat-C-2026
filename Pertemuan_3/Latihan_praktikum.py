class Sempak:
   def __init__(self, merk, harga, ukuran):
      self.merk = merk
      self.harga = harga
      self.ukuran = ukuran

   def print_sempak(self):
      print(f'saya membeli {self.merk} dengan harga {self.harga}')

   def new_harga(self, harga_baru):
      self.harga = harga_baru
      print(f'harga baru {harga_baru}')

crocodile = Sempak('crocodile', 70000, 'l')
agree = Sempak('agree', 45000, 'xl')
champiro = Sempak('champiro', 50000, 'm')

crocodile.print_sempak()

print(agree.harga)

crocodile.new_harga(1000000)