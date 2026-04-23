class Node:
  def __init__(self, url):
    self.url = url
    self.next = None

class StackLinkedList:
  def __init__(self):
    self.top = None
    self.count = 0

  def push(self, url):
    new_node = Node(url)
    if self.top:
      new_node.next = self.top
    self.top = new_node
    self.count += 1

  def pop(self):
    if self.isEmpty():
      return "Riwayat kosong"
    popped_node = self.top
    self.top = self.top.next
    self.count -= 1
    return popped_node.url

  def peek(self):
    if self.isEmpty():
      return None
    return self.top.url

  def is_empty(self):
    return self.count == 0

  def stackSize(self):
    return self.count

  def traverseAndPrint(self):
    currentNode = self.top
    while currentNode:
      print(currentNode.url, end=" -> ")
      currentNode = currentNode.next
    print()

riwayat = Stack()
riwayat.push('A')
riwayat.push('B')
riwayat.push('C')

print("LinkedList: ", end="")
riwayat.traverseAndPrint()
print("Peek: ", riwayat.peek())
print("Pop: ", riwayat.pop())
print("LinkedList after Pop: ", end="")
riwayat.traverseAndPrint()
print("isEmpty: ", riwayat.isEmpty())
print("Size: ", riwayat.stackSize())