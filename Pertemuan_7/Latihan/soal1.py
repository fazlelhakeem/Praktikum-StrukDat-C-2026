arr = ["B 1234 ABC", "D 8888 XYZ", "A 111 TUV", "B 2022 EFG"]

def pisah_ganjil(arr):
   ganjil = []

   for i in arr:
      if int(i[-5]) % 2 != 0:
         ganjil.append(i)
   
   return ganjil

def pisah_genap(arr):
   genap = []

   for i in arr:
      if int(i[-5]) % 2 == 0:
         genap.append(i)

   return genap

plat_ganjil = pisah_ganjil(arr)
plat_genap = pisah_genap(arr)

print(plat_ganjil)
print(plat_genap)