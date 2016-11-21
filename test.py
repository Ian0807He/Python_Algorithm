from Graph import *

print("Graph:")
g = GraphNode(1,[2,3,4])
print(g.getItem())
print(g.getNextNodes())
for x in g.getNextNodes():
    print(x.getItem())

from DoubleLinkedList import *

print("\n\nDoubleLinkedList:")
# Create A DoubleLinkedList
list = DoubleLinkedList()
list.add(1)
list.add(2)
list.add(3)
list.add(4)
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
list.remove()
e = list.last.getItem()
print(e)

# remove last item
print("Remove the last item again, and print the last item")
list.remove()
f = list.last.getItem()
print(f)


# foreward go through
print("Foreward go through: ", list.foreward())
# backward go through
print("Backward go through: ", list.backward())
# size
print("Size:", list.size)
