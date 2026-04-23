stack = []

# Push
stack.append('https://drive.google.com/file/d/1OSVx31ynCOCqx1tYipUCz_64NUHUve6/view')
stack.append('https://drive.google.com/file/d/1GDLgo_AtcqfKKDGmlHj2aOFJDpWyGMDI/view')
stack.append('https://www.w3schools.com/python/python_dsa_stacks.asp')
print("Stack: ", stack)

# Peek
topElement = stack[-1]
print("Peek: ", topElement)

# Pop
poppedElement = stack.pop()
print("Pop: ", poppedElement)

# Stack after Pop
print("Stack after Pop: ", stack)

# isEmpty
isEmpty = not bool(stack)
print("isEmpty: ", isEmpty)

# Size
print("Size: ",len(stack))