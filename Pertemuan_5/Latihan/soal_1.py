stok_barang = [15, 40, 30, 10, 25]

# a 
index = stok_barang.index(10)
stok_barang[index] = 50

# b 
stok_barang.append(5)
stok_barang.sort(reverse=True)

# c 
print(sum(stok_barang))

# d 
avg = sum(stok_barang) / len(stok_barang)
print("Stok Aman") if avg > 20 else print('Waspada')