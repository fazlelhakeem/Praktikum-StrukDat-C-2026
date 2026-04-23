class Stack:
  def __init__(self):
    self.items = []

  def push(self, element):
    self.items.append(element)

  def pop(self):
    if self.isEmpty():
      return "Riwayat kosong"
    return self.items.pop()

  def peek(self):
    if self.isEmpty():
      return None
    return self.items[-1]

  def is_empty(self):
    return len(self.items) == 0

  def size(self):
    return len(self.items)

# Create a items
riwayat = Stack()

riwayat.push('A')
riwayat.push('B')
riwayat.push('C')

print("Stack: ", riwayat.items)
print("Pop: ", riwayat.pop())
print("Stack after Pop: ", riwayat.items)
print("Peek: ", riwayat.peek())
print("isEmpty: ", riwayat.isEmpty())
print("Size: ", riwayat.size())
