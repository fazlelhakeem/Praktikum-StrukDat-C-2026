#Contoh Set
myset = {"apple", "banana", "cherry"}
print(myset)

#===Mengakses Item Set
#menggunalan keyword in
thisset = {"apple", "banana", "cherry"}

for x in thisset:
   print(x)

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

#==Menambah Item Set==
#menggunakan method add()
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")
print(thisset)

#menggunakan method update()
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print(thisset)

#==Menghapus Item Set==
#menggunakan method remove() atau discard()
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")
thisset.discard("cherry")
print(thisset)

#menggunakan method pop()
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()
print(x)
print(thisset)

#menggunakan method clear()
thisset = {"apple", "banana", "cherry"}

thisset.clear()
print(thisset)

#menggunakan keyword del
thisset = {"apple", "banana", "cherry"}

del thisset
print(thisset)


#==Operasii Dua Set==
#method union()/ | dan update()
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

#menggunakan method intersection()/ &
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

#menggunakan method difference()/ -
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)

#menggunakan method symmetric_difference()/ ^
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)


#==Frozenset==
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))