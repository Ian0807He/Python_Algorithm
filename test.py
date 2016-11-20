from DoubleLinkedList import *

list = DoubleLinkedList()
list.add(1)
list.add(2)
list.add(3)
list.add(4)
list.add('a')
list.add('b')

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
print(list.foreward())
# backward go through
print(list.backward())

# remove last item
list.remove()
e = list.last.getItem()
print(e)

# remove last item
list.remove()
f = list.last.getItem()
print(f)

# foreward go through
print(list.foreward())
# backward go through
print(list.backward())
