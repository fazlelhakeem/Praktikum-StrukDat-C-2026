#Contoh List
thislist = ["apple", "banana", "cherry"]
print(thislist)

#==Mengakses Elemen List==
#menggunakan indeks
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#==Mengubah Nilai Item==
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#menggunakan method insert()
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#==Menambah Item List==
#menggunakan method append()
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#menggunakan method insert
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#menggabungkan dua list dengan method extend()
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


#==Menghapus Elemen List==
#menggunakan method remove()
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#menggunakan method pop()
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#menggunakan keyword del
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#menggunakan method clear()
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


#==Mengurutkan Elemen List
#menggunakan method sort
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#menggabungkan list
#dengan operator +
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#menggunakan method append()
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#menggunakan method extend()
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)