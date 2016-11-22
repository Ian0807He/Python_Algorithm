from DoubleLinkedList import *

print("DoubleLinkedList:\n")
# Create A DoubleLinkedList
list = DoubleLinkedList()
list.insertEnd(1)
list.insertEnd(2)
list.insertEnd(3)
list.insertEnd(4)
list.insertEnd(2)
list.insertEnd(3)
list.insertEnd(4)
list.insertEnd('a')
list.insertEnd('b')

# Get First item
a = list.head.getItem()
# Get Second item
b = list.head.getNext().getItem()
# Get Last item
c = list.last.getItem()
# Get the item before the last item
d = list.last.getPrev().getItem()
print(a, b, c, d)

# foreward go through
print("Foreward go through: ", list.foreward())
# backward go through
print("Backward go through: ", list.backward())

# size
print("Size:", list.size)

# Search
# Succeed
print("Search number 3 and print the positions")
for num in list.search(3):
    print(num)
# Failed
print("Search number 5")
for num in list.search(5):
    print(num)

# remove last item
print("Remove the last item, and print the last item")
list.removeEnd()
e = list.last.getItem()
print(e)

# remove last item
print("Remove the last item again, and print the last item")
list.removeEnd()
f = list.last.getItem()
print(f)


# foreward go through
print("Foreward go through: ", list.foreward())
# backward go through
print("Backward go through: ", list.backward())
# size
print("Size:", list.size)

print("Insert An item to Head:")
list.insertHead('a')
# foreward go through
print("Foreward go through: ", list.foreward())

print("Remove an item from Head:")
list.removeHead()
# foreward go through
print("Foreward go through: ", list.foreward())

print("Remove 3:")
list.remove(3)
print("Foreward go through: ", list.foreward())

print("Remove 3 again:")
list.remove(3)
print("Foreward go through: ", list.foreward())


# remove all items
print("Remove all items:")
list.removeEnd()
list.removeEnd()
list.removeEnd()
list.removeEnd()
print("Foreward go through: ", list.foreward())
list.removeEnd()
print("Foreward go through: ", list.foreward())
list.removeEnd()
print("Foreward go through: ", list.foreward())
