from LinkedList import *

list = LinkedList()
list.addEnd(1)
list.addEnd(2)
list.addEnd(3)
list.addEnd('a')
list.addEnd(3)
list.addEnd('b')
print(list.printList())

list.addHead(5)
print(list.printList())

for i in list.search(3):
    print(i)

list.remove(3)
print(list.printList())
