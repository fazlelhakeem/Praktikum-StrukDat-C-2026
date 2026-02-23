#membuat sebuah class
class MyClass:
   x = 5

#membuat beberapa object dengan class yang sudah dibuat
p1 = MyClass
p2 = MyClass
p3 = MyClass
print(p1.x)
print(p2.x)
print(p3.x)

#membuat class tanpa isi (dengan statement pass)
class World:
   pass

#membuat class dengan method __init__()
class Person:
   def __init__(self, name, age = 18):
      self.name = name
      self.age = age 

p1 = Person('Emil', 36)
p2 = Person('Tobias')

print(p1.name, p1.age)
print(p2.name, p2.age)

#mengganti nama parameter self dengan yang lain (tidak disarankan)
class Food:
   def __init__(eat, taste):
      eat.taste = taste

f1 = Food('spicy')
print(f1.taste)

#mengakses properti menggunakan method di dalam class
class Car:
   def __init__(self, brand, model, year):
      self.brand = brand
      self.model = model
      self.year = year

   def display_info(self):
      print(f'{self.year} {self.brand} {self.model}')

car1 = Car('Toyota', 'Corolla', 2020)
car1.display_info()

#membuat class property
class Person:
   species = 'human'

   def __init__(self, name):
      self.name = name

p1 = Person('Emil')
p2 = Person('Tobias')

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)

#method __str__()
class Person:
   def __init__(self, name, age):
      self.name = name
      self.age = age

   def __str__(self):
      return f'{self.name} {self.age}'

p4 = Person('Wahyu', 17)
print(p4)