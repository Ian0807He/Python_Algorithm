from DoubleLinkedList import *

print("DoubleLinkedList:\n")
# Create A DoubleLinkedList
list = DoubleLinkedList()
list.insert(1)
list.insert(2)
list.insert(3)
list.insert(4)
list.insert(2)
list.insert(3)
list.insert(4)
list.insert('a')
list.insert('b')

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

from BinaryTree import *

print("\n\nBinaryTree:\n")
r = BinaryTree()
r1 = BinaryTree()
r1.makeTree(1,None,None)
r2 = BinaryTree()
r2.makeTree(2,r1,None)
r3 = BinaryTree()
r3.makeTree(3,None,None)
r4 = BinaryTree()
r4.makeTree(4,r2,r3)
r5 = BinaryTree()
r5.makeTree(5,None,None)
r6 = BinaryTree()
r6.makeTree(6,None,None)
r7 = BinaryTree()
r7.makeTree(7,r5,r6)
r.makeTree(8,r4,r7)
print('PreOrder')
r.preOrder(r)
print('InOrder')
r.inOrder(r)
print('PostOrder')
r.postOrder(r)
print('levelOrder')
r.levelOrder(r)
print('invertOrder')
r.invertOrder(r)

from QuickSort import *

a = [2,4,10,3,2,4,1,5,4,9]
print(QuickSort(a))
