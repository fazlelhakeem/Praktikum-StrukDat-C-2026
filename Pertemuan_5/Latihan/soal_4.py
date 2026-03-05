gudang_pc = [ 
{"item": "Monitor", "harga": 1500000, "stok": 5}, 
{"item": "Keyboard", "harga": 400000, "stok": 12}, 
{"item": "Mouse", "harga": 250000, "stok": 20} 
]

# a 
tambah = {"kategori" : "Aksesoris"}
gudang_pc[1].update(tambah)

# b 
new = {
   'item' : 'Headset',
   'harga' : 350000,
   'stok' : 8
}
gudang_pc.append(new)

# c 
for i in gudang_pc:
   aset = i['harga'] * i['stok']

   print(f'Item : {i['item']} | Total Aset : Rp {aset}')